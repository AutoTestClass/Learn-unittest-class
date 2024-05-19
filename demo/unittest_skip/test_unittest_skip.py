import sys
import unittest

__version__ = 0


def element_is_exists() -> bool:
    """
    element is exists
    :return: 
    """
    return False


class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(__version__ < 3, "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if element_is_exists():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
