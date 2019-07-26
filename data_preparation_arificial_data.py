import pandas as pd
import numpy as np
import correlations

#TODO Pfad anpassen
data = pd.read_csv('/home/lchen/parameters/data/small.csv', sep=',')

#TODO Path als Parmeter übergeben
def get_data():
    # features with label included
    x = np.array(data.values)
    return x

def get_correlated_data():
    # features with label included
    corr_data = correlations.eliminate_non_correlated_features(data, -0.5, 0.5)
    x = np.array(corr_data.values)
    return x

def get_feature_names():
    return data.columns.values.tolist()

def get_biomarker_candidate(index):
    names = data.columns.values.tolist()
    return names[index]

#get_correlated_data()
