""""module to create new recipe"""
from modeldb import ModelDB
class Recipe(object):
    """"class to manage recipes"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.store = {}

    def addrecipe(self):
        """function to add new recipe"""
        if self.name and self.description:
            if self.name.strip() and self.description.strip():
                self.store[self.name] = self.description
                ModelDB.RECDATA[self.name] = self.store
                return "Recipe added successful"
            return "Empty Field"
        return "Invalid Recipe"
    @classmethod
    def getrecipe(cls):
        """method to retrieve recipe list"""
        if ModelDB.RECDATA:
            return ModelDB.RECDATA
        return "No recipe added"
    