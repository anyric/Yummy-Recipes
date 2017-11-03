"""module to test user.py"""
import unittest
from user import User

class UserTestCase(unittest.TestCase):
    """Tests for user.py"""
    def setUp(self):
        self.user = User("Anyama", "cooldad", "co1da@")

    def test_isuser_add(self):
        """determines if a user is added successfully"""
        self.assertIsInstance(self.user, User, "adding user failed")

if __name__ == '__main__':
    unittest.main()
