import json

from datetime import datetime

from datetime import date

def Convert(lst):

	res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
	
	return res_dct

def addData():

	userData = {}

	name = email = address = ph = today = ""

	name = input("\nEnter the name: ")

	email = input("\nEnter the email: ")

	address = input("\nEnter the address: ")

	ph = input("\nEnter the phone-number: ")

	today1 = datetime.now()

	today2 = date.today()

	temp1 = str(today1)

	temp2 = str(today2)

	userData = {temp1: {'name': name, 'email': email, 'address': address, 'phone-number': ph, "date": temp2}}

	# Opening JSON file 
	with open('data.json') as json_file: 

		data = json.load(json_file)

		userData.update(data)

	with open('data.json', 'w') as fp:

		json.dump(userData, fp)

	print("\nData entered successfully!\n")

	
