#login system

from add import addData

from view import viewData

from alert import alert

import json

with open('users.json') as json_file: 

    users = json.load(json_file)

status = ""

user = {}

def displayMenu():
	
	status = input("\nAlready have account...Y/N? press q to quit: ")

	if status == "y" or status == "Y":

		oldUser()
	
	elif status == "n" or status == "N":

		newUser()

	elif status == "q":

		exit()


def newUser():
	
	createLogin = input("\nEnter the username: ")

	if createLogin in users:

		print("\n User already exist!\n")

	else:

		createPass = input("\nEnter Password: ")

		user[createLogin] = createPass

		print("\nUser created successfully! Now login!\n")

		file = open("users.json", "r+")
		
		data = json.load(file)

		data.update(user)

		file.seek(0)

		json.dump(data, file)
		
		file.close()


def oldUser():
	
	login = input("\nEnter username: ")

	passw = input("\nEnter password: ")

	if login in users and users[login] == passw:
		
		print("\nLogin successful!\n")

		module = input("Press 1 for add data.\tpress 2 for view data.\tpress 3 to alert users\n\n")

		if module == "1":
			
			addData()

		elif module == "2":

			viewData()

		elif module == "3":

			alert()

	else:

		print("\nIncorrect username or password!\n")

while status != "q":
	
	displayMenu()


