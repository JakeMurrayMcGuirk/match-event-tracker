import pytest
from stats_tagger import parse_event

# Test
test_inputs = ["s22", "sw15", "tisu4", "ko22won", "ss23", "sw15", "se", "ss", "kos", "kow", "kowon", "kolost", "kol", "kog", "f16", "fg15", "f"]
expected_output = [
    ['shot', None, "22"],
    ['shot', 'wide', '15'],
    ['tackle', None, '4'],
    ['kickout', None, None],
    ['shot', 'saved' ,'23'],
    ['shot', 'wide', '15'],
    ['shot', None, None],
    ['shot', 'saved', None],
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
def test_input():
    for input, index in enumerate(test_inputs):
        assert parse_event(input) == expected_output[index]