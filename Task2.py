"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def track_duration(dictionary, phone, duration):
	if(dictionary.get(phone)==None):
		dictionary[phone]= int(duration)
	else:
		dictionary[phone] = dictionary.get(phone)+ int(duration)
	return dictionary

def get_by_month(call, month, year):
	time_stamp= call[2]
	date_object= datetime.strptime(time_stamp, '%d-%m-%Y %H:%M:%S')
	year_call = date_object.year
	month_call = date_object.month

	if(year_call==year and month_call==month):
		return True
	else:
		return False

records= filter(lambda x: get_by_month(x,9,2016),calls)
dictionary={}

for record in records:
	outgoing_number=record[0]
	incoming_number=record[1]
	duration=record[3]
	dictionary= track_duration(dictionary,outgoing_number,duration)
	dictionary= track_duration(dictionary, incoming_number,duration)

phone_number = max(dictionary.items(), key=lambda str: int(str[1]))

print(f"{phone_number[0]} spent the longest time, {phone_number[1]} seconds, on the phone during September 2016.")


