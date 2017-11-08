"""module to test recipe.py"""
import unittest
from recipe import Recipe

class UserTestCase(unittest.TestCase):
    """Tests for recipe.py"""
    def setUp(self):
        self.recipe = Recipe("Gobe", "This is a source made from leaves of peas")

    def test_isrecipe(self):
        """determines if a recipe is added successfully"""
        self.assertIsInstance(self.recipe, Recipe, "adding recipe failed")

    def test_addrecipe_true(self):
        """determines if addrecipe returns dictionary of recipe details"""
        dict = {"Gobe":{"Name":'Gobe', "Description":'This is a source made from leaves of peas'}}
        self.assertEqual(self.recipe.addrecipe(), dict)

    def test_addrecipe_false(self):
        """determines if a adduser reutrns false"""
        recipe_false = Recipe("", "")
        self.assertEqual(recipe_false.addrecipe(), False, "Invalid recipe details")

    
    def test_getrecipe_true(self):
        """verifies if a recipe is in given dictionary"""
        dict = {"Gobe":{"Gobe":{"Name":'Gobe',"Description":'This is a source made from leaves of peas'}}}
        self.assertEqual(self.recipe.getrecipe("Gobe", dict), True)

    def test_getrecipe_false(self):
        """test if recipe is not in given dictionary"""
        dict = {"Gobe":{"Gobe":{"Name":'Gobe', "Description":'This is a source made from leaves of peas'}}}
        self.assertEqual(self.recipe.getrecipe("Meat", dict), False)


if __name__ == '__main__':
    unittest.main()
