import start
class parameter:
    def __init__(self):
        self.dict = {}

    def search_parameter(self,  input_data, target_feature_index):
        params, min_error, feature_importance_dict = start.get_parameters(input_data, target_feature_index)
        parameter = self.format_parameter(params)
        info = {}
        info['parameter'] = parameter
        info['min_error'] = min_error
        info['feature_importance'] = feature_importance_dict
        self.update_dict(target_feature_index, info)

        return parameter, min_error, feature_importance_dict

    def format_parameter(self, params):
        param = {
            'boosting_type': 'gbdt',
            'objective': 'regression_l2',
            'num_threads': 12,
            'max_depth': params['max_depth'],
            'num_leaves': params['num_leaves'],
            'max_bin': params['max_bin'],
            'min_data_in_leaf': params['min_data_in_leaf'],
            'verbose': -1,
            'learning_rate': 0.1,
            'bagging_fraction': params['bagging_fraction'],
            'bagging_freq': params['bagging_freq'],
            'feature_fraction': params['feature_fraction'],
            'lambda_l1': params['lambda_l1'],
            'lambda_l2': params['lambda_l2'],
            'min_gain_to_split': params['min_gain_to_split']
        }

        return param

    def update_dict(self, key, value):
        self.dict[key] = value

    def get_dict(self):
        return self.dict

    def get_feature_info(self, key):
        return self.dict.get(key)

# TODO Save the dictionary to MongoDB





