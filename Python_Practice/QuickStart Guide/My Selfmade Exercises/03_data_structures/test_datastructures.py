import pytest
from datastructures import fruits, largest_number, union_set, intersection_set, frequency, countries, my_list, nested_dict

def test_fruits_list():
    assert isinstance(fruits, list)
    assert "Fig" in fruits
    assert "Banana" not in fruits

def test_largest_number():
    assert largest_number == 40

def test_union_intersection_sets():
    assert 1 in union_set
    assert 3 in intersection_set

def test_character_frequencies():
    assert frequency['a'] == 3
    assert frequency['n'] == 2

def test_countries_capitals():
    assert countries['USA'] == 'Washington D.C.'

def test_reversed_list():
    assert my_list == [5, 4, 3, 2, 1]

def test_nested_dictionary_access():
    assert nested_dict['dict1']['key2'] == 2
