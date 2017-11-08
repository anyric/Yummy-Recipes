"""module to test user.py"""
import unittest
from user import User

class UserTestCase(unittest.TestCase):
    """Tests for user.py"""
    def setUp(self):
        self.user = User("Anyama", "cooldad", "co1da@")

    def test_isuser(self):
        """determines if a user is created successfully"""
        self.assertIsInstance(self.user, User, "adding user failed")

    def test_adduser_true(self):
        """determines if a adduser returns dictionary of user details"""
        self.assertEqual(self.user.adduser(), {"cooldad":{"Name":'Anyama', "Password":'co1da@'}})

    def test_adduser_false(self):
        """determines if a adduser reutrns false"""
        user_false = User("", "", "")

        self.assertEqual(user_false.adduser(), False, "Invalid user details")

    def test_verifyuser_true(self):
        """verifies if user is in given dictionary"""
        dict = {"cooldad": {"cooldad":{"Name":'Anyama', "Password":'co1da@'}}}

        self.assertEqual(self.user.verifyuser("cooldad", "co1da@", dict), True)

    def test_verifyuser_false(self):
        """test if user is not in given dictionary"""
        dict = {"cooldad":{"Name":'Anyama', "Password":'co1da@'}}
        self.assertEqual(self.user.verifyuser("ric", "ric@1", dict), False)

if __name__ == '__main__':
    unittest.main()
