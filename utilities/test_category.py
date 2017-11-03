"""module to test category.py"""
import unittest
from category import Category

class UserTestCase(unittest.TestCase):
    """Tests for category.py"""
    def setUp(self):
        self.category = Category("Greens", "These are vegetables grown locally from\
         which you get vitamins")

    def test_iscategroy_add(self):
        """determines if a category is added successfully"""
        self.assertIsInstance(self.category, Category, "adding category failed")

if __name__ == '__main__':
    unittest.main()
