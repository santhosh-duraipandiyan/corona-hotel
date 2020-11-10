import json

from pprint import pprint

def viewData():
	
	data = json.load(open('data.json'))

	print("##########################################")

	for item in data:

		if data[item]["name"] == "dummy":
			
			return

		print("\nName: ",data[item]["name"])

		print("Email: ",data[item]["email"])

		print("Address: ",data[item]["address"])

		print("Phone-number: ",data[item]["phone-number"])

		print("Date: ",data[item]["date"],"\n")

		print("##########################################")
