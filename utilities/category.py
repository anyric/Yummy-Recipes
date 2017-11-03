""""module to create new category"""
from modeldb import ModelDB
class Category(object):
    """"class to manage recipe categories"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.store = {}

    def addcategory(self):
        """function to add new category"""
        if self.name and self.description:
            if self.name.strip() and self.description.strip():
                self.store[self.name] = self.description
                ModelDB.CATDATA[self.name] = self.store
                return "Category added successful"
            return "Empty Field"
        return "Invalid Category"
    @classmethod
    def getcategory(cls):
        """method to retrieve category list"""
        if ModelDB.CATDATA:
            return ModelDB.CATDATA
        return "No category added"
    