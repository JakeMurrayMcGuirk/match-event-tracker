'''Tests for the functions in stats_tagger.py'''

# Import functions to be tested from stats_tagger.py
from app.stats_tagger import parse_event, get_event, get_event_rules, validate_event, get_outcome, get_player_no
from app.utils import delete_event, show_help

# Test input values for test_parse_input
test_inputs = ["s22", "sw15", "tisu4",
               "ko22won", "ss23", "sw15",
               "se", "ss", "kos",
               "kow", "kowon", "kolost",
               "kol", "kog", "f16",
               "fg15", "f"]

# Expected output values for test_parse_input
expected_output = [
    ['shot', None, "22"],
    ['shot', 'wide', '15'],
    ['tackle', 'incomplete', '4'],
    ['kickout', None, None],
    ['shot', None ,'23'],
    ['shot', 'wide', '15'],
    ['shot', None, None],
    ['shot', None, None],
    ['kickout', None, None],
    ['kickout', None, None],
    ['kickout', 'won', None],
    ['kickout', 'lost', None],
    ['kickout', None, None],
    ['kickout', None, None],
    ['foul', None, '16'],
    ['foul', None, '15'],
    ['foul', None, None]
]


def test_parse_input():
    '''Tests the parse_event function in stats_tagger.py'''
    for index, i in enumerate(test_inputs):
        assert parse_event(i) == expected_output[index]


def test_get_event():
    '''Tests the get_event function in stats_tagger.py'''
    # Chat GPT used to find errors with changing lists to tuples
    assert get_event("sg69696969") == ("shot", "g69696969")
    assert get_event("f14") == ("foul", "14")
    assert get_event("sw5") == ("shot", "w5")
    assert get_event("pofr65") == ("pass", "ofr65")
    assert get_event("zk69") == (None, "zk69")

def test_get_event_rules():
    '''Tests that the get_event_rules function is retrieving the correct rulesets'''
    assert get_event_rules("shot", "g69696969") == {'outcome': True, 'player_no':True}
    assert get_event_rules("foul", "14") == {'outcome':False, 'player_no':True}
    assert get_event_rules("shot", "w5") == {'outcome': True, 'player_no':True}
    assert get_event_rules("pass", "ofr65") == {'outcome':True, 'player_no':True}
    assert get_event_rules(None, "zk69") == None

def test_validate_event():
    assert validate_event("shot", "g696969", {'outcome': True, 'player_no':True}) == True
    assert validate_event("foul", "14", {'outcome':False, 'player_no':True}) == True
    assert validate_event("shot", "w5", {'outcome': True, 'player_no':True}) == True
    assert validate_event("pass", "ofr65", {'outcome':True, 'player_no':True}) == True
    assert validate_event(None, "zk69", None) == False

def test_get_outcome():
    '''Tests the get_outcome function in stats_tagger.py'''
    assert get_outcome("shot", "g69696969") == ("goal", "69696969")
    assert get_outcome("foul", "14") == (None, "14")
    assert get_outcome("shot", "w5") == ("wide", "5")
    assert get_outcome("pass", "ofr65") == (None, "ofr65")
    assert get_outcome(None, "zk69") == (None, "zk69")

def test_get_player_no():
    '''Tests the get_player_no function in stats_tagger.py'''
    assert get_player_no("69696969") == "69696969"
    assert get_player_no("14") == "14"
    assert get_player_no("5") == "5"
    assert get_player_no("ofr65") == "65"
    assert get_player_no("zk69") == "69"

def test_delete_event():
    '''Tests that delete_event is working correctly'''
    assert delete_event([]) == 0
    assert delete_event([["start game", None, None], ["shot", "goal", "15"], ["pass", "complete", None]]) == [["start game", None, None], ["shot", "goal", "15"]]

def test_show_help():
    '''Ensures the show_help function is functioning correctly'''
    assert show_help() == 'To enter an event please follow the following format: event outcome (if applicable) player no.(if applicable)\nE.g. foul by player 14 = f14\n\'delete\' removes the most recently input event'
