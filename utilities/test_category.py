"""module to test category.py"""
import unittest
from category import Category

class UserTestCase(unittest.TestCase):
    """Tests for category.py"""
    def setUp(self):
        self.category = Category("Greens", "These are vegetables grown locally from which you get vitamins")

    def test_iscategroy(self):
        """determines if a category is added successfully"""
        dict = {"Name": 'Greens', "Description":'These are vegetables grown locally from which you get vitamins'}
        self.assertIsInstance(self.category, Category, "adding category failed")

    def test_addcategroy_true(self):
        """determines if a addcategory returns dictionary of categroy details"""
        dict = {"Greens":{"Name":'Greens', "Description":'These are vegetables grown locally from which you get vitamins'}}
        self.assertEqual(self.category.addcategory(), dict)

    def test_addcategory_false(self):
        """determines if a adduser reutrns false"""
        category_false = Category("", "")
        self.assertEqual(category_false.addcategory(), False, "Invalid category details")

    
    def test_getcategory_true(self):
        """verifies if user is in given dictionary"""
        dict = {"Greens":{"Greens":{"Name":'Greens', "Description":'These are vegetables grown locally from which you get vitamins'}}}
        self.assertEqual(self.category.getcategory("Greens", dict), True)

    def test_getcategory_false(self):
        """test if user is not in given dictionary"""
        dict = {"Greens":{"Name":'Greens', "Description":'These are vegetables grown locally from which you get vitamins'}}
        self.assertEqual(self.category.getcategory("Meat", dict), False)


if __name__ == '__main__':
    unittest.main()
