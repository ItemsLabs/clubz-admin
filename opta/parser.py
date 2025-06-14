import json
import logging
from functools import lru_cache
from django.utils import timezone
from core.models import MatchEvent, Player, Action
import dateutil.parser

logger = logging.getLogger()

LabelStartPhase = 32
LabelEndPhase = 30
LabelGoal = 16
LabelOwnGoal = 16 # But qualifier
LabelYellowCard = 17
LabelRedCard = 17
LabelSubIn = 7
LabelSubOut = 8
LabelOutOfPlay = 9
LabelFoul = 10
LabelPass = 1
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
PropertyOwnGoal = 28

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

# typeId / property = qualifier
# "properties_values" => a dict where key = property value / value = actual value that property could have
ActionRules = {
    # Goal
    Action45: [{ "labels": [16], "excluded_properties": [28] }],

    # Assist
    # Action7: [{ "labels": [1], "properties": [210], "properties_values": { 210: ["16"] }, "outcomes": [1] }],

    # Penalty Won
    Action73: [{ "labels": [4], "properties": [9], "outcomes": [1] }],

    # Shot Hit Post
    Action63: [{ "labels": [14], "outcomes": [1] }],

    # Goalkeeper Save
    Action80: [{ "labels": [10], "excluded_properties": [94] }],

    # Shot On Target
    Action43: [{ "labels": [15], "excluded_properties": [9, 82] }],

    # Key Pass
    Action8: [{ "labels": [1], "properties": [210], "properties_values": { 210: ["13", "14", "15"] } }],

    # Successful Cross - Bonus
    Action5: [{ "labels": [1], "properties": [2], "excluded_properties": [5, 6], "outcomes": [1] }],

    # Through Ball
    Action68: [{ "labels": [1], "properties": [4], "outcomes": [1] }],

    # Shot off Target
    Action44: [{ "labels": [13], "excluded_properties": [214] }],

    # Won Corner
    Action69: [{ "labels": [6] }],

    # Corners Into box - Successful
    Action29: [{ "labels": [1], "properties": [2, 6], "outcomes": [1] }],

    # Pass - Successful
    Action2: [{ "labels": [1], "excluded_properties": [210,2,4,5,6,107,123,124], "outcomes": [1] }],

    # Foul - Conceded - has to be 0
    Action26: [{ "labels": [4], "outcomes": [0], "excluded_properties": [10] }],

    # 2nd Yellow Card
    Action59: [{ "labels": [17], "properties": [32], "outcomes": [1] }],

    # Yellow Card
    Action58: [{ "labels": [17], "properties": [31], "outcomes": [1] }],

    # Penalty Missed
    Action74: [{ "labels": [15], "properties": [9] }],

    # Own Goal
    Action49: [{ "labels": [16], "properties": [28] }],

    # Red Card
    Action60: [{ "labels": [17], "properties": [33], "outcomes": [1] }],

    # Last Line Save
    Action70: [{ "labels": [10], "properties": [101], "outcomes": [1] }],

    # Last Man Tackle
    Action71: [{ "labels": [7], "properties": [14], "outcomes": [1] }],

    # Defensive Block
    Action36: [{ "labels": [10], "properties": [94], "outcomes": [1] }],

    # Great Skill
    Action61: [{ "labels": [42], "outcomes": [1] }],

    # Shot Blocked
    Action53: [{ "labels": [15], "properties": [82], "outcomes": [1] }],

    # Tackle Won
    Action32: [{ "labels": [7], "outcomes": [1], "excluded_properties": [14] }],

    # Successful Take On
    Action55: [{ "labels": [3], "outcomes": [1] }],

    # Goalkeeper Claim
    Action37: [{ "labels": [11], "properties": [88], "outcomes": [1] }],

    # Interception
    Action31: [{ "labels": [8], "outcomes": [1] }],

    # Tackle - Won (without Possession)
    Action33: [{ "labels": [7], "outcomes": [0] }],

    # Effective Clearance
    Action38: [{ "labels": [12], "outcomes": [1] }],

    # Aerial Duel - Won
    Action18: [{ "labels": [44], "outcomes": [1] }],

    # Foul - Won
    Action25: [{ "labels": [4], "outcomes": [1], "excluded_properties": [9] }],

    # Keeper pick-up
    Action77: [{ "labels": [52], "outcomes": [1] }],

    # Goalkeeper Throw - Successful
    Action85: [{ "labels": [1], "properties": [123], "outcomes": [1] }],

    # Goal Kick Successful
    Action87: [{ "labels": [1], "properties": [124], "outcomes": [1] }],

    # Goal Kick Unsuccessful - has to be 0
    Action88: [{ "labels": [1], "properties": [124], "outcomes": [0] }],

    # Aerial Duel - Lost - has to be 0
    Action19: [{ "labels": [44], "outcomes": [0] }],

    # Unsuccessful dribble - has to be 0
    Action56: [{ "labels": [3], "outcomes": [0] }],

    # Dispossessed
    Action67: [{ "labels": [50], "outcomes": [1] }],

    # Goalkeeper Throw - Unsuccessful - has to be 0
    Action86: [{ "labels": [1], "properties": [123], "outcomes": [0] }],

    # Unsuccessful Crosses Total - has to be 0
    Action6: [{ "labels": [1], "properties": [2], "excluded_properties": [5, 6], "outcomes": [0] }],

    # Pass - Unsuccessful - has to be 0
    Action3: [{ "labels": [1], "excluded_properties": [2, 4, 5, 6, 107, 123, 124], "outcomes": [0] }],

    # Handball Conceded - has to be 0
    Action27: [{ "labels": [4], "properties": [10], "outcomes": [0] }],

    # Caught Offside
    Action65: [{ "labels": [2], "properties": [7], "outcomes": [1] }],

    # Cross not claimed - has to be 1
    Action79: [{ "labels": [53], "outcomes": [1] }],

    # Big Error - lead to shot
    Action62: [{ "labels": [51], "properties": [169], "outcomes": [1] }],

    # Penalty Conceded - has to be 1
    Action57: [{ "labels": [4], "properties": [9], "outcomes": [0] }],

    # Big Error - lead to goal
    Action64: [{ "labels": [51], "properties": [170] }],

    # Big Chance Missed
    Action72: [{ "labels": [13], "properties": [214], "outcomes": [1] }],

    # Goalkeeper Punch
    Action75: [{ "labels": [41], "properties": []}],

    # # Successful Take On
    # Action55: [{ "labels": [3], "properties": [], "outcomes": [1] }],

    # # Aerial Duel - Lost - has to be 0
    # # Action19: [{ "labels": [44], "properties": [], "outcomes": [0] }],

    #   Aerial Total
    #   Action17: [{ "labels": [21], "properties": [25]}],
    #
    #   Clearance Lost - has to be 0
    #   Action39: [{ "labels": [21], "properties": [25]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action30: [{ "labels": [90,9], "properties": [17]}],
    #
    #   Corners Into box - Unsuccessful
    #   Action28: [{ "labels": [], "properties": [17]}],
    #
    #   Crosses Total (Open Delay)
    #   Action4: [{ "labels": [7], "properties": [11]}],
    #
    #   Defensive/backward Passes
    #   Action12: [{ "labels": [], "properties": [11]}],
    #
    #   Fouls Total
    #   Action24: [{ "labels": [], "properties": [10]}],
    #
    #   Free Kicks Taken Total
    #   Action23: [{ "labels": [], "properties": [20, 27]}],
    #
    #   Goals from Open Play
    #   Action46: [{ "labels": [], "properties": [13, 19, 27], "excluded_properties": [82]}],
    #
    #   Goals from Penalties
    #   Action48: [{ "labels": [], "properties": [43, 19]}],
    #
    #   Goals from Set Plays
    #   Action47: [{ "labels": [82], "properties": [13, 27]}],
    #
    #   Ground Duels Lost - has to be 0
    #   Action22: [{ "labels": [22, 23], "properties": [25]}],
    #
    #   Ground Duels Total
    #   Action20: [{ "labels": [22], "properties": [25]}],
    #
    #   Ground Duels Won
    #   Action21: [{ "labels": [22, 24], "properties": [25]}],
    #
    #   Headed Clearance Lost - has to be 0
    #   Action41: [],
    #
    #   Headed Clearance Won
    #   Action40: [],
    #
    #   Headed Shots off Target
    #   Action52: [{ "labels": [3,50], "properties": [13]}],
    #
    #   Headed Shots on Target
    #   Action50: [{ "labels": [3,49], "properties": [13]}],
    #
    #   Headed Shots Total
    #   Action-: [{ "labels": [3], "properties": [13]}],
    #
    #   Long Passes Lost - has to be 0
    #   Action-: [{ "labels": [9,17], "properties": [11]}],
    #
    #   Long Passes total
    #   Action-: [{ "labels": [17], "properties": []}],
    #
    #   Long Passes Won
    #   Action-: [{ "labels": [8], "properties": [11]}],
    #
    #   Offensive Passes Lost - has to be 0
    #   Action-: [{ "labels": [9], "properties": [11]}],
    #
    #   Offensive Passes Total
    #   Action-: [{ "labels": [], "properties": [11]}],
    #
    #   Offensive Passes Won
    #   Action-: [{ "labels": [8], "properties": [11]}],
    #
    #   Passes Total
    #   Action-: [{ "labels": [], "properties": [11]}],
    #
    #   Saves Total
    #   Action-: [{ "labels": [], "properties": [14]}],
    #
    #   Sideway Passes Total
    #   Action-: [{ "labels": [11], "properties": [11]}],
    #
    #   Total Shots
    #   Action-: [{ "labels": [], "properties": [13,19,27]}],
    #
    #   Total Touches
    #   Action-: [{ "labels": [], "properties": [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27]}],
}


