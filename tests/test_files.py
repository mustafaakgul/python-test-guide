from tests.test_main import is_done
import os


class TestIsDone:

    def setup(self):
        self.tmp_file = "/tmp/test_file"

    def teardown(self):
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)

    def write_tmp_file(self, content):
        with open(self.tmp_file, "w") as _f:
            _f.write(content)

    def test_yes(self):
        self.write_tmp_file("yes")
        assert is_done(self.tmp_file) is True

    def test_no(self):
        self.write_tmp_file("no")
        assert is_done(self.tmp_file) is False

# class TestIsDone:
#
#     def setup(self):
#         self.tmp_file = "/tmp/test_file"
#
#     def teardown(self):
#         if os.path.exists(self.tmp_file):
#             os.remove(self.tmp_file)
#
#     def test_yes(self):
#         with open(self.tmp_file, "w") as _f:
#             _f.write("yes")
#         assert is_done(self.tmp_file) is True
#
#     def test_no(self):
#         with open(self.tmp_file, "w") as _f:
#             _f.write("no")
#         assert is_done(self.tmp_file) is False


# class TestIsDone:
#
#     def teardown(self):
#         if os.path.exists("/tmp/test_file"):
#             os.remove("/tmp/test_file")
#
#     def test_yes(self):
#         with open("/tmp/test_file", "w") as _f:
#             _f.write("yes")
#         assert is_done("/tmp/test_file") is True
#
#     def test_no(self):
#         with open("/tmp/test_file", "w") as _f:
#             _f.write("no")
#         assert is_done("/tmp/test_file") is False

# class TestIsDone:
#
#     def test_yes(self):
#         with open("/tmp/test_file", "w") as _f:
#             _f.write("yes")
#         assert is_done("/tmp/test_file") is True
#
#     def test_no(self):
#         with open("/tmp/test_file", "w") as _f:
#             _f.write("no")
#         assert is_done("/tmp/test_file") is False