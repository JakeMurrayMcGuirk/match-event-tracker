'''Functions that collect user inputs and parse them into events'''
# Importing dependencies
import re
from app.utils import event_shortcuts, outcomes, outcome_shortcuts


def get_event(event):
    '''Takes user input and gets the event code and event name from the input'''
    # Used ChatGPT to help with function to match event shortcuts WITHIN text
    for e in event_shortcuts:
        if event.startswith(e):
            # Return the shortcut code, full event name, and remaining text
            return event_shortcuts[e], event[len(e):]
    return None, None, event

def get_outcome(event, remaining_text):
    '''Takes in a string and extracts the outcome'''
    # Checks if the event is in a list of possible outcomes
    if event not in outcomes:
        return None, remaining_text

    # Get possible list of outcome shortcuts from list based on event
    possible_full_outcomes = outcomes[event]

    # Creates empty dict to store all possible shortcut values
    valid_shortcuts = {}

    # Iterates through all shortcut and full name pairings in the outcome_shortcuts dictionary
    for sc, full in outcome_shortcuts.items():
        # If full name is in possible_full_outcomes then append pairing to dictionary valid_shortcuts
        if full in possible_full_outcomes:
            valid_shortcuts[sc] = full

    for o in sorted(valid_shortcuts, key = len, reverse = True):
        # If text starts with outcome shortcut
        if remaining_text.startswith(o):
            # Returns outcome shortcut, remaining text
            return outcome_shortcuts[o], remaining_text[len(o):]
    return None, remaining_text


def get_player_no(remaining_text):
    '''Extracts player number from an inputted string'''
    # Regex search to find a number if at end of string
    player_no = re.search("\d+$", remaining_text)
    if player_no:
        player_no = player_no.group()
        return player_no
    return None


def parse_event(event):
    '''Take input and calls the above functions to parse it into an event
    First it makes the input lowercase and removes all whitespace.
    Then calls get_event to extract event_name from input
    Remaining text is fed into get_outcome to extract the outcome
    The leftover text after is fed into get_player_no to extract player no.
    All is returned to caller function.
    '''
    # Get event code and format it to remove all whitespace and make lowercase
    event = event.strip().lower().replace(" ","")
    # Used Chat GPT to help generate the below 3 lines
    event_name, remaining = get_event(event)
    if event_name is None:
        return None

    # Get outcome code
    outcome_name, remaining = get_outcome(event_name, remaining)

    # Get player no
    player_no = get_player_no(remaining)

    # Return event, outcome and player number
    return [event_name, outcome_name, player_no]

def input_event():
    '''Takes event input from user'''
    e = input("Enter match event: ")
    return e
