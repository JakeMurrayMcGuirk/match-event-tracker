from stats_tagger import get_teams, get_event, get_outcome, get_player_no, parse_event, inputEvent
from utils import commands

match_events = []

print("Enter an event in the format 'event outcome(if applicable) player no. (if applicable)\nIf outcome or player no. not available, skip that section.\nE.g. foul commited by player 14: f14\nShot wide from player 12: sw14\nStart game:sg")
event = inputEvent()

while event.strip.lower()!="end game":
    event = event.strip.lower()
    if event in commands:
        print(commands[event])
    else:
        attempt_parse = parse_event(event)
        if attempt_parse:
            match_events.append(attempt_parse)
            print(attempt_parse)
        else:
            print("Invalid event entered")