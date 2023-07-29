import os


# Let's use a real-world scenario to see how test classes can help. The following function checks if a
# given file has a content of "yes" to return True. If the file doesn't exist or if it contains a "no",
# it returns False. This scenario is common in asynchronous tasks that use the filesystem to indicate completion.
def is_done(path):
    if not os.path.exists(path):
        return False
    with open(path) as _f:
        contents = _f.read()
    if "yes" in contents.lower():
        return True
    elif "no" in contents.lower():
        return False


def test_main():
    #assert "a string value" == "a string value"
    assert True