import json

class user: #Defines user object for account creation and login
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def saveinfo(self): #Method to update stored userlogin info upon change/creation
        userbase[self.email] = {"password":self.password}
        json.dump(userbase, open("./src/userbase.json", 'w+'))
    def checkdupe(self): #Method to check new accounts against existing ones to prevent email duplication
        for i in userbase.keys():
            if self.email == i:
                return True
        return False

def createacc(mail, pas, confpas):
    if pas != confpas: #Check if passwords match
        return 1
    else:
        new = user(mail, pas)
        isdupe = new.checkdupe()
        if isdupe == True:
            return 2
        elif isdupe == False:
            new.saveinfo()
            return 0   #Success
        
def login(mail, pas):
    try:
        if pas == userbase[mail]["password"]: #Check password against email password
            return 0 #Success
        elif pas != userbase[mail]["password"]: #If password doesn't match account
            return 1 #Failure
    except KeyError: #If email isn't associated with account
        return 2 #Failure

try:
    userbase = json.load(open("./src/userbase.json"))
except FileNotFoundError:
    userbase = {"blank":"blank"}
