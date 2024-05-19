import unittest


class MyTest(unittest.TestCase):

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3 > 2, "当条件为真时跳过测试")
    def test_skip_if(self):
        print('test bbb')

    @unittest.skipUnless(3 > 2, "当条件为真时执行测试")
    def test_skip_unless(self):
        print('test ccc')

    @unittest.expectedFailure
    def test_expected_failure(self):
        print('test ddd')
        self.assertEqual(2, 3)


@unittest.skip("整个测试类跳过")
class MySkippedTestCase(unittest.TestCase):

    def test_not_run(self):
        print('test eee')


if __name__ == '__main__':
    unittest.main()