def extract_match_events(match, event_body):
    minute = event_body.get("timeMin", 0)
    second = event_body.get("timeSec", 0)
    result = []

    matched_actions = match_actions(match, event_body)

    # calculate how much minutes we should add, this depends on period
    """
    opta values:
    • 1 (First half)
    • 2 (Second half)
    • 3 (Extra time - first half)
    • 4 (Extra time - second half)
    • 5 (Penalty shootout)
    • 10 (Half time)
    • 11 (End of second half - before extra time)
    • 12 (Extra time half time)
    • 13 (End of extra time - before penalties)
    • 14 (Full time)
    • 16 (Pre-match)
    """
    current_period = event_body.get("periodId", 0)

    # reduce matched_actions to action with max points if goal or assist present
    should_reduce = False
    for action in matched_actions:
        if action[0] in (ActionGoal, ActionSelfGoal, Action7, Action43):
            # print("should_reduce action: {}".format(action[0]))
            should_reduce = True
            break

    if should_reduce:
        # print("matched_actions before: {}".format(matched_actions))
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
        # print("matched_actions after: {}".format(matched_actions))

    if matched_actions is None:
        print("[matched_actions] IS NONE! - event_body: {}".format(event_body))

    for action in matched_actions:
        try:
            if action is None or action[0] == ActionNoop:
                continue
        except:
            print("[matched_actions] action failed: ", action)

        # try to find player and team by "person_id" and "selection_edition_id"
        player = None
        team = None

        player_id, team_id = None, None

        if action and action[3]:
            player_id = action[3]

        if action and action[4]:
            team_id = action[4]

        if player_id:
            player = get_player_by_person_id(player_id)
        if team_id:
            if match.is_opta_home_selection_from_match(team_id):
                team = match.home_team
            elif match.is_opta_away_selection_from_match(team_id):
                team = match.away_team

        match_event = MatchEvent()
        match_event.player = player
        match_event.team = team
        match_event.type = action[0]
        match_event.points = action[2]
        match_event.x = event_body.get("x", 0)
        match_event.y = event_body.get("y", 0)
        match_event.period = current_period
        match_event.minute = minute
        match_event.second = second
        match_event.payload = json.dumps(action[1])
        match_event.provider_id = event_body.get("id")
        if event_body.get('timeStamp'):
            match_event.timestamp = dateutil.parser.parse(event_body.get('timeStamp'))
            match_event.has_real_timestamp = True
        else:
            match_event.timestamp = timezone.now()
            match_event.has_real_timestamp = False

        result.append(match_event)

    return result

