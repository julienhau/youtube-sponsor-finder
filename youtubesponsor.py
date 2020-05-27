#! python3

import requests, json, pprint, re
import smtplib, ssl

port = 465  # For SSL

context = ssl.create_default_context()

SENDER_EMAIL = ''
RECEIVER_EMAIL = ''
PASSWORD = ''
YOUR_KEY = ''

def mail(message):
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	    server.login(SENDER_EMAIL, PASSWORD)
	    server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,message)


regex = re.compile(r'discount|deal|sponsor|\d\d% off|giveaway',re.I)

for i in [0,15,19,20,23,24,26,28]:
	res = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=50&videoCategoryId={i}&key={YOUR_KEY}')
	print(i)
	string = ''
	for i in json.loads(res.text)['items']:
		mo = regex.search(i['snippet']['description'])
		if mo != None:
			description = i['snippet']['description'] + '\n\n\n\n -------\n\n\n\n-------'
			string += description
	encoded_string = string.encode('ascii','ignore')
	decoded_string = encoded_string.decode()
	mail(decoded_string)
