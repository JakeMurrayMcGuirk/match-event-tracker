team1 = input("Enter team 1 name: ")
team2 = input("Enter team 2 name: ")

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

outcomes = {
    'shot' : ['scored', 'wide'],
    'kickout' : ['won', 'lost'],
    'tackle' : ['successful', 'incomplete'],
    'pass' : ['complete', 'incomplete']
}

match_events=[]