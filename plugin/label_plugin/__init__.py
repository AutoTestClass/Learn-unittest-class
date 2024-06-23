def label(*labels):
    """
    Test case classification label

    Usage:
        class MyTest(unittest.TestCase):

            @label('quick')
            def test_foo(self):
                pass
    """

    def inner(cls):
        # append labels to class
        cls._labels = set(labels) | getattr(cls, '_labels', set())
        return cls

    return inner
