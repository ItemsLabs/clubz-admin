import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any

from ortools.constraint_solver.pywrapcp import (Solver)
from ortools.sat.python import cp_model

from core.models import AppInbox, CustomUser

import divisions


@dataclass
class Division:
    id: uuid.UUID
    tier: int
    percentage: float


@dataclass
class User:
    id: uuid.UUID
    division_tier: Optional[int]
    division_id: Optional[uuid.UUID]
    verified: bool


@dataclass
class DistributionResult:
    id: uuid.UUID
    capacity: int
    promotion_count: int
    relegation_count: int


def calculate_desired_capacity(divisions: List[Division], user_count: int) -> Dict[int, int]:
    division_capacity = {}
    total = user_count
    left = total
    for i in range(len(divisions)):
        d = divisions[i]
        if i == len(divisions) - 1:
            num_users = left
        else:
            num_users = int(d.percentage * total)
            left -= num_users

        division_capacity[d.tier] = num_users

    return division_capacity


class DivisionHolder:
    def __init__(
            self,
            divisions: List[Division],
            relegation_ranges: Dict[int, Tuple[float, float]],
            promotion_ranges: Dict[int, Tuple[float, float]],
    ):
        self._divisions = sorted(divisions, key=lambda d: d.tier)
        self._division_map = {d.id: d for d in divisions}
        self._relegation_ranges = {}
        self._promotion_ranges = {}
        self._division_tier_to_id = {d.tier: d.id for d in divisions}

        for div_tier, ranges in relegation_ranges.items():
            div_id = self._division_tier_to_id.get(div_tier)
            if div_id is None:
                continue
            self._relegation_ranges[div_id] = (ranges[0], ranges[1])

        for div_tier, ranges in promotion_ranges.items():
            div_id = self._division_tier_to_id.get(div_tier)
            if div_id is None:
                continue
            self._promotion_ranges[div_id] = (ranges[0], ranges[1])

    def can_relegate(self, division_id: uuid.UUID) -> bool:
        return self.prev_division(division_id) is not None

    def can_promote(self, division_id: uuid.UUID) -> bool:
        return self.next_division(division_id) is not None

    def next_division(self, division_id: uuid.UUID) -> Optional[uuid.UUID]:
        division = self._division_map[division_id]
        next_tier = division.tier - 1
        return self._division_tier_to_id.get(next_tier, None)

    def prev_division(self, division_id: uuid.UUID) -> Optional[uuid.UUID]:
        division = self._division_map[division_id]
        next_tier = division.tier + 1
        return self._division_tier_to_id.get(next_tier, None)

    def calculate_desired_capacity(self, division_id: uuid.UUID, total_users: int) -> int:
        total_capacity = self.calculate_total_desired_capacity(total_users)
        return total_capacity.get(division_id, 0)

    def calculate_total_desired_capacity(self, total_users: int) -> Dict[uuid.UUID, int]:
        division_capacity = {}
        left = total_users
        for i in range(len(self._divisions)):
            d = self._divisions[i]
            if i == len(self._divisions) - 1:
                num_users = left
            else:
                num_users = int(d.percentage * total_users)
                left -= num_users

            division_capacity[d.id] = num_users

        return division_capacity

    def promotion_range(self, division_id: uuid.UUID) -> Tuple[float, float]:
        return self._promotion_ranges.get(division_id, (0.0, 0.0))

    def relegation_range(self, division_id: uuid.UUID) -> Tuple[float, float]:
        return self._promotion_ranges.get(division_id, (0.0, 0.0))


