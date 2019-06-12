from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import lightgbm as lgb
import numpy as np

import start

dataset = load_breast_cancer()

x = dataset.data
y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                    test_size = 0.2,
                                                    random_state=42,
                                                    stratify = y,
                                                    shuffle = True)

train_data = lgb.Dataset(x_train, label=y_train, free_raw_data=False).construct()
test_data = lgb.Dataset(x_test, label=y_test, free_raw_data=False).construct()


def get_f1_score(model):
    predict = model.predict(test_data.data, num_iteration=model.best_iteration)
    predict_label = np.round(predict)
    print(f1_score(test_data.get_label(), predict_label, average='micro'))

    return f1_score(test_data.get_label(), predict_label, average='micro')


param = start.get_parameters()

params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'max_depth': param['max_depth'],
    'num_leaves': param['num_leaves'],
    'max_bin':param['max_bin'],
    'min_data_in_leaf': param['min_data_in_leaf'],
    'verbose': -1,
    'learning_rate': 0.1,
    'bagging_fraction': param['bagging_fraction'],
    'bagging_freq': param['bagging_freq'],
    'feature_fraction': param['feature_fraction'],
    'lambda_l1': param['lambda_l1'],
    'lambda_l2': param['lambda_l2'],
    'min_gain_to_split': param['min_gain_to_split']
}


gbm = lgb.train(params,
                train_data,
                num_boost_round=10,
                valid_sets=test_data,
                early_stopping_rounds=5)


predict = gbm.predict(x_test, num_iteration=gbm.best_iteration)

get_f1_score(gbm)
