# Import dependencies
import pytest
# Import functions to be tested from stats_tagger.py
from stats_tagger import parse_event, get_event, get_outcome, get_player_no

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

# Function to test the parse_event function
def test_parse_input():
    for index, input in enumerate(test_inputs):
        assert parse_event(input) == expected_output[index]

# Tests the get_event function in stats_tagger.py
def test_get_event():
    assert get_event("sg69696969") == ("sg", "start game", "69696969") # Chat GPT used to find errors with changing lists to tuples
    assert get_event("f14") == ("f", "foul", "14")
    assert get_event("sw5") == ("s", "shot", "w5")
    assert get_event("pofr65") == (None, None, "pofr65")

def test_get_outcome():
    assert get_outcome("69696969") == (None, "69696969")
    assert get_outcome("14") == (None, "14")
    assert get_outcome("w5") == ("wide", "5")
    assert get_outcome("pofr65") == (None, "pofr65")

def test_get_player_no():
    assert get_player_no("69696969") == "69696969"
    assert get_outcome("14") == "14"
    assert get_outcome("5") == "5"
    assert get_outcome("pofr65") == "65"

test_parse_input()
test_get_event()
test_get_outcome
test_get_player_no
