import pytest
import os

# The tmpfile() fixture uses Pytest's tmpdir() fixture, which guarantees a valid temporary file that
# gets cleaned after tests are done.
# A custom Pytest fixture that uses the tmpdir() fixture to create a temporary done file with some contents.
@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath
    return write

# Update the TestFile class so that it uses the fixture instead of the helper methods:
# A test class that uses the custom tmpfile() fixture to create the file.
class TestFile:

    def test_f(self, tmpfile):
        path = tmpfile()
        with open(path) as _f:
            contents = _f.read()
        assert contents == "1"

# Add a new class-based test to the test_advanced.py file. This test should use a setup()
# and teardown() function that creates a temporary file with some text on it. After each
# test, the file gets removed. It should look like this:
# class TestFile:
#
#     def setup(self):
#         with open("/tmp/done", 'w') as _f:
#             _f.write("1")
#
#     def teardown(self):
#         try:
#             os.remove("/tmp/done")
#         except OSError:
#             pass
#
#     def test_done_file(self):
#         with open("/tmp/done") as _f:
#             contents = _f.read()
#         assert contents == "1"

# pytest -v test_advanced.py
# Two parametrized tests for the str_to_bool() function, one that tests the true values and the
# other one that test the false values.
@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True

@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False

# A str_to_bool() function that accepts a string and returns a boolean
# value depending on the contents of the string.
def str_to_bool(string):
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False