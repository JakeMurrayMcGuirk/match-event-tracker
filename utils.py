# File that contains all lists and dictionaries for events, event shortcuts and their possible outcomes (and respective shortcuts)

commands = {
    'help' : 'To enter an event please follow the following format: event outcome (if applicable) player no.(if applicable)\nIf outcome or number are not available then skip E.g. foul on player 14 = f14',
    #'delete' : 'Deletes the most recently recorded event.'
}

events = [
    'start game',
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
    'sg' : 'start game',
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