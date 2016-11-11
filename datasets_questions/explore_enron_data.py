#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("row count : {}, feature count : {}".format(len(enron_data), len(enron_data[enron_data.keys()[0]])))

from poi_email_addresses import poiEmails

salary_exist_count = 0
email_exist_count = 0
none_count = 0
true_count = 0
true_contain_count = 0
false_count = 0
for name in enron_data:
    row = enron_data[name]
    if row['salary'] != 'NaN':
        salary_exist_count += 1
    if row['email_address'] != 'NaN':
        email_exist_count += 1

    if row['poi'] is None:
        none_count += 1
    elif row['poi']:
        if row['email_address'] in poiEmails():
            true_contain_count += 1
        true_count += 1
    else:
        false_count += 1

print("none_count:{}, true_count:{}, false_count:{}, total_count:{}".format(none_count, true_count, false_count,
                                                                            none_count + true_count + false_count))

'../final_project/poi_names.txt'

print("true_contain_count:{}".format(true_contain_count))

print(enron_data['PRENTICE JAMES']['total_stock_value'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# print(enron_data.keys())
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])

print(enron_data['FASTOW ANDREW S'])

print("salary_exist_count:{}, email_exist_count:{}".format(salary_exist_count, email_exist_count))