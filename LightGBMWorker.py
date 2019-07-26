# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import f1_score
# import numpy as np
# import data_preparation_bacmen_vs_viral as data
# import data_preparation_arificial_data as data
import feature_weights as test
from hpbandster.core.worker import Worker
import ConfigSpace as CS


class LightGBMWorker(Worker):
    def __init__(self, sleep_interval, data, target_feature_index,**kwargs):
        super().__init__(**kwargs)

        self.sleep_interval = sleep_interval
        self.train_loader = data
        self.test_loader = target_feature_index
    def compute(self, config, budget, *args, **kwargs):
        max_depth = int(config['max_depth'])
        num_leaves = int(config['num_leaves'])
        max_bin = int(config['max_bin'])
        min_data_in_leaf = int(config['min_data_in_leaf'])
        # num_trees = int(config['num_trees'])
        bagging_fraction = config['bagging_fraction']
        bagging_freq = int(config['bagging_freq'])
        feature_fraction = config['feature_fraction']
        lambda_l1 = config['lambda_l1'],
        lambda_l2 = config['lambda_l2'],
        min_gain_to_split = config['min_gain_to_split']

        parameters = {
            'boosting_type': 'gbdt',
            'objective': 'regression_l2',
            'num_threads': 3,
            'learning_rate': 0.1,
            'num_leaves': num_leaves,
            'max_depth': max_depth,
            'min_data_in_leaf': min_data_in_leaf,
            # 'num_trees': num_trees,
            'max_bin': max_bin,
            'bagging_fraction': bagging_fraction,
            'bagging_freq': bagging_freq,
            'feature_fraction': feature_fraction,
            'verbose': -1,
            'lambda_l1': lambda_l1,
            'lambda_l2': lambda_l2,
            'min_gain_to_split': min_gain_to_split
        }

        best_score, feature_importance_dict = test.analyze_features(parameters, self.train_loader, self.test_loader)
        # print('best score:', best_score)
        return ({
            'loss': float(best_score), # this is the a mandatory field to run hyperband
            'info': feature_importance_dict,  # can be used for any user-defined information - also mandatory
        })

    @staticmethod
    def get_configspace():
        config_space = CS.ConfigurationSpace()
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('max_depth', lower=3, upper=6))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('num_leaves', lower=3, upper=5))
        # config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('num_trees', lower=3, upper=50))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('min_data_in_leaf', lower=1, upper=2))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('max_bin', lower=3, upper=8))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('bagging_fraction', lower=0.1, upper=0.9))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('bagging_freq', lower=0, upper=50))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('feature_fraction', lower=0.1, upper=0.9))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('lambda_l1', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('lambda_l2', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('min_gain_to_split', lower=0, upper=1))

        return (config_space)
