import json
import logging
from functools import lru_cache
from django.utils import timezone
from core.models import MatchEvent, Player, Action
import dateutil.parser

logger = logging.getLogger()

LabelStartPhase = 1
LabelEndPhase = 2
LabelGoal = 3
LabelOwnGoal = 4
LabelYellowCard = 5
LabelRedCard = 6
LabelSubIn = 7
LabelSubOut = 8
LabelOutOfPlay = 9
LabelFoul = 10
LabelPass = 11
LabelReception = 12
LabelGoalAttempt = 13
LabelSaveOnGoalAttempt = 14
LabelInterception = 15
LabelGoalKick = 16
LabelCorner = 17
LabelThrowIn = 18
LabelPenalty = 19
LabelFreeKick = 20
LabelTouch = 21
LabelDribble = 22
LabelClearance = 23
LabelDefensiveBlock = 24
LabelDuel = 25
LabelOffside = 26
LabelFreeKickOnGoal = 27

# properties
PropertyRightFoot = 1
PropertyLeftFoot = 2
PropertyHead = 3
PropertyHigh = 4
PropertyDirect = 5
PropertyFakePass = 6
PropertyCross = 7
PropertyCompleted = 8
PropertyNotCompleted = 9
PropertyDirectionForwards = 10
PropertyDirectionWide = 11
PropertyDirectionBack = 12
PropertyDiagonalForwardDirection = 13
PropertyDiagonalBackDirection = 14
PropertyLengthShort = 15
PropertyLengthMedium = 16
PropertyLengthLong = 17
PropertyBadControl = 18
PropertyError = 19
PropertyBigChance = 20
PropertyAirDuel = 21
PropertyGroundDuel = 22
PropertyDuelWon = 23
PropertyDuelLost = 24
PropertyBody = 25
PropertySliding = 26
PropertyTouched = 27
PropertyUntouched = 28
PropertyShieldOpponent = 29
PropertyOvertakeOpponentLeft = 30
PropertyOvertakeOpponentRight = 31
PropertyBlocked = 32
PropertySaveAGoal = 33
PropertyTrajectoryUnchanged = 34
PropertyPossessionRegain = 35
PropertyPossessionLost = 36
PropertyInterception = 37
PropertyCurvedIn = 38
PropertyCurvedOut = 39
PropertyStraight = 40
PropertyAssist = 41
PropertyKeyAction = 42
PropertyGoal = 43
PropertySaved = 44
PropertyOnThePost = 45
PropertyOnTheCrossBar = 46
PropertyWide = 47
PropertyOver = 48
PropertyShotOnTarget = 49
PropertyShotOffTarget = 50
PropertyDisallowedGoal = 51
PropertyIncorrect = 52
PropertyOnDeepPass = 53
PropertyOnCrossPass = 54
PropertyPunched = 55
PropertyCaught = 56
PropertyGround = 57
PropertyStanding = 58
PropertyDiving = 59
PropertySixSecondRule = 60
PropertyDangerousPlay = 61
PropertyHands = 62
PropertyObstruction = 63
PropertyProtest = 64
PropertySimulation = 65
PropertyTimeDelay = 66
PropertySuccessfulSave = 67
PropertyUnsuccessfulSave = 68
PropertyOffensivePart = 69
PropertyDefensivePart = 70
PropertyCornerShort = 71
PropertyPassThrow = 72
PropertySubjectedToFoul = 73
PropertyFiftyFiftyDuels = 74
PropertyThrowinKeepPossession = 75
PropertyShotBlocked = 76
PropertyPassFromHand = 77
PropertyGoalAttemptFromBuildUp = 78
PropertyGoalAttemptFromOffensive = 79
PropertyGoalAttemptFromCounter = 80
PropertyGoalAttemptFromTurnOver = 81
PropertyGoalAttemptFromSetPlay = 82
PropertyThrowinLong = 83
PropertyThrowInToOpponentBox = 84
PropertyFinalThirdEntry = 85

# player ones
Action70 = 70  # Last Line Save
Action71 = 71  # Last Man Tackle
Action36 = 36  # Defensive Block
Action32 = 32  # Tackle - Won
Action31 = 31  # Interception
Action33 = 33  # Tackle - Won (without Possession)
Action38 = 38  # Effective Clearance
Action18 = 18  # Aerial Duel - Won
Action19 = 19  # Aerial Duel - Lost
Action26 = 26  # Foul - Conceded
Action57 = 57  # Penalty Conceded
Action49 = 49  # Own Goal
Action27 = 27  # Handball Conceded
Action58 = 58  # Yellow Card
Action59 = 59  # 2nd Yellow Card
Action60 = 60  # Red Card
Action69 = 69  # Won Corner
Action73 = 73  # Penalty Won
Action61 = 61  # Great Skill
Action55 = 55  # Successful Take On (dribble)
Action25 = 25  # Foul - Won
Action67 = 67  # Dispossessed
Action56 = 56  # Unsuccessful dribble
Action62 = 62  # Big Error - lead to shot
Action80 = 80  # Goalkeeper Save
Action37 = 37  # Goalkeeper Claim
Action75 = 75  # Goalkeeper Punch
Action77 = 77  # Keeper pick-up
Action87 = 87  # Goal Kick  Successful
Action85 = 85  # Goalkeeper Throw - Successful
Action88 = 88  # Goal Kick Unsuccessful
Action79 = 79  # Cross not claimed
Action7 = 7  # Assist
Action8 = 8  # Key Pass
Action68 = 68  # Through Ball
Action5 = 5  # Successful Cross - Bonus
Action29 = 29  # Corners Into box - Successful
Action2 = 2  # Pass - Successful
Action3 = 3  # Pass - Unsuccessful
Action6 = 6  # Unsuccessful Crosses Total (excl corners & freekicks)
Action86 = 86  # Goalkeeper Throw - Unsuccessful
Action64 = 64  # Big Error - lead to goal
Action45 = 45  # Goal
Action63 = 63  # Shot hit the Post
Action43 = 43  # Shot on Target
Action53 = 53  # Shot Blocked
Action44 = 44  # Shot off Target
Action65 = 65  # Caught Offside
Action72 = 72  # Big Chance Missed
Action74 = 74  # Penalty Missed

# system ones
ActionPeriodStart = 10001
ActionPeriodEnd = 10002
ActionGoal = 10003
ActionSelfGoal = 10004
ActionLineUp = 10005
ActionMatchEnd = 10006
ActionSubstitution = 10007

# no operation
ActionNoop = 20000

# cancel
ActionCancel = 30000

