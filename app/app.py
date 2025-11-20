'''
Calls the functions from stats_tagger.py and stores match events accordingly

Prompts user for an input, calls parse_event (unless "end game" is input), and stores the output (if any) in a list (match_events)
'''
from app.stats_tagger import parse_event, inputEvent
from app.utils import commands

match_events = []

print("Enter an event in the format 'event outcome(if applicable) player no. (if applicable)\nIf outcome or player no. not available, skip that section.\nE.g. foul commited by player 14: f14\nShot wide from player 12: sw14\nStart game:sg")
event = inputEvent()

while event.strip().lower()!="end game":
    event = event.strip().lower()
    if event in commands:
        print(commands[event])
    else:
        attempt_parse = parse_event(event)
        if attempt_parse:
            match_events.append(attempt_parse)
            print(attempt_parse)
        else:
            print("Invalid event entered")
    event = inputEvent()

# Once match is done
print(match_events)