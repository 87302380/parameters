import numpy as np
import lightgbm as lgb
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import PowerTransformer
import operator
import warnings
import data_preparation_arificial_data as parsed_data

warnings.filterwarnings("ignore")

def zielFunction(param):
    input_data = parsed_data.get_data_with_label_included()
    selected_y = input_data[:,3]
    selected_x = np.delete(input_data, 3, 1)

    sample_loo = LeaveOneOut()
    for loo_index, (train_index, test_index) in enumerate(sample_loo.split(selected_x)):
               
        x_train = selected_x[train_index]
        y_train = selected_y[train_index]
        x_test = selected_x[test_index]
        y_test = selected_y[test_index]


        x_powerTransformer = PowerTransformer(copy=True, method='yeo-johnson', standardize=True)
        x_train = x_powerTransformer.fit_transform(x_train)
        x_test = x_powerTransformer.transform(x_test)

        y_powerTransformer = PowerTransformer(copy=True, method='yeo-johnson', standardize=True)
        y_train = y_powerTransformer.fit_transform(y_train.reshape(-1, 1))[:, 0]
        y_test = y_powerTransformer.transform(y_test.reshape(-1, 1))[:, 0]

        train_data = lgb.Dataset(x_train, label=y_train)
        test_data = lgb.Dataset(x_test, label=y_test)

        evals_result = {}
        booster = lgb.train(param,
                            train_data,
                            valid_sets=[test_data],
                            early_stopping_rounds=15,
                            verbose_eval=False,
                            evals_result=evals_result,
                            )
    print(min(evals_result['valid_0']['l2']))
    return min(evals_result['valid_0']['l2'])

# param = []
# zielFunction(param)