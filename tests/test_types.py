import pytest


# We have a test that wants to check if an object has an attribute. For this test, we'll
# use the hasattr() built-in function from Python. It returns a boolean depending on the
# attribute of the object. Here’s a quick example of how that works:
"""
>>> hasattr(dict(), "keys")
True
>>> hasattr("string", "append")
False
"""
"""
The parametrize decorator still uses a single string for the first argument but with two words. These two words within the string, are now separated by a comma. Each comma-separated word becomes an argument to the function. In this case, it’s item and attribute.

Next, the list of items to pass is a list of two items. Each of these pairs represents an item and an attribute to test for.

When Pytest can't build a string representation of the objects being passed in, it will create one. You can see this in action when running the test:

$ pytest -v
"""
@pytest.mark.parametrize("item, attribute", [("", "format"), (list(), "append")])
def test_attributes(item, attribute):
    assert hasattr(item, attribute)


# Use parametrize
# Behind the scenes, Pytest will consider each item in that list as a separate test.
# That means that all passing and failing tests will get reported separately.
# Let's see what happens when running the test with pytest:
# that means that all passing and failing tests will get reported separately like below in
# old method in python test [1] not like [2]
"""
There are a few notable items in the test reporting. First, we see that from a single test 
Pytest is reporting five tests in total: three passing and two failing. The failures are 
reported separately, including what the failing input is. For example, the string "No" is 
reported in three places: one in the title of the failure section, then the assertion error, 
and finally in the failure line towards the end:
"""
"""
And running the tests produces minimal output: pytest
But increasing the verbosity can include the values that Pytest sees for each test when parametrizing:
pytest -v test_types.py
"""
@pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])  # Using decorator
def test_string_is_digit(item):
    assert item.isdigit()

# A group of tests that make the same assertion are also a good candidate for parametrize.
# If the previous test was rewritten with one test for each item, it would allow for better
# failure reporting, but it would be repetitive:
"""
These tests are better in the sense that a failure can be easily associated with a single input, and although it might seem out of the ordinary to have several similar tests, it’s actually common to see in production test suites that try to be granular.
Although the tests would be better because they can report exactly what fails (or passes) they also come with the following issues:
Code is very repetitive, which creates unnecessary maintenance burden
There’s potential for typos and mistakes when updates need to happen to all these tests
Because they’re repetitive, engineers might avoid all use cases and inputs
"""
# [1]
def test_is_digit_1():
    assert "1".isdigit()

def test_is_digit_10():
    assert "10".isdigit()

def test_is_digit_33():
    assert "33".isdigit()

# [2]
# def test_string_is_digit():
#     items = ["1", "10", "33"] # items = ["No", "1", "10", "33", "Yes"]
#     for item in items:
#         assert item.isdigit()