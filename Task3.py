"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def extract_code(number):
	startNums = ("7", "8", "9")
	telemarketer_area_code = "140"
	if number.startswith('(0'):
		return number[0:number.index(')') + 1]
	elif number.startswith(startNums):
		return number[0:4]
	elif number.startswith(telemarketer_area_code):
		return telemarketer_area_code
	return None

def get_called(calls, code):
	calledList = []
	for record in calls:
		calling, answering, *_ = record
		if extract_code(calling) == code:
			calledList.append(extract_code(answering))
	return calledList

def percentage(codes, code):
	return codes.count(code) / len(codes) * 100

bangalore_area_code = "(080)"

codes = get_called(calls, bangalore_area_code)
unique_codes = set(codes)
unique_codes_list = list(unique_codes)
unique_codes_list.sort()


print("The numbers called by people in Bangalore have codes:")
for code in unique_codes_list:
   print(code)

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
 				.format(percentage(codes, bangalore_area_code)))

