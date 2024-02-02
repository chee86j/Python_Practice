import pytest
from controlflow import *

def test_positive_check():
    assert number > 0  # Check if the number is positive

def test_for_loop_numbers():
    expected = list(range(1, 11))
    assert all(i in expected for i in range(1, 11))  # Check if the loop iterates correctly

def test_while_loop_iterations():
    assert counter == 5  # Check if the while loop iterates exactly 5 times

def test_odd_even_check():
    assert number % 2 == 0  # Check if the number is even
    
def test_3x3_grid_output():
    expected_format = "(1,1) (1,2) (1,3) \n(2,1) (2,2) (2,3) \n(3,1) (3,2) (3,3) \n"
    assert create_3x3_grid() == expected_format


def test_list_comprehension_squares():
    assert squares == [1, 4, 9, 16, 25]  # Check if the list comprehension is correct

def test_for_loop_with_range(capsys):
    for i in range(5):
        print(f"Number {i}")
    captured = capsys.readouterr()
    for i in range(5):
        assert f"Number {i}" in captured.out

def test_for_loop_with_else(capsys):
    for i in range(3):
        print(i)
    else:
        print("Loop completed")
    captured = capsys.readouterr()
    assert "Loop completed" in captured.out