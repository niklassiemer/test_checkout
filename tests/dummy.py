import unittest

whoami = "pr"
new_line = "new!"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(whoami, 'master')


if __name__ == '__main__':
    unittest.main()
