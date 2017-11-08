""""module to create new recipe"""

class Recipe(object):
    """"class to manage recipes"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.store = {}

    
    def addrecipe(self):
        """function to add new category"""
        if self.name.strip() and self.description.strip():
            self.store[self.name] = {"Name": self.name, "Description":self.description}
            return self.store
        return False

    @classmethod
    def getrecipe(cls,name, dict):
        """method to retrieve category list"""
        return_value = dict.get(name, {}).get(name,{}).get("Name")
        if return_value == name:
            return True
        return False
    