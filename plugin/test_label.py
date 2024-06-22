import unittest

from label_plugin import label
from label_plugin.LabelTestRunner import LabelTestRunner


class LabelTest(unittest.TestCase):

    @label("base")
    def test_label_base(self):
        self.assertEqual(1 + 1, 2)

    @label("slow")
    def test_label_slow(self):
        self.assertEqual(1, 2)

    def test_no_label(self):
        self.assertEqual(2 + 3, 5)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests([
        LabelTest("test_label_base"),
        LabelTest("test_label_slow"),
        LabelTest("test_no_label"),
    ])
    runner = LabelTestRunner(
        whitelist=["base"],  # 设置白名单
        # blacklist=["slow"],  # 设置黑名单
    )
    runner.run(suit)
