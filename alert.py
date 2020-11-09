import smtplib

import json

from email.message import EmailMessage

def emailAlert(subject, body, to):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to

	user = "lividsamael@gmail.com"
	msg['from'] = user
	password = "nfdehxcpwwcbeelq"

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user, password)
	server.send_message(msg)
	server.quit()

def alert():

	date = input("Enter the date (format: year-month-day (xxxx-xx-xx)): ")
	
	data = json.load(open('data.json'))

	for item in data:

		if data[item]["date"] == date:

			emailAlert("Corona alert", "Someone from restarunt you stayed in have corona!", data[item]["email"])

			print("Email sent successfully for: ",data[item]["name"])

		
	
	
