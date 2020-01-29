from string import ascii_letters
from math import factorial
from functools import reduce
import operator

import pytest
from hypothesis import given
from hypothesis import strategies as st

from stats import stats

tiny=22        # see stats._permutations_reference
small=150      # small enough to not take a long time on combinatorics
medium=1029    # see stats._combinations_reference

positive_integers = st.integers(min_value=0)
counting_integers = st.integers(min_value=1)
tiny_integers = st.integers(min_value=0, max_value=tiny)
tiny_counting_integers = st.integers(min_value=1, max_value=tiny-1)
small_integers = st.integers(min_value=0, max_value=small)
small_counting_integers = st.integers(min_value=1, max_value=small-1)
medium_integers = st.integers(min_value=0, max_value=medium)
medium_counting_integers = st.integers(min_value=1, max_value=medium-1)
# Tuples of integers with one bigger than the other:
# (72, 1), (9999, 543), (6,5)
sorted_pairs = st.tuples(
    positive_integers, counting_integers
    ).map(lambda x: sorted(x, reverse=True))

tiny_sorted_pairs = st.tuples(
    tiny_integers, tiny_counting_integers
    ).map(lambda x: sorted(x, reverse=True))

small_sorted_pairs = st.tuples(
    small_integers, small_counting_integers
    ).map(lambda x: sorted(x, reverse=True))

medium_sorted_pairs = st.tuples(
    medium_integers, medium_counting_integers
    ).map(lambda x: sorted(x, reverse=True))

@given(text=st.text(alphabet=ascii_letters))
def test_num_from_str_text(text):
    with pytest.raises(Exception):
        stats.num_from_str(text)

@given(my_float=st.floats(allow_infinity=False, allow_nan=False))
def test_num_from_str_there_and_back_float(my_float):
    returned = stats.num_from_str(str(my_float))
    assert returned == my_float

@given(integer=st.integers())
def test_num_from_str_there_and_back_int(integer):
    returned = stats.num_from_str(str(integer))
    assert returned == integer



@given(negative=st.integers(max_value=-1))
def test_positive_int_from_str_negative(negative):
    with pytest.raises(Exception):
        stats.positive_int_from_str(str(negative))

@given(my_float=st.floats())
def test_positive_int_from_str_float(my_float):
    with pytest.raises(Exception):
        stats.positive_int_from_str(str(my_float))

@given(integer=positive_integers)
def test_positive_int_from_str_there_and_back(integer):
    returned_int = stats.positive_int_from_str(str(integer))
    assert returned_int == integer

@pytest.mark.slow
@given(integer=positive_integers)
def test_permutations_slow_factorial(integer):
    result = stats.permutations(integer)
    assert result == factorial(integer)

@pytest.mark.slow
@given(integer=positive_integers)
def test_permutations_slow_number_equal_choose(integer):
    result = stats.permutations(integer)
    result_choose = stats.permutations(integer, choose=integer)
    assert result == result_choose

@given(integer=tiny_integers)
def test_permutations_factorial(integer):
    result = stats.permutations(integer)
    assert result == factorial(integer)

@given(integer=tiny_integers)
def test_permutations_number_equal_choose(integer):
    result = stats.permutations(integer)
    result_choose = stats.permutations(integer, choose=integer)
    assert result == result_choose

@given(two_ints=small_sorted_pairs)
def test_permutations_there_and_back(two_ints):
    num = two_ints[0]
    choose = two_ints[1]

    result = stats.permutations(num, choose=choose)
    top_to_bottom = [result]
    top_to_bottom.extend(range(num, num - choose, -1))
    and_back = reduce(
        operator.truediv,
        top_to_bottom
        )

    assert round(and_back) == 1

@pytest.mark.slow
@given(two_ints=tiny_sorted_pairs)
def test_permutations_versus_reference_implementation(two_ints):
    num = two_ints[0]
    choose = two_ints[1]

    result = stats.permutations(num, choose=choose)
    reference = stats._permutations_reference(num, choose=choose)
    assert result == reference




@given(integer=positive_integers)
def test_combinations_choose_none(integer):
    assert stats.combinations(integer) == 1

@given(integer=positive_integers)
def test_combinations_choose_all(integer):
    assert stats.combinations(integer, choose=integer) == 1

@given(integer=positive_integers)
def test_combinations_choose_zero(integer):
    assert stats.combinations(integer, choose=0) == 1

@given(integer=positive_integers)
def test_combinations_choose_one(integer):
    assert stats.combinations(integer, choose=1) == integer

@given(two_ints=small_sorted_pairs)
def test_combinations_invert_n_m(two_ints):
    """
    nCm = nCn-m
    n!/(n-m)!m! = n!/m!(n-m)!
    """
    num = two_ints[0]
    choose = two_ints[1]

    n_choose_m = stats.combinations(num, choose=choose)
    n_choose_n_minus_m = stats.combinations(num, choose=num-choose)

    assert n_choose_m == n_choose_n_minus_m

@pytest.mark.slow
@given(two_ints=medium_sorted_pairs)
def test_combinations_versus_reference_implementation(two_ints):
    num = two_ints[0]
    choose = two_ints[1]

    result = stats.combinations(num, choose=choose)
    reference = stats._combinations_reference(num, choose=choose)
    assert result == reference
