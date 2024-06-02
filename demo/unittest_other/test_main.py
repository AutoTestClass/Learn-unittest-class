import unittest


class TestLogin(unittest.TestCase):

    def test_login_fail(self):
        ...

    def test_login_success(self):
        ...


class TestRegister(unittest.TestCase):

    def test_register_fail(self):
        self.assertEqual(1, 3)

    def test_register_success(self):
        ...


if __name__ == '__main__':
    unittest.main(
        failfast=True,
        testRunner=unittest.TextTestRunner,
        module="test_example",
        verbosity=2,
        buffer=True
    )
