'''
Calls the functions from stats_tagger.py and stores match events accordingly

Prompts user for an input
Checks that input is not "end game"
Calls parse_event and stores the output (if any) in list match_events
Repeats
'''
from app.stats_tagger import parse_event, input_event, print_event
from app.utils import commands

match_events = []

print("Enter an event in the format 'event outcome(if applicable) player no. (if applicable)\nIf outcome or player no. not available, skip that section.\nE.g. foul commited by player 14: f14\nShot wide from player 12: sw14\nStart game:sg")
event = input_event()

while event!="end game" and event !="eg":
    event = event.strip().lower()
    if event in commands:
        if event=="delete":
            commands[event](match_events)
        else:
            commands[event]
    else:
        attempt_parse = parse_event(event)
        if attempt_parse:
            match_events.append(attempt_parse)
            print_event()
        else:
            print("Invalid event entered")
    event = input_event()

# Once match is done
print(match_events)
