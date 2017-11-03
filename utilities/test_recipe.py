"""module to test recipe.py"""
import unittest
from recipe import Recipe

class UserTestCase(unittest.TestCase):
    """Tests for recipe.py"""
    def setUp(self):
        self.recipe = Recipe("Gobe", "This is a source made from leaves of peas")

    def test_iscategroy_add(self):
        """determines if a recipe is added successfully"""
        self.assertIsInstance(self.recipe, Recipe, "adding recipe failed")

if __name__ == '__main__':
    unittest.main()