def match_actions(match, event_body):
    actions = []

    def cb(typ, payload=None, points=None, player_id=None, selection_edition_id=None):
        actions.append((typ, payload if payload else {}, points if points else 0, player_id, selection_edition_id))

    for finder in finders:
        finder(match, event_body, cb)

    if len(actions) == 0:
        # print("No action found for event", event_body.get("typeId"))
        actions.append((ActionNoop, {}, 0, None, None))
    return actions


def phase_finder(match, event_body, cb):
    label = event_body.get("typeId")
    periodId = event_body.get("periodId")
    if label == LabelStartPhase:
        cb(ActionPeriodStart, payload={"period_id": periodId})
    elif label == LabelEndPhase:
        cb(ActionPeriodEnd, payload={"period_id": periodId})

    """
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
    label = event_body.get("typeId")
    if label == (LabelGoal or LabelOwnGoal):
        for qualifier in event_body.get("qualifier", []):
            qualifierId = qualifier.get("qualifierId")
            if qualifierId == PropertyOwnGoal:
                cb(ActionSelfGoal, {}, Action.get_score_by_id(Action49), event_body.get("playerId"), event_body.get("contestantId"))
                return # set as own goal if done it, else, should be a score for the team
        cb(ActionGoal, {}, Action.get_score_by_id(Action45), event_body.get("playerId"), event_body.get("contestantId"))


def player_action_finder(match, event_body, cb):
        id = event_body.get("id")
        label = event_body.get("typeId")
        properties = event_body.get("qualifier", [])
        outcome = event_body.get("outcome", None)

        player_id = event_body.get("playerId", None)
        selection_edition_id = event_body.get("contestantId", None)
        rr = None
        if player_id is not None or selection_edition_id is not None:
            # iterate over rules and find corresponding actions
            for action_id, rules in ActionRules.items():
                for rule in rules:
                    if match_action(rule, label, properties, outcome, id):
                        cb(action_id, {}, Action.get_score_by_id(action_id),
                            player_id=player_id,
                            selection_edition_id=selection_edition_id)
                        rr = rule
                        break
        # print(f"id: {id} - label: {label} - rule: {rr}")



def match_action(rule, event_label, event_properties, outcome = None, id = None):
    labels = rule.get("labels", [])
    if len(labels) > 0:
        label_matched = False
        for rule_label in labels:
            if rule_label == "*" or rule_label == event_label:
                label_matched = True
                break

        if not label_matched:
            return False

    # check that all properties of rules are present in the event
    rule_properties = rule.get("properties", [])
    if len(rule_properties) > 0 and not all(elem in [e['qualifierId'] for e in event_properties] for elem in rule_properties):
        return False
    # if there are any related property values should match the event qualifier value
    property_values = rule.get("properties_values", None)
    if property_values is not None:
        for e in event_properties:
            values = property_values.get(e['qualifierId'], None)
            if values is not None and isinstance(values, list):
                if str(e.get("value")) not in values:
                    print(False)

    # check that there are no excluded properties present
    rule_excluded_properties = rule.get("excluded_properties", [])
    if len(rule_excluded_properties) > 0 and any(elem in [e['qualifierId'] for e in event_properties] for elem in rule_excluded_properties):
        return False

    possible_outcomes = rule.get("outcomes", [])
    if len(possible_outcomes) > 0 and outcome is not None and outcome not in possible_outcomes:
        return False

    return True


@lru_cache(maxsize=4096)
def get_player_by_person_id(player_id, fn=None, ln=None, nn=None, dob=None):
    try:
        return Player.objects.get(import_id=player_id)
    except Player.DoesNotExist:
        if player_id:
            return Player.objects.create(
                import_id=player_id,
                first_name=fn,
                last_name=ln,
                full_name="{} {}".format(fn, ln),
                nick_name=nn,
                birth_date= dob,
            )


def assist_finder(match, event_body, cb):
    label = event_body.get("typeId")
    if label == LabelPass and event_body.get("assist", 0) == 1 and event_body.get("outcome", 0) == 1:
        cb(Action7, {}, Action.get_score_by_id(Action7), event_body.get("playerId"), event_body.get("contestantId"))

finders = [
    goal_finder,
    phase_finder,
    assist_finder,
    player_action_finder,
]