ActionRules = {
    # Goal
    Action45: [{"properties": [], "labels": [3]}],

    # Assist
    Action7: [{"properties": [41], "labels": []}],

    # Penalty Won
    Action73: [{"properties": [89], "labels": []}],

    # Shot Hit Post
    Action63: [{"properties": [45], "labels": [13, 19, 27]},
               {"properties": [46], "labels": [13, 19, 27]}],

    # Shot On Target
    Action43: [{"properties": [49], "labels": [13, 19, 27]}],

    # Goalkeeper Save
    Action80: [{"properties": [67], "labels": [14]}],

    # Last Line Save
    Action70: [{"properties": [33], "labels": [24]}],

    # Shot Blocked
    Action53: [{"properties": [76], "labels": [13, 27]}],

    # Defensive Block
    Action36: [{"properties": [32], "labels": [24]}],

    # Tackle Won
    Action32: [{"properties": [22, 23, 70, 35], "labels": [25]}],

    # Successful Take On
    Action55: [{"properties": [30, 23], "labels": [25]},
               {"properties": [31, 23], "labels": [25]}],

    # Goalkeeper Claim
    Action37: [{"properties": [4, 56], "labels": [15]}],

    # Interception
    Action31: [{"properties": [37], "labels": []}],

    # Key Pass
    Action8: [{"properties": [42], "labels": []}],

    # Tackle - Won (without Possession)
    Action33: [{"properties": [22, 23, 70], "labels": [25], "excluded_properties": [35]}],

    # Shot off Target
    Action44: [{"properties": [47], "labels": [13, 19, 27]},
               {"properties": [48], "labels": [13, 19, 27]}],

    # Successful Cross - Bonus
    Action5: [{"properties": [7, 8], "labels": [11]}],

    # Goalkeeper Punch
    Action75: [{"properties": [55], "labels": [15]}],

    # Through Ball
    Action68: [{"properties": [91], "labels": [11]}],

    # Won Corner
    Action69: [{"properties": [86], "labels": []}],

    # Corners Into box - Successful
    Action29: [{"properties": [8, 90], "labels": [17]}],

    # Effective Clearance
    Action38: [{"properties": [], "labels": [23]}],

    # Aerial Duel - Won
    Action18: [{"properties": [21, 23], "labels": [25]}],

    # Foul - Won
    Action25: [{"properties": [73], "labels": [25]}],

    # Keeper pick-up
    Action77: [{"properties": [53, 56], "labels": [15], "excluded_properties": [4]}],

    # Goalkeeper Throw - Successful
    Action85: [{"properties": [8, 72], "labels": [11]}],

    # Goal Kick Successful
    Action87: [{"properties": [8], "labels": [16]}],

    # Pass - Successful
    Action2: [{"properties": [8], "labels": [11], "excluded_properties": [7]}],

    # Goal Kick Unsuccessful
    Action88: [{"properties": [9], "labels": [16]}],

    # Unsuccessful dribble
    Action56: [{"properties": [36], "labels": [22]}],

    # Unsuccessful Crosses Total
    Action6: [{"properties": [7, 9], "labels": [11]}],

    # Dispossessed
    Action67: [{"properties": [22, 36, 69], "labels": [25]}],

    # Foul - Conceded
    Action26: [{"properties": [], "labels": [10], "excluded_properties": [62, 88]}],

    # Aerial Duel - Lost
    Action19: [{"properties": [21, 22], "labels": [25]}],

    # Pass - Unsuccessful
    Action3: [{"properties": [9], "labels": [11], "excluded_properties": [7]}],

    # Handball Conceded
    Action27: [{"properties": [62], "labels": [10]}],

    # Caught Offside
    Action65: [{"properties": [], "labels": [26]}],

    # 2nd Yellow Card
    Action59: [{"properties": [92], "labels": [5]}],

    # Big Error - lead to shot
    Action62: [{"properties": [19], "labels": ["*"]}],

    # Yellow Card
    Action58: [{"properties": [], "labels": [5]}],

    # Penalty Conceded
    Action57: [{"properties": [88], "labels": [10]}],

    # Big Chance Missed
    Action72: [{"properties": [20], "labels": [13, 19, 27], "excluded_properties": [43]}],

    # Penalty Missed
    Action74: [{"properties": [], "labels": [19], "excluded_properties": [43]}],

    # Own Goal
    Action49: [{"properties": [], "labels": [4]}],

    # Red Card
    Action60: [{"properties": [], "labels": [6]}],

    #   Aerial Total
    #   Action17: [{"properties": [21], "labels": [25]}],
    #
    #   Clearance Lost
    #   Action39: [{"properties": [21], "labels": [25]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action30: [{"properties": [90,9], "labels": [17]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action28: [{"properties": [], "labels": [17]}],
    #
    #   Crosses Total (Open Delay)
    #   Action4: [{"properties": [7], "labels": [11]}],
    #
    #   Defensive/backward Passes
    #   Action12: [{"properties": [], "labels": [11]}],
    #
    #   Fouls Total
    #   Action24: [{"properties": [], "labels": [10]}],
    #
    #   Free Kicks Taken Total
    #   Action23: [{"properties": [], "labels": [20, 27]}],
    #
    #   Goals from Open Play
    #   Action46: [{"properties": [], "labels": [13, 19, 27], "excluded_properties": [82]}],
    #
    #   Goals from Penalties
    #   Action48: [{"properties": [], "labels": [43, 19]}],
    #
    #   Goals from Set Plays
    #   Action47: [{"properties": [82], "labels": [13, 27]}],
    #
    #   Ground Duels Lost
    #   Action22: [{"properties": [22, 23], "labels": [25]}],
    #
    #   Ground Duels Total
    #   Action20: [{"properties": [22], "labels": [25]}],
    #
    #   Ground Duels Won
    #   Action21: [{"properties": [22, 24], "labels": [25]}],
    #
    #   Headed Clearance Lost
    #   Action41: [],
    #
    #   Headed Clearance Won
    #   Action40: [],
    #
    #   Headed Shots off Target
    #   Action52: [{"properties": [3,50], "labels": [13]}],
    #
    #   Headed Shots on Target
    #   Action50: [{"properties": [3,49], "labels": [13]}],
    #
    #   Headed Shots Total
    #   Action-: [{"properties": [3], "labels": [13]}],
    #
    #   Long Passes Lost
    #   Action-: [{"properties": [9,17], "labels": [11]}],
    #
    #   Long Passes total
    #   Action-: [{"properties": [17], "labels": []}],
    #
    #   Long Passes Won
    #   Action-: [{"properties": [8], "labels": [11]}],
    #
    #   Offensive Passes Lost
    #   Action-: [{"properties": [9], "labels": [11]}],
    #
    #   Offensive Passes Total
    #   Action-: [{"properties": [], "labels": [11]}],
    #
    #   Offensive Passes Won
    #   Action-: [{"properties": [8], "labels": [11]}],
    #
    #   Passes Total
    #   Action-: [{"properties": [], "labels": [11]}],
    #
    #   Saves Total
    #   Action-: [{"properties": [], "labels": [14]}],
    #
    #   Sideway Passes Total
    #   Action-: [{"properties": [11], "labels": [11]}],
    #
    #   Total Shots
    #   Action-: [{"properties": [], "labels": [13,19,27]}],
    #
    #   Total Touches
    #   Action-: [{"properties": [], "labels": [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27]}],
}


