import json

from pprint import pprint

def viewData():
	
	data = json.load(open('data.json'))

	for item in data:

		print("\nName: ",data[item]["name"])

		print("Email: ",data[item]["email"])

		print("Address: ",data[item]["address"])

		print("Phone-number: ",data[item]["phone-number"])

		print("Date: ",data[item]["date"],"\n")