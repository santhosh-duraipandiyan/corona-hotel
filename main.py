#Corona alert automation system...

#Created by odd0introvrt using python...

#Idea by sivabalan...


#Importing needed stuffs and other pages...

from add import addData

from view import viewData

from alert import alert

from getpass import getpass

import json

#Getting user data from json file...

with open('users.json') as json_file: 

    users = json.load(json_file)

status = ""

user = {}

#Menu...

def displayMenu():

	print("\n##########################################\n")
	print("####### HOTEL CORONA ALERT SYSTEM ########\n")
	print("##########################################")

	print("\n\n> Press Y is you already have an account.\n> Press N if you donnt have an account.\n> Press Q to quit.\n\n")
	
	status = input("Your choice: ")

	if status == "y" or status == "Y":

		oldUser()
	
	elif status == "n" or status == "N":

		newUser()

	elif status == "q" or status == "Q":

		exit()

#Adding new user...

def newUser():
	
	createLogin = input("\nEnter the username: ")

	if createLogin in users:

		print("\n User already exist!\n")

	else:

		createPass = getpass("\nEnter the password: ")

		user[createLogin] = createPass

		print("\nUser created successfully! Now login!\n")

		file = open("users.json", "r+")
		
		data = json.load(file)

		data.update(user)

		file.seek(0)

		json.dump(data, file)
		
		file.close()

#Login with existing user...

def oldUser():
	
	name = input("\nEnter username: ")

	passw = getpass("\nEnter the password: ")

	if name in users and users[name] == passw:
		
		print("\nLogin successful!")

		loggedIn("1")

	else:

		print("\nIncorrect username or password!\n")


#Home page...

def loggedIn(login):

	print("\n\n> Press 1 for add data.\n> Press 2 for view data.\n> Press 3 to alert users.\n> Press 4 to logout.\n\n")
	
	module = input("Your choice: ")

	if module == "1":

		addData()

		if login == "1":
		
			loggedIn("1")

		else:

			return

	elif module == "2":

		viewData()

		if login == "1":
		
			loggedIn("1")

		else:

			return

	elif module == "3":

		alert()

		if login == "1":
		
			loggedIn("1")

		else:

			return

	elif module == "4":

		login = "0"

		return


while status != "q" or status != "Q":
	
	displayMenu()


