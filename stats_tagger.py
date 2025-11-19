import re
from utils import events, event_shortcuts, outcomes, outcome_shortcuts


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
    
    # Get possible list of outcome shortcuts from list based on event
    possible_full_outcomes = outcomes[event]

    # Creates empty dict to store all possible shortcut values
    valid_shortcuts = {}

    # Iterates through all shortcuts and their full name pairings in the outcome_shortcuts dictionary
    for sc, full in outcome_shortcuts.items():
        # If the full name is in the possible_full_outcomes list then append pairing to dictionary
        if full in possible_full_outcomes:
            valid_shortcuts[sc] = full

    
    for o in sorted(valid_shortcuts, key = len, reverse = True):
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
    # Get event code and format it to remove all whitespace and make lowercase
    event = event.strip().lower().replace(" ","")
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

def inputEvent():
    e = input("Enter match event: ")
    return e