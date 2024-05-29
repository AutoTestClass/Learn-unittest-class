import unittest


def skipUnlessHasattr(obj, attr):
    """
    自定义 skipUnlessHasattr 装饰器
    :param obj:
    :param attr:
    :return:
    """
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


def skipTestBaseLogin(username, password):
    # 登录的逻辑
    is_login = False
    if username == "admin" and password == "admin123":
        is_login = True

    if is_login:
        return lambda func: func

    return unittest.skip("登录失败")


class ExampleClass:
    """
    示例类，包含一些属性
    """

    def __init__(self):
        self.some_attribute = 'value'


ec = ExampleClass()


class MyTestCase(unittest.TestCase):

    @skipTestBaseLogin("admin", "admin456")
    def test_login_after(self):
        print("登录之后")

    @skipUnlessHasattr(ec, 'some_attribute')
    def test_with_attribute(self):
        self.assertTrue(True)

    @skipUnlessHasattr(ec, 'missing_attribute')
    def test_without_attribute(self):
        self.assertTrue(True)


# 运行测试
if __name__ == '__main__':
    unittest.main()
