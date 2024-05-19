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


#
class ExampleClass:
    """
    示例类，包含一些属性
    """

    def __init__(self):
        self.some_attribute = 'value'


class MyTestCase(unittest.TestCase):

    @skipUnlessHasattr(ExampleClass(), 'some_attribute')
    def test_with_attribute(self):
        self.assertTrue(True)

    @skipUnlessHasattr(ExampleClass(), 'missing_attribute')
    def test_without_attribute(self):
        self.assertTrue(True)


# 运行测试
if __name__ == '__main__':
    unittest.main()
