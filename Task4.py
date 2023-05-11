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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


outgoing_calls_list = []
receive_calls_list = []
telemarketers = []

for record in calls:
    outgoing_number = record[0]
    receive_number = record[1]

    if outgoing_number not in outgoing_calls_list:
        outgoing_calls_list.append(outgoing_number)

    if receive_number not in receive_calls_list:
        receive_calls_list.append(receive_number)

outgoing_texts_list = []
receive_texts_list = []

for record in texts:
    outgoing_number = record[0]
    receive_number = record[1]

    if outgoing_number not in outgoing_texts_list:
        outgoing_texts_list.append(outgoing_number)

    if receive_number not in receive_texts_list:
        receive_texts_list.append(receive_number)

for phoneNum in outgoing_calls_list:
    if((phoneNum not in receive_calls_list) and (phoneNum not in outgoing_texts_list) and (phoneNum not in receive_texts_list)):
        telemarketers.append(phoneNum)


print("These numbers could be telemarketers: ")
print(*sorted(telemarketers), sep='\n')
