""""module to create new user account"""
class User():
    """class to register new user"""

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.store = {}

    def adduser(self):
        """function to add new users"""
        if self.name.strip() and self.username.strip() and self.password.strip():
            self.store[self.username] = {"Name": self.name, "Password":self.password}
            
            return self.store
        return False

    def verifyuser(self, username, password, dict):
        """method to verify user login"""
        if username.strip() and password.strip():
            return_value = dict.get(username, {}).get(username,{}).get("Password")
            if return_value == password:
                return True
        return False
