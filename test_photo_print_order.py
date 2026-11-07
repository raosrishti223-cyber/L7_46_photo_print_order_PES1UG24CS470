from hypothesis import given, strategies as st
from photo_print_order import (
    parse_order,
    file_size_average,
    payable_amount
)


# Test 1: parse_order
@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    parse_order(s)


# Test 2: file_size_average
@given(st.text() | st.none())
def test_file_size_average_no_crash(s):
    file_size_average(s)


# Test 3: payable_amount
@given(st.text() | st.none())
def test_payable_amount_no_crash(s):
    payable_amount(s)