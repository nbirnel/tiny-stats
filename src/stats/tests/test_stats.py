import pytest

from string import ascii_letters
from hypothesis import given
from hypothesis import strategies as st

from stats import stats

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

@given(integer=st.integers(min_value=0))
def test_positive_int_from_str_there_and_back(integer):
    returned_int = stats.positive_int_from_str(str(integer))
    assert returned_int == integer

