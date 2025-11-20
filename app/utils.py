'''Contains all lists and dictionaries for events, event shortcuts, possible outcomes and outcome shortcuts'''

def show_help():
    '''Displays format to enter events'''
    help = 'To enter an event please follow the following format: event outcome (if applicable) player no.(if applicable)\nE.g. foul by player 14 = f14\n\'delete\' removes the most recently input event'
    return help


def delete_event(match_events):
    '''Deletes a specified event from the user'''
    if match_events:
        match_events = match_events[:-1]
        return match_events
    return 0

commands = {
    'help' : show_help,
    'delete' : delete_event
}

events = [
    'begin game',
    'end half',
    'start half',
    'end game',
    'shot',
    'kickout',
    'tackle',
    'pass',
    'foul'
]

event_shortcuts = {
    'bg' : 'begin game',
    'eh' : 'end half',
    'sh' : 'start half',
    'eg' : 'end game',
    's' : 'shot',
    'ko' : 'kickout',
    't' : 'tackle',
    'p' : 'pass',
    'f' : 'foul'
}

event_categories = {
    'time' : ['begin game', 'end half', 'start half', 'end game'],
    'play' : ['shot', 'kickout', 'tackle', 'pass'],
    'foul' :  ['foul']
}

possible_params = {
    'time' : 0,
    'begin game' : 0,
    'end half' : 0,
    'start half' : 0,
    'end game' : 0,
    'shot' : 3,
    'kickout' : 3,
    'tackle' : 2,
    'pass' : 2,
    'foul' : 1
}

param_rules = {
    # Default ruleset
    'play' : {
        'outcome' : True,
        'player_no' : True
    },
    # Category rule for events in the time category
    'time' : {
        'outcome' : False,
        'player_no' : False
    },
    # Rule for fouls
    'foul' : {
        'outcome' : False,
        'player_no' : True
    },
    # Handle null vals
    None : None
}

outcomes = {
    'shot' : ['goal', 'point', '2 points', 'wide'],
    'kickout' : ['won', 'lost'],
    'tackle' : ['successful', 'incomplete'],
    'pass' : ['complete', 'incomplete']
}

outcome_shortcuts = {
    'g' : 'goal',
    'p' : 'point',
    '2p' : '2 points',
    'w' : 'wide',
    'c' : 'complete',
    'i' : 'incomplete',
    'won' : 'won',
    'lost' : 'lost',
}
