import unittest


def user_login_no_fail() -> bool:
    # ....
    return True  # 真失败


def user_login() -> bool:
    # ....
    return False  # 成功


class Config:
    IS_LOGIN_SUCCESS = False


class MyTest(unittest.TestCase):

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(user_login_no_fail() is False, "登录没有失败")
    def test_skip_if(self):
        print('登录失败之后，注册账号')

    def test_aa_login(self):
        # 测试执行登录
        print("执行登录")
        Config.IS_LOGIN_SUCCESS = True
        print(Config.IS_LOGIN_SUCCESS)

    @unittest.skipUnless(user_login() is True, "当条件为真时执行测试")
    def test_zz_skip_unless(self):
        print('登录之后，执行', Config.IS_LOGIN_SUCCESS)

    @unittest.expectedFailure  # 失败是在预期之内，所以，失败了不会抛错误
    def test_expected_failure(self):
        print('test ddd')
        self.assertEqual(2, 3)


@unittest.skip("整个测试类跳过")
class MySkippedTestCase(unittest.TestCase):

    def test_not_run(self):
        print('test eee')


if __name__ == '__main__':
    unittest.main()
