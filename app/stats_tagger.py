'''Functions that collect user inputs and parse them into events'''
# Importing dependencies
import re
from app.utils import event_shortcuts, outcomes, outcome_shortcuts, event_categories, param_rules

def get_event(event):
    '''Takes user input and gets the event code and event name from the input'''
    # Used ChatGPT to help with function to match event shortcuts WITHIN text
    for e in event_shortcuts:
        if event.startswith(e):
            # Return the full event name, and remaining text
            return event_shortcuts[e], event[len(e):]
    return None, event

def get_event_rules(event_name):
    '''Get and return the ruleset for the input event'''
    if event_name is None:
        return None
    # Iterate through event_categories
    for e in event_categories:
        if event_name in event_categories[e]:
            event_category = e
    # Get ruleset from param_rules
    ruleset = param_rules[event_category]
    return ruleset

def validate_event(event_name, remaining_text, ruleset):
    '''Validates that user input is valid'''
    # Check if event name is null
    if event_name is None:
        return False
    # Checks if remaining_text is None
    if remaining_text is None:
        remaining_text=""
    # If ruleset allows for outcome and player_no
    if ruleset['outcome'] and ruleset['player_no']:
        if remaining_text is None:
            return False
        # Use regex to check if remaining text is just a digit
        if re.search(r"^\d+", remaining_text):
            return False
        return True
    # If ruleset only allows for player_no and no outcome (e.g. foul)
    if ruleset['outcome'] is False and ruleset['player_no']:
        # If there is remaining text and it is not a digit
        if not re.search(r"^\d+", remaining_text) and remaining_text!="":
            return False
        # If remaining text is blank or a number
        if remaining_text is not None or remaining_text=="" or re.search(r"^\d+", remaining_text):
            return True
    if ruleset['outcome'] is False and ruleset['player_no'] is False:
        if remaining_text is not None and remaining_text!="":
            return False
        return True
    # If none of the above is true return false
    return False

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
        # If full name is in possible_full_outcomes: append pairing to valid_shortcuts
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
    # If text is null return None
    if remaining_text is None:
        return None
    # Regex search to find a number if at end of string
    player_no = re.search(r"\d+$", remaining_text)
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
    # Used Chat GPT to help generate the below line
    event_name, remaining = get_event(event)

    # Get ruleset for event
    ruleset = get_event_rules(event_name)

    # Validate event input is valid. Returns None if not
    if validate_event(event_name, remaining, ruleset) is False:
        return None

    # Get outcome code
    outcome_name, remaining = get_outcome(event_name, remaining)

    # Get player no
    player_no = get_player_no(remaining)

    # Final check that outcome_name is not null (except for time and foul events)
    if ruleset['outcome'] and outcome_name is None:
        return None
    # Create list to store event
    output_event = [event_name, outcome_name, player_no]
    # Return event to caller
    return output_event

def input_event():
    '''Takes event input from user
    Removes all leading and trailing whitespace and lowercases it
    '''
    e = input("Enter match event: ")
    # Get event code and format it to remove all whitespace and make lowercase
    e = e.strip().lower().replace(" ", "")
    return e
