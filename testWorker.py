import lightgbm as lgb

from hpbandster.core.worker import Worker
import ConfigSpace as CS

import data_preparation_breast_cancer as to_be_deleted

from sklearn.datasets import load_breast_cancer

class testWorker(Worker):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

        data = load_breast_cancer()

        x = data.data
        y = data.target

        train_data = lgb.Dataset(x, y)
        self.train_loader = train_data

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
            'objective': 'binary',
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
        cv_result = lgb.cv(parameters,
               self.train_loader,
               seed=1,
               nfold=5,
               metrics='binary_error',
               # early_stopping_rounds=15,
               stratified=False
               )

        best_score = cv_result['binary_error-mean'][-1]


        return ({
            'loss': float(best_score), # this is the a mandatory field to run hyperband
            'info': float(best_score)  # can be used for any user-defined information - also mandatory
        })



    @staticmethod
    def get_configspace():
        config_space = CS.ConfigurationSpace()
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('max_depth', lower=3, upper=8))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('num_leaves', lower=3, upper=50))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('min_data_in_leaf', lower=1, upper=10))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('max_bin', lower=3, upper=50))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('bagging_fraction', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformIntegerHyperparameter('bagging_freq', lower=0, upper=50))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('feature_fraction', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('lambda_l1', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('lambda_l2', lower=0, upper=1))
        config_space.add_hyperparameter(CS.UniformFloatHyperparameter('min_gain_to_split', lower=0, upper=1))

        return (config_space)