import re
from utils import events, event_shortcuts, outcomes, outcome_shortcuts

def get_teams():
    team1 = input("Enter team 1 name: ")
    team2 = input("Enter team 2 name: ")



def get_event(event):
    # Used ChatGPT to help with function to match event shortcuts WITHIN text
    for e in event_shortcuts:
        if event.startswith(e):
            # Return the shortcut code, full event name, and remaining text
            return e, event_shortcuts[e], event[len(e):]
    return None, None, event

def get_outcome(event, remaining_text):
    # Checks if the event is in a list of possible outcomes
    if event not in outcomes:
        return None, remaining_text
    
    # Get possible list of outcome shortcuts from dictionary
    possible_outcomes = outcomes[event]
    
    for o in sorted(possible_outcomes, key = len, reverse = True):
        # If text starts with outcome shortcut
        if remaining_text.startswith(o):
            # Returns outcome shortcut, remaining text
            return outcome_shortcuts[o], remaining_text[len(o):]
    return None, remaining_text


def get_player_no(remaining_text):
    player_no = re.search("\d+$", remaining_text)
    if player_no:
        player_no = player_no.group()
        return player_no
    return None


def parse_event(event):
    # Get event code and format it
    event = event.strip().lower()
    # Used Chat GPT to help generate the below 3 lines
    event_code, event_name, remaining = get_event(event)
    if event_name is None:
        return None
    
    # Get outcome code
    outcome_name, remaining = get_outcome(event_name, remaining)

    # Get player no
    player_no = get_player_no(remaining)

    # Return event, outcome and player number
    return [event_name, outcome_name, player_no]


match_events=[]

def inputEvent():
    e = input("Enter match event: ")
    return e

event = inputEvent()

while inputEvent()!="end game":
    inputEvent()