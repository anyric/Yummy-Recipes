""""module to create new user account"""
from modeldb import ModelDB
class User():
    """class to register new user"""

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.store = {}

    def adduser(self):
        """function to add new users"""
        if self.name and self.username and self.password:
            if self.name.strip() and self.username.strip() and self.password.strip():
                self.store[self.name] = {"Username": self.username, "Password":self.password}
                ModelDB.ACCOUNTS[self.username] = self.store
                return self.store
            return "Empty Field"
        return "Invalid User"

    def verifyuser(self):
        """method to verify user login"""
        if self.username and self.password:
            if self.username.strip() and self.password.strip():
                if ModelDB.ACCOUNTS.get(self.username):
                    if ModelDB.ACCOUNTS[self.username].Password == self.password:
                        return "User Loged successful"
                    return "Invalid password"
                return "account not found"
            return "Empty field"
        return "Invalid input"
