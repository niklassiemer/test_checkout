import unittest

whoami = "pr"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(whoami, 'pr')


if __name__ == '__main__':
    unittest.main()
