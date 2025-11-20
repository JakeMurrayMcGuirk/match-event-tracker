'''Contains all lists and dictionaries for events, event shortcuts, possible outcomes and outcome shortcuts'''

def show_help():
    '''Displays format to enter events'''
    print('To enter an event please follow the following format: event outcome (if applicable) player no.(if applicable)\nE.g. foul by player 14 = f14\n\'delete\' removes the most recently input event')

def delete_event(match_events):
    '''Deletes a specified event from the user'''
    if match_events:
        match_events = match_events[:-1]
    return match_events

commands = {
    'help' : show_help(),
    'delete' : delete_event()
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
