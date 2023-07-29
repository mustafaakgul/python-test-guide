import pytest


"""
It isn't common to have tests within the same file as actual code. For simplicity, the examples in
this exercise will have actual code in the same file. In real-world Python projects you'll find
that tests are separated by files and directories from the code it's testing.
"""

# An admin_command() function that accepts an argument, and a keyword argument.
def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects
    `command` to be a list.
    """
    # if sudo:
    #     return ["sudo"] + command
    # return command
    # return ["sudo"] + command if sudo else command

    # A TypeError exception with a helpful error message in the admin_command() function.
    if not isinstance(command, list):
        raise TypeError(f"was expecting command to be a list, but got a {type(command)}")
    return ["sudo"] + command if sudo else command


# A TestAdminCommand() test class that has a command() helper method and three test methods
# that check the admin_command() function.
class TestAdminCommand:

    # Now append a new test to the class to check on the exception. This test should expect a TypeError from
    # the function when a non-list value is passed to the function:
    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True)
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"

    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected