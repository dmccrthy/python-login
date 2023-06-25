import json
    
class user: #Defines user object for account creation and login
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def saveinfo(self): #Method to update stored userlogin info upon change/creation
        userbase[self.email] = {"password":self.password}
        json.dump(userbase, open("./src/userbase.json", 'w+'))
    def checkdupe(self): #Method to check new accounts against existing ones to prevent email duplication
        for i in userbase.keys.lower():
            if self.email == i:
                return True
        return False

def CreateAcc():
    mail = input("Email: ")
    pas = input("Password: ")
    confpas = input("Confirm Password: ")
    if pas != confpas: #Check if passwords match
        print("Error: Passwords Don't Match")
        CreateAcc()
    else:
        new = user(mail, pas)
        isdupe = new.checkdupe()
        if isdupe == True:
            print("Error: Email Already in Use")
            CreateAcc()
        elif isdupe == False:
            print("Account Creation Successful")
            new.saveinfo()
            print(userbase)

def Main():
    CreateAcc()

try:
    userbase = json.load(open("./src/userbase.json"))
except FileNotFoundError:
    userbase = {"blank":"blank"}

Main()
