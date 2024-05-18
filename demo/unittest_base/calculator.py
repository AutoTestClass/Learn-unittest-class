class Calculator:
    """
    计算器
    """

    def __init__(self, *args):
        self.args = args

    def add(self):
        """
        加法运算
        """
        return sum(self.args)
