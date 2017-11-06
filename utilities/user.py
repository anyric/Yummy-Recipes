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
                return "User added successfully"
            return "Empty Field"
        return "Invalid User"

    def verifyuser(self, username, password):
        """method to verify user login"""
        if username and password:
            if username.strip() and password.strip():
                if ModelDB.ACCOUNTS.get(username):
                    if ModelDB.ACCOUNTS[username].Password == password:
                        return "User Loged successful"
                    return "Invalid password"
                return "account not found"
            return "Empty field"
        return "Invalid input"
