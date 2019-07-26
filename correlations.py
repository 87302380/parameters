import scipy.stats as stats
import numpy as np
import pandas as pd
import csv
import os

file = '/home/lchen/parameters/data/correlation.csv'

if os.path.exists(file):
    os.remove(file)
else:
    print("This file does not exist:", file)

with open(file, 'a', newline='')as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    header = ('feature', 'kendall')
    writer.writerow(header)

def eliminate_non_correlated_features(data, lower_bound = -0.5, upper_bound = 0.5):
    number_of_features = data.shape[1]
    label = data['0']
    feature_names = data.columns.values.tolist()
    correlated_features = data
    for x in range(1, number_of_features):
        print(x,'from',number_of_features)
        #result1 = stats.spearmanr(label, data[feature_names[x]])
        #correlation_coefficient = result1[0]
        #kendall
        #result2 = stats.pearsonr(label, data[feature_names[x]])
        #correlation_coefficient2 = result2[0]
        result2 = stats.kendalltau(label, data[feature_names[x]])
        correlation_coefficient2 = result2[0]
        #print(correlation_coefficient)
        #print(correlation_coefficient2)
        #print('--------------------------------------------------')
        # if the feature is not correlated to the label delete feature from dataset
        if (correlation_coefficient2 < upper_bound) and (correlation_coefficient2 > lower_bound):
            correlated_features.drop(feature_names[x], axis=1, inplace=True)
        else:
            print(correlation_coefficient2)
            #print(correlation_coefficient)
            print('--------------------------------------------------')
            element = (x, correlation_coefficient2)
            with open(file, 'a', newline='')as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(element)
    print(data)
    return correlated_features
