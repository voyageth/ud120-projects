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

from feature_format import featureFormat
from feature_format import targetFeatureSplit

print(enron_data[enron_data.keys()[0]].keys())

names = enron_data.keys()
features = ['salary', 'to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances', 'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income', 'long_term_incentive', 'from_poi_to_this_person']

feature_formatted = featureFormat(enron_data, features, remove_all_zeroes=False)
for i in range(len(feature_formatted)):
    print(i, ":", feature_formatted[i])
# print(len(feature_formatted[0]))
# print(feature_formatted[0][0])

# [user1's feature array, user2's feature array]

splitted = targetFeatureSplit(feature_formatted)
feature_array = feature_formatted
for i in range(len(features)):
    print(features[i])
    feature_array = targetFeatureSplit(feature_array)
    print("user1's feature value : ", feature_array[0][0])
    print("user2's feature value : ", feature_array[0][1])
    feature_array = feature_array[1]


# print(len(splitted[0]))
# print(len(splitted[1]))
#
# print(splitted[0][0])
# print(splitted[1][0])

import pandas as pd

df = pd.DataFrame()

feature_array = feature_formatted
for i in range(len(features)):
    feature_array = targetFeatureSplit(feature_array)
    df[features[i]] = feature_array[0]
    feature_array = feature_array[1]

print(df.describe())
print(df.head())

print(len(df[df['total_payments'] == 0]), float(len(enron_data)))

total_count=0
total_payments_nan_count = 0
for name in enron_data:
    total_count +=1
    row = enron_data[name]
    if row['total_payments'] == 'NaN':
        total_payments_nan_count += 1

print("total_payments_nan_count:", total_payments_nan_count, "total_count:", total_count, "percentage:", total_payments_nan_count / float(total_count))

# print("---------")
# print(df[df['total_payments'] == 0])
# print("==========")
# for name in enron_data:
#     row = enron_data[name]
#     if row['total_payments'] == 'NaN':
#         print(row)

