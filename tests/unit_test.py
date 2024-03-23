"""
Naming conventions
The class and method names are following a test convention. The convention is that they need to be prefixed
with test. Although it isn't required, test classes use camel-casing, and test methods are lower-case, and words
are separate with an underscore. For example, the following is how a test for customer accounts that verify
creation and deletion could look:
"""
"""
Python data structures like dictionaries and lists evaluate as true when they have at least one item in them and false 
when they are empty. Avoid evaluating data structures in this way with assertTrue() and assertFalse() to prevent 
unexpected items go undetected. It is preferable to be as accurate as possible when testing.
"""
import unittest


# class TestAccounts(unittest.TestCase):
#
#     def test_creation(self):
#         self.assertTrue(account.create())
#
#     def test_deletion(self):
#         self.assertTrue(account.delete())


class TestAssertions(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_equals(self):
        self.assertEqual("one string", "one string")

    def test_not_equals(self):
        self.assertNotEqual("one string", "another string")


# By running run this file, or python test_assertions.py, or click green buttons, or python -m unittest
if __name__ == "__main__":
    unittest.main()