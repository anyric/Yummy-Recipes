""""module to create new recipe"""

class Recipe(object):
    """"class to manage recipes"""

    def __init__(self, category, name, description):
        self.category = category
        self.name = name
        self.description = description
        self.store = {}

    def addrecipe(self):
        """function to add new category"""
        if self.name.strip() and self.description.strip():
            self.store[self.name] = {"Category": self.category, "Name": self.name, "Description":self.description}
            return self.store
        return False

    @classmethod
    def getrecipe(cls, name, dict):
        """method to retrieve category list"""
        return_value = dict[name][name]
        if return_value:
            return return_value
        return False
    