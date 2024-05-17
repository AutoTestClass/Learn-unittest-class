"""
seldom testing
"""
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    seldom.main()