def extract_match_events(match, current_period, event_body):
    annotation = get_annotation(event_body)
    if not annotation:
        return []

    minute, second = get_min_sec(event_body.get("Time", 0))
    result = []
    idx = 1

    matched_actions = match_actions(match, event_body)

    # calculate how much minutes we should add, this depends on period
    """
     ortec values:
    1 - 1st half
    2 - 2nd half
    3 - 1st extra time
    4 - 2nd extra time
    5 - penalties
    """
    add_min = 0
    if current_period == 1:
        add_min = 0
    elif current_period == 2:
        add_min = 45
    elif current_period == 3:
        add_min = 90
    elif current_period == 4:
        add_min = 105
    elif current_period == 5:
        add_min = 120

    # reduce matched_actions to action with max points if goal or assist present
    should_reduce = False
    for action in matched_actions:
        if action[0] in (ActionGoal, ActionSelfGoal, Action7, Action43):
            should_reduce = True
            break

    if should_reduce:
        non_point_actions = []

        # find action with biggest points
        max_action = None
        for action in matched_actions:
            if not action[2]:
                non_point_actions.append(action)
                continue

            if max_action is None or action[2] > max_action[2]:
                max_action = action

        matched_actions = [max_action] + non_point_actions

    for action in matched_actions:
        # try to find player and team by "person_id" and "selection_edition_id"
        player = None
        team = None

        player_id, team_id = None, None
        if action[3]:
            player_id = action[3]
        elif "PersonId" in annotation:
            player_id = str(annotation.get("PersonId"))

        if action[4]:
            team_id = action[4]
        elif "SelectionEditionId" in annotation:
            team_id = str(annotation.get("SelectionEditionId"))

        if player_id:
            player = get_player_by_person_id(player_id)
        if team_id:
            if match.is_ortec_home_selection_from_match(team_id):
                team = match.home_team
            elif match.is_ortec_away_selection_from_match(team_id):
                team = match.away_team

        match_event = MatchEvent()
        match_event.player = player
        match_event.team = team
        match_event.type = action[0]
        match_event.points = action[2]
        match_event.x = annotation.get("LocationX", 0)
        match_event.y = annotation.get("LocationY", 0)
        match_event.minute = minute + add_min
        match_event.second = second
        match_event.payload = json.dumps(action[1])
        match_event.provider_id = "{}_{}".format(annotation.get("Id"), idx)
        if event_body.get('DateTime'):
            match_event.timestamp = dateutil.parser.parse(event_body.get('DateTime'))
            match_event.has_real_timestamp = True
        else:
            match_event.timestamp = timezone.now()
        match_event.period = current_period
        result.append(match_event)

        idx += 1

    return result


