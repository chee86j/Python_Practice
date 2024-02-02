import pytest
from variablesanddatatypes import *

def test_data_types():
    assert type(int_var) is int
    assert type(str_var) is str
    assert type(float_var) is float

def test_swap_values():
    assert a == 10
    assert b == 5

def test_type_conversion():
    assert int(str_num) == 8
    assert str(int_num) == "8"

def test_list_of_hobbies():
    assert isinstance(hobbies, list)

def test_average_of_numbers():
    assert average == sum(numbers) / len(numbers)

def test_dictionary_of_book():
    assert isinstance(book, dict)
    assert book["title"] == "1984"

def test_string_concatenation():
    assert sentence == "Hello World"

def test_variable_types():
    assert isinstance(int_var, int)
    assert isinstance(str_var, str)
    assert isinstance(float_var, float)

def test_check_data_type():
    assert isinstance(var, str)
