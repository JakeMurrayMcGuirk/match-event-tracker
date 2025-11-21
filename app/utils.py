'''Contains all lists and dictionaries for events, event shortcuts, possible outcomes and outcome shortcuts'''

def show_help():
    '''Displays format to enter events'''
    help = 'To enter an event please follow the following format:' \
    ' event outcome (if applicable) player no.(if applicable)' \
    '\nE.g. foul by player 14 = f14\n\'delete\' removes the most recently input event'
    return help


def delete_event(match_events):
    '''Deletes a specified event from the user'''
    if match_events:
        match_events.pop()
        #print("Event deleted")
        return match_events
    #print("No events to delete")
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
