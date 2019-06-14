# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import f1_score
# import lightgbm as lgb
# import numpy as np

# import data_preparation_bacmen_vs_viral as to_be_deleted
# import data_preparation_arificial_data as to_be_deleted
import data_preparation_breast_cancer as to_be_deleted
from hpbandster.core.worker import Worker
import ConfigSpace as CS

from regression_classifier import get_accuracy

class LightGBMWorker(Worker):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

        # Load data here
        data = to_be_deleted.get_data_with_label_included()
        self.train_loader = data
        # self.test_loader = lgb.Dataset(x_test, label=y_test)


    def compute(self, config, budget, *args, **kwargs):
        max_depth = int(config['max_depth'])
        num_leaves = int(config['num_leaves'])
        max_bin = int(config['max_bin'])
        min_data_in_leaf = int(config['min_data_in_leaf'])
        num_trees = int(config['num_trees'])
        bagging_fraction = config['bagging_fraction']
        bagging_freq = int(config['bagging_freq'])
        feature_fraction = config['feature_fraction']
        lambda_l1 = config['lambda_l1'],
        lambda_l2 = config['lambda_l2'],
        min_gain_to_split = config['min_gain_to_split']

        parameters = {
            'boosting_type': 'gbdt',
            'objective': 'regression',
            'learning_rate': 0.1,
            'num_leaves': num_leaves,
            'max_depth': max_depth,
            'min_data_in_leaf': min_data_in_leaf,
            'num_trees': num_trees,
            'max_bin': max_bin,
            'bagging_fraction': bagging_fraction,
            'bagging_freq': bagging_freq,
            'feature_fraction': feature_fraction,
            'verbose': -1,
            'lambda_l1': lambda_l1,
            'lambda_l2': lambda_l2,
            'min_gain_to_split': min_gain_to_split
        }

        accuracy = get_accuracy(self.train_loader, parameters, 15)
        1-accuracy/100

        return ({
            'loss': float(1-accuracy/100),  # this is the a mandatory field to run hyperband
            # 'info': f1_score  # can be used for any user-defined information - also mandatory
        })

    @staticmethod
    def get_configspace():
        config_space = CS.ConfigurationSpace()
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('max_depth', lower=3, upper=6))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('num_leaves', lower=3, upper=50))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('num_trees', lower=3, upper=50))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('min_data_in_leaf', lower=1, upper=8))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('max_bin', lower=3, upper=50))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('bagging_fraction', lower=0.1, upper=0.9))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('bagging_freq', lower=0, upper=50))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('feature_fraction', lower=0.1, upper=0.9))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('lambda_l1', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('lambda_l2', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('min_gain_to_split', lower=0, upper=1))

        return (config_space)