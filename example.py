from parameters import parameter
import data_preparation_arificial_data as parsed_data
import time
import csv
import os

file = './data/result.csv'

if os.path.exists(file):
    os.remove(file)
else:
    print("This file does not exist:", file)

# get the data
input_data = parsed_data.get_data()
# create an object of a parameter
parameter = parameter()

result = {}

global_start = time.time()

print(input_data.shape[0])

for feature_index in range(input_data.shape[1]):
    result_per_feature ={}
    print(feature_index)
    start = time.time()
    # give the feature_name and data to beging search the parameters
    parameter.search_parameter(input_data, feature_index)
    # measure the calculation time per feature
    end = time.time()
    overall_time = end - start
    day = overall_time // (24 * 3600)
    overall_time = overall_time % (24 * 3600)
    hour = overall_time // 3600
    overall_time %= 3600
    minutes = overall_time // 60
    overall_time %= 60
    seconds = overall_time
    duration = (day, hour, minutes, seconds)
    print("calcutaion time per feature -> %d:%d:%d:%d" % (day, hour, minutes, seconds))

    # Search parameters will automatically store the results in a dictionary.
    # If you want to get the dictionary, you can use get_dict()
    # dict = parameter.get_dict()
    # If you want to get the result of a feature, you can use get_feature_info()
    # feature_info contains parameter, min_error, and feature_importance_dict
    feature_info = parameter.get_feature_info(feature_index)

    result.update({feature_index: feature_info})

    for (key, value) in result_per_feature.items():
        print(key, " : ", value)

print('number of features: ', input_data.shape[1])

global_end = time.time()
overall_time = global_end - global_start
day = overall_time // (24 * 3600)
overall_time = overall_time % (24 * 3600)
hour = overall_time // 3600
overall_time %= 3600
minutes = overall_time // 60
overall_time %= 60
seconds = overall_time
duration = (day, hour, minutes, seconds)
print("calcutaion time -> %d:%d:%d:%d" % (day, hour, minutes, seconds))

with open(file, 'a', newline='')as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    header = ('feature', 'min error', 'label importance', 'feature importance')
    writer.writerow(header)
    feature_number = 0
    for (key, value) in result.items():
        feature_info = value
        list_of_row_items = [feature_number, feature_info.get('min_error'), feature_info.get('feature_importance').get(0)]

        # print results
        print('min error:', feature_info.get('min_error'))
        print('label importance:', feature_info.get('feature_importance').get(0))

        if not feature_info.get('feature_importance').get(0):
            list_of_row_items.append(feature_info.get('feature_importance'))
            print('feature importance:', feature_info.get('feature_importance'))

        # save results as csv
        writer.writerow(list_of_row_items)

        print('------------------------------------')
        feature_number = feature_number+1

print(result.get('feature_importance'))
print(result.get('min_error'))

# for (key, value) in result.items():
#     print('feature:',key)
#     feature_info = value
#     #print(feature_info.get('feature_importance'))
#     print('min error:',feature_info.get('min_error'))
#     print('label importance:', feature_info.get('feature_importance').get(0))
#     if not feature_info.get('feature_importance').get(0):
#         print('feature importance:', feature_info.get('feature_importance'))
#     print('------------------------------------')
#     #if key == 'feature_importance':
#         #print(key, " : ", value.get(0))
#     #if key == 'min_error':
#         #print(key, " : ", value)
