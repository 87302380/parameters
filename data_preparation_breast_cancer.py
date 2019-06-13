from sklearn.datasets import load_breast_cancer
import numpy as np
import csv

data = load_breast_cancer()

def get_biomarker_candidate(index):
    lables = data.get('target', '')
    return lables[index]

def get_data_with_label_included():
    data_array = data.get('data', '')
    lables = data.get('target', '')
    lables = lables.reshape(-1, 1)
    label_in_first_row = np.hstack((lables, data_array))
    minimized_data = np.empty((8,label_in_first_row.shape[1]))

    j=0
    k=4
    for i in range(200):
        if (label_in_first_row[i,0] == 0)&(j<4):
            minimized_data[j] = label_in_first_row[i]
            j = j+1
        if (label_in_first_row[i,0] == 1.0)&(k<8):
            minimized_data[k] = label_in_first_row[i]
            k = k + 1
        if (j >= 4)&(k >= 8):
            break

    # with open('./data/breast_cancer.csv', 'a', newline='')as csv_file:
    #     writer = csv.writer(csv_file, delimiter=',')
    #     for i in np.nditer(label_in_first_row):
    #         writer.writerow(label_in_first_row[i])

    return minimized_data

def get_data_without_label_included():
    data_array = data.get('data', '')
    minimized_data = np.empty((569,data_array.shape[1]))

    j=0
    k=4
    for i in range(200):
        if (data_array[i,0] == 0)&(j<4):
            minimized_data[j] = data_array[i]
            j = j+1
        if (data_array[i,0] == 1.0)&(k<8):
            minimized_data[k] = data_array[i]
            k = k + 1
        if (j >= 4)&(k >= 8):
            break

    return minimized_data

#returns labels as numpy array
def get_labels():
    return data.target