def get_annotation(event_body):
    annotations = event_body.get("Annotations", [])
    if len(annotations) == 0:
        return None

    return annotations[0]


def get_min_sec(millis):
    mins = int(millis / 1000 / 60)
    secs = int(millis / 1000 % 60)
    return mins, secs


def match_actions(match, event_body):
    actions = []

    def cb(typ, payload=None, points=None, player_id=None, selection_edition_id=None):
        actions.append((typ, payload if payload else {}, points if points else 0, player_id, selection_edition_id,))

    for finder in finders:
        finder(match, event_body, cb)

    if len(actions) == 0:
        actions.append((ActionNoop, {}, 0, None, None))

    return actions


def phase_finder(match, event_body, cb):
    phase = event_body.get("Phase")
    label = get_annotation(event_body).get("Label")

    # convert phase to opta format
    if phase == 1:
        phase_converted = 1
    elif phase == 2:
        phase_converted = 2
    elif phase == 3:
        phase_converted = 3
    elif phase == 4:
        phase_converted = 4
    elif phase == 5:
        phase_converted = 5
    else:
        phase_converted = 0

    if label == LabelStartPhase:
        cb(ActionPeriodStart, payload={"period_id": phase_converted})
    elif label == LabelEndPhase:
        cb(ActionPeriodEnd, payload={"period_id": phase_converted})

    """
    ortec values:
    1 - 1st half
    2 - 2nd half
    3 - 1st extra time
    4 - 2nd extra time
    5 - penalties

    opta values:
    1 - first half
    2 - second half
    3 - first period of extra time
    4 - second period of extra time
    5 - penalty shoot out
    14 - post-game
    15 - pre-game
    16 - pre-match
    """


def goal_finder(match, event_body, cb):
    label = get_annotation(event_body).get("Label")

    # goal
    if label == 3:
        cb(ActionGoal)
    elif label == 4:
        cb(ActionSelfGoal)


def player_action_finder(match, event_body, cb):
    annotations = event_body.get("Annotations", [])
    for an in annotations:
        label = an.get("Label")
        properties = an.get("Properties", [])

        player_id = str(an.get("PersonId"))
        selection_edition_id = str(an.get("SelectionEditionId"))

        # iterate over rules and find corresponding actions
        for action_id, rules in ActionRules.items():
            for rule in rules:
                if match_action(rule, label, properties):
                    cb(action_id, {}, Action.get_score_by_id(action_id),
                       player_id=player_id,
                       selection_edition_id=selection_edition_id)
                    break


def match_action(rule, event_label, event_properties):
    labels = rule.get("labels", [])

    if len(labels) > 0:
        label_matched = False
        for rule_label in labels:
            if rule_label == "*" or rule_label == event_label:
                label_matched = True
                break

        if not label_matched:
            return False

    # check that all properties of rules is present
    for p in rule.get("properties", []):
        if not (p in event_properties):
            return False

    # check that there are no excluded properties present
    for p in rule.get("excluded_properties", []):
        if p in event_properties:
            return False

    return True


def substitution_finder(match, event_body, cb):
    annotations = event_body.get("Annotations", [])

    sub_in, sub_out = None, None
    for an in annotations:
        if an.get("Label") == LabelSubIn:
            sub_in = an
        elif an.get("Label") == LabelSubOut:
            sub_out = an

    if not sub_in or not sub_out:
        return

    player_in = get_player_by_person_id(sub_in.get("PersonId"))
    player_out = get_player_by_person_id(sub_out.get("PersonId"))

    cb(ActionSubstitution, {
        "in_player_id": str(player_in.id),
        "out_player_id": str(player_out.id),
    })


@lru_cache(maxsize=4096)
def get_player_by_person_id(person_id):
    try:
        return Player.objects.get(import_id=person_id)
    except Player.DoesNotExist:
        return Player.objects.create(
            import_id=person_id,
            first_name="John",
            last_name="Doe",
        )


finders = [
    phase_finder,
    goal_finder,
    substitution_finder,
    player_action_finder,
]
