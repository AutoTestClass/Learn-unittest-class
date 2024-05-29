import unittest


class Test(unittest.TestCase):

    def user_login(self):
        # 1. 输入用户名
        # 2. 输入密码
        # 3. 点击 登录
        print("执行登录的动作")

    def setUp(self) -> None:
        self.user_login()
        print("before")

    def test_case_send_mail(self):
        # 写邮件 _> 发送
        print("写邮件 _> 发送")

    def test_case_del_mail(self):
        # 查看邮件 _> 删除
        print("查看邮件 _> 删除")

    def test_case_read_mail(self):
        # 打开邮件 _> 查看
        print("打开邮件 _> 查看")

    def tearDown(self) -> None:
        print("after")


if __name__ == '__main__':
    unittest.main()
