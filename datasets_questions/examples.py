#!/usr/bin/python

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

examples = 5
i = 0

for person in enron_data:
	if i >= examples:
		break
	i += 1

	print person
	for item in enron_data[person].keys():

		print "		", item, enron_data[person][item]







"""
email_addresses = 0

if enron_data[(person).upper()]["email_address"] == "NaN":
		continue
	else:
		print enron_data[(person).upper()]["email_address"]
		if "@" in enron_data[(person).upper()]["email_address"]:
			email_addresses += 1
print "email_address: ", email_addresses



for person in ["Lay", "Skilling", "Fastow"]:
	person = person.upper()
	for name in enron_data:
		if person in name:
			person = name
			break
	print person, enron_data[(person).upper()]["total_payments"]

	#for x in enron_data[(person).upper()]:
	#	print x, enron_data[(person).upper()][x]
"""
