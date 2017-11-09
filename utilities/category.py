""""module to create new category"""
class Category(object):
    """"class to manage recipe categories"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.store = {}

    def addcategory(self):
        """function to add new category"""
        if self.name.strip() and self.description.strip():
            self.store[self.name] = {"Name": self.name, "Description":self.description}
            return self.store
        return False

    @classmethod
    def getcategory(cls, name, dict):
        """method to retrieve category list"""
        return_value = dict[name][name]
        if return_value:
            return return_value
        return False
