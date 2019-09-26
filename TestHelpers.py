import unittest

from Helpers import *


class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.helpers = Helpers()

    def tearDown(self):
        self.helpers = None

    def test_invalid_user_input(self):
        user_input = 'A'
        self.assertEqual(self.helpers.validate_user_input(user_input, ['1', '2', '3']), None)

    def test_valid_user_input(self):
        user_input = 'C'
        self.assertEqual(self.helpers.validate_user_input(user_input, ['A', 'B', 'C']), 'C')


if __name__ == '__main__':
    unittest.main()