class OrToolsDistributionStrategy:
    def __init__(self,
                 divisions: List[Division],
                 relegation_ranges: Dict[int, Tuple[float, float]],
                 promotion_ranges: Dict[int, Tuple[float, float]],
                 debug: bool):
        self.divisions = divisions
        self.debug = debug
        self.relegation_ranges = relegation_ranges
        self.promotion_ranges = promotion_ranges
        self.holder = DivisionHolder(self.divisions, relegation_ranges, promotion_ranges)

    def calculate_capacity(self, division_population: Dict[uuid.UUID, int]) -> Dict[uuid.UUID, DistributionResult]:
        total_capacity = sum([v for v in division_population.values()])
        desired_capacity = self.holder.calculate_total_desired_capacity(total_capacity)
        given_capacity = {div.id: division_population.get(div.id, 0) for div in self.divisions}

        model = cp_model.CpModel()

        num_users = total_capacity

        promotion_count = {}
        relegation_count = {}
        for div in self.divisions:
            capacity = given_capacity[div.id]
            promotion_count[div.id] = model.new_int_var(0, capacity, f"promotion_{div.id}")
            relegation_count[div.id] = model.new_int_var(0, capacity, f"relegation_{div.id}")

            model.Add(promotion_count[div.id] + relegation_count[div.id] <= capacity)

            can_relegate = self.holder.can_relegate(div.id)
            can_promote = self.holder.can_promote(div.id)

            if can_relegate:
                relegate_range = self.holder.relegation_range(div.id)
                min_relegate = int(capacity * relegate_range[0])
                max_relegate = int(capacity * relegate_range[1])
                model.Add(relegation_count[div.id] >= min_relegate)
                model.Add(relegation_count[div.id] <= max_relegate)
            else:
                model.Add(relegation_count[div.id] == 0)

            if can_promote:
                promote_range = self.holder.promotion_range(div.id)
                min_promote = int(capacity * promote_range[0])
                max_promote = int(capacity * promote_range[1])
                model.Add(promotion_count[div.id] >= min_promote)
                model.Add(promotion_count[div.id] <= max_promote)
            else:
                model.Add(promotion_count[div.id] == 0)

        # score function, minimize diff between desired and given
        capacity_diff = {div.id: model.new_int_var(0, num_users, f"cap_diff_{div.id}") for div in self.divisions}

        for div in self.divisions:
            capacity = given_capacity[div.id]
            next_capacity = model.new_int_var(0, num_users, f"next_capacity_{div.id}")

            next_div_id = self.holder.next_division(div.id)
            prev_div_id = self.holder.prev_division(div.id)

            if next_div_id is not None and prev_div_id is not None:
                # both promotion and relegation
                model.Add(
                    next_capacity == capacity + promotion_count[prev_div_id] + relegation_count[next_div_id]
                    - relegation_count[div.id] - promotion_count[div.id])
            elif next_div_id is not None:
                model.Add(next_capacity == capacity + relegation_count[next_div_id] - promotion_count[div.id])
            elif prev_div_id is not None:
                model.Add(next_capacity == capacity + promotion_count[prev_div_id] - relegation_count[div.id])

            v = model.new_int_var(-num_users, num_users, f"v_{div.id}")
            model.Add(v == next_capacity - desired_capacity[div.id])
            model.AddAbsEquality(capacity_diff[div.id], v)

        model.Minimize(sum(capacity_diff.values()))

        solver = cp_model.CpSolver()
        status = solver.solve(model)

        result = {}
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            sum_diff = 0
            for div in self.divisions:
                curr_cap = given_capacity[div.id]
                desired_cap = desired_capacity[div.id]
                promotion = solver.Value(promotion_count[div.id])
                relegation = solver.Value(relegation_count[div.id])
                cap_diff = solver.Value(capacity_diff[div.id])
                sum_diff += cap_diff

                result[div.id] = DistributionResult(div.id, curr_cap, promotion, relegation)
                if self.debug:
                    print(f"CalculateCapacity. div #{div.tier}, curr: {curr_cap}, desired: {desired_cap}, promotion: {promotion}, relegation: {relegation}, cap_diff: {cap_diff}")
            if self.debug:
                print(f"CalculateCapacity.Sum diff is {sum_diff}")
        else:
            if self.debug:
                print("No solutions")

        return result

    def distribute(self, users: List[User], leaderboard: Dict[int, int], week) -> Dict[uuid.UUID, Dict[str, Any]]:
        genesis_users = [user for user in users if user.division_tier is None]
        division_users = [user for user in users if user.division_tier is not None]

        desired_capacity = calculate_desired_capacity(self.divisions, len(division_users))
        given_capacity = {div.tier: 0 for div in self.divisions}
        for user in division_users:
            if user.division_tier is not None:
                given_capacity[user.division_tier] += 1

        model = cp_model.CpModel()

        num_users = len(division_users)
        num_divisions = len(self.divisions)

        promotion_count = {}
        relegation_count = {}
        for i in range(num_divisions):
            div_tier = self.divisions[i].tier
            capacity = given_capacity[div_tier]
            promotion_count[i] = model.new_int_var(0, capacity, f"promotion_{i}")
            relegation_count[i] = model.new_int_var(0, capacity, f"relegation_{i}")

            model.Add(promotion_count[i] + relegation_count[i] <= capacity)

            can_relegate = i != 0 and i != 1
            can_promote = i != num_divisions - 1

            if can_relegate:
                relegate_range = self.relegation_ranges[div_tier]
                min_relegate = int(capacity * relegate_range[0])
                max_relegate = int(capacity * relegate_range[1])
                model.Add(relegation_count[i] >= min_relegate)
                model.Add(relegation_count[i] <= max_relegate)
            else:
                model.Add(relegation_count[i] == 0)

            if can_promote:
                promote_range = self.promotion_ranges[div_tier]
                min_promote = int(capacity * promote_range[0])
                max_promote = int(capacity * promote_range[1])
                model.Add(promotion_count[i] >= min_promote)
                model.Add(promotion_count[i] <= max_promote)
            else:
                model.Add(promotion_count[i] == 0)

        # score function, minimize diff between desired and given
        capacity_diff = [model.new_int_var(0, num_users, f"cap_diff_{i}") for i in range(num_divisions)]
        for i in range(num_divisions):
            div_tier = self.divisions[i].tier
            capacity = given_capacity[div_tier]
            next_capacity = model.new_int_var(0, num_users, f"next_capacity_{i}")

            if i == 0:
                model.Add(next_capacity == capacity - promotion_count[i] + relegation_count[i + 1])
            elif i == (num_divisions - 1):
                model.Add(next_capacity == capacity + promotion_count[i - 1] - relegation_count[i])
            else:
                model.Add(
                    next_capacity == capacity + promotion_count[i - 1] - relegation_count[i] - promotion_count[i] +
                    relegation_count[i + 1])

            v = model.new_int_var(-num_users, num_users, f"v_{i}")
            model.Add(v == next_capacity - desired_capacity[div_tier])
            model.AddAbsEquality(capacity_diff[i], v)

        model.Minimize(sum(capacity_diff))

        solver = cp_model.CpSolver()
        status = solver.solve(model)

        result = {}
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            divs = []
            sum_diff = 0
            for i in range(num_divisions):
                div_tier = self.divisions[i].tier
                curr_cap = given_capacity[div_tier]
                desired_cap = desired_capacity[div_tier]
                promotion = solver.Value(promotion_count[i])
                relegation = solver.Value(relegation_count[i])
                cap_diff = solver.Value(capacity_diff[i])
                sum_diff += cap_diff

                divs.append(
                    (div_tier, curr_cap, desired_cap, promotion, relegation, cap_diff),
                )

                users_in_division = [user for user in division_users if user.division_tier == div_tier]
                # sort users by score
                users_in_division.sort(key=lambda x: leaderboard[x.id], reverse=True)

                promoted_users = set()
                relegated_users = set()

                # top N gets promoted
                if promotion > 0:
                    for user in users_in_division[:promotion]:
                        user_data = {
                            'position': 0,  # default data
                            'week_division_tier': user.division_tier,
                            'points': leaderboard[user.id],
                            'coins': 0,  # default data

                            'new_division_tier': user.division_tier - 1,
                            'division_status': 'p',  # promoted
                        }
                        result[user.id] = user_data
                        promoted_users.add(user.id)
                        self.send_app_inbox_notification(user.id, "Promoted", user.division_tier, week)

                # worst M got relegation
                if relegation > 0:
                    for user in users_in_division[-relegation:]:
                        user_data = {
                            'position': 0,  # default data
                            'week_division_tier': user.division_tier,
                            'points': leaderboard[user.id],
                            'coins': 0,  # default data

                            'new_division_tier': user.division_tier + 1,
                            'division_status': 'r',  # relegated
                        }
                        result[user.id] = user_data
                        relegated_users.add(user.id)
                        self.send_app_inbox_notification(user.id, "Relegated", user.division_tier, week)

                # everyone else stays where they are, send 'Safe' notification only to those who are neither promoted nor relegated
                for user in users_in_division:
                    if user.id not in promoted_users and user.id not in relegated_users:
                        user_data = {
                            'position': 0,  # default data
                            'week_division_tier': user.division_tier,
                            'points': leaderboard[user.id],
                            'coins': 0,  # default data

                            'new_division_tier': user.division_tier,
                            'division_status': 's',  # safe
                        }
                        result[user.id] = user_data
                        self.send_app_inbox_notification(user.id, "Safe in division", user.division_tier, week)

                if self.debug:
                    print(
                        f"div #{div_tier}, curr: {curr_cap}, desired: {desired_cap}, promotion: {promotion}, relegation: {relegation}, cap_diff: {cap_diff}")
            if self.debug:
                print(f"Sum diff is {sum_diff}")
        else:
            if self.debug:
                print("No solutions")

        # verified users goes into 10,9,8,7,6. Overall 5 partitions
        verified_genesis = [user for user in genesis_users if user.verified]
        if verified_genesis:
            self.add_to_dict(self.distribute_by_divisions(verified_genesis, leaderboard, self.divisions[0:5]), result)

        # non verified goes into 10,9,8. Overall 3 partitions
        non_verified_genesis = [user for user in genesis_users if not user.verified]
        if non_verified_genesis:
            self.add_to_dict(self.distribute_by_divisions(non_verified_genesis, leaderboard, self.divisions[0:3]),
                            result)

        return result


    def add_to_dict(self, source: Dict[int, int], dest: Dict[int, Dict[str, Any]]):
        for k, v in source.items():
            dest[k] = v

    # uniform distribute users by divisions
    def distribute_by_divisions(
            self,
            users: List[User],
            leaderboard: Dict[int, int],
            divisions: List[Division],
    ) -> Dict[int, Dict[str, Any]]:
        result = {}

        # sort by leaderboard places
        users.sort(key=lambda x: leaderboard[x.id])

        partitions = self.partition_indices(len(users), len(divisions))
        for i in range(len(partitions)):
            for user_idx in range(partitions[i][0], partitions[i][1] + 1):
                user_data = {
                    'position': 0,  # default data
                    'week_division_tier': None,
                    'points': leaderboard[users[user_idx].id],
                    'coins': 0,  # default data

                    'new_division_tier': divisions[i].tier,
                    'division_status': 'p',  # promoted
                }
                result[users[user_idx].id] = user_data

        return result

    def division_num_to_idx(self, num):
        # 10 -> 0
        # 9 -> 1
        # etc.
        return 10 - num

    def partition_indices(self, size, num_partitions):
        if num_partitions <= 0 or size <= 0:
            raise ValueError("Length and number of partitions must be positive integers")

        partitions = []
        partition_size = size // num_partitions
        remainder = size % num_partitions

        start = 0
        for i in range(num_partitions):
            end = start + partition_size - 1
            if remainder > 0:
                end += 1
                remainder -= 1
            partitions.append((start, end))
            start = end + 1

        return partitions

    def send_app_inbox_notification(self, user_id, status, division_tier,week):
        user = CustomUser.objects.get(id=user_id)
        title = f"You have been {status}!"
        description = f"You are now {status.lower()} in division {division_tier}."
        
        # Set the image URL based on the status
        if status == 'Promoted':
            image_url = "https://laliga.ams3.digitaloceanspaces.com/notification-icons/promotion.png"
        elif status == 'Relegated':
            image_url = "https://laliga.ams3.digitaloceanspaces.com/notification-icons/demotion.png"
        else:  # Assume 'Safe' status
            image_url = "https://laliga.ams3.digitaloceanspaces.com/notification-icons/safe.png"
        
        # Create a new AppInbox entry
        AppInbox.objects.create(
            user=user,
            title=title,
            description=description,
            status='Active',
            priority='High',
            category='division_end',
            game_week_id=week,
            image_url=image_url  # Add the image URL here
        )