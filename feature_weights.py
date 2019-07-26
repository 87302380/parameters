import numpy as np
import lightgbm as lgb
from sklearn.model_selection import KFold
from sklearn.preprocessing import PowerTransformer
import warnings
import shap

warnings.filterwarnings("ignore")

def save_shap_feature_importances(booster, x_train, feature_indices, shap_feature_importance_dict):

    # read the feature importances from the booster via shap (https://github.com/slundberg/shap)
    explainer = shap.TreeExplainer(booster)
    shap_values = explainer.shap_values(x_train)
    feature_importances = np.sum(np.abs(shap_values), axis=0) #TODO check negative shap values

    # summarize the effects of all the features
    # shap.summary_plot(shap_values, x_train, plot_type="bar")

    # combine the feature importance and the feature name
    feature_importance_tuples = sorted(zip(feature_indices, feature_importances), key=lambda x: x[1])  # zip verschränkt Listen (1a 2b 3c...)

    # save features where the importance is > 0 and dismiss the rest
    # keep important features only and remove all features with importance = 0
    feature_importance_tuples = [(int(x[0]), x[1]) for x in feature_importance_tuples if x[1] > 0]

    # add the feature importances of each iteration of the cv
    for important_feature, importance in feature_importance_tuples:
        if not important_feature in shap_feature_importance_dict:
            shap_feature_importance_dict.setdefault(important_feature, importance)
        else:
            # the best score is minimal -> importance/score to maximize ########## ELSE MULTIPLY #########!!!!!!
            shap_feature_importance_dict[important_feature] = shap_feature_importance_dict[important_feature] + importance
    return

# check the label importance and the regression error for the given target feature
def analyze_features(param, input_data, target_feature_index):

    # split target feature and train data
    selected_y = input_data[:, target_feature_index]
    selected_x = np.delete(input_data, target_feature_index, 1)

    #TODO set number_of_folds as input parameter
    #number_of_folds = selected_x.shape[0]
    number_of_folds = 3

    shap_feature_importance_dict = {}
    best_score_list = []

    sample_kfold = KFold(number_of_folds)
    for loo_index, (train_index, test_index) in enumerate(sample_kfold.split(selected_x)):
               
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

        # save the indices of the features in the train data as strings
        feature_indices = list(range(len(x_train[1])+1))
        feature_indices.pop(target_feature_index)
        str(feature_indices)

        save_shap_feature_importances(booster, x_train, feature_indices, shap_feature_importance_dict)

        best_score = min(evals_result['valid_0']['l2'])  # welcher score ist hier am besten?
        best_score_list.append(best_score)

    min_error = min(best_score_list)
    print(min_error)
    return min_error, shap_feature_importance_dict

# param = []
# zielFunction(param)
# import data_preparation_arificial_data as input_data
# feature = 5
# param = {'verbose':-1, 'num_threads': 12, 'objective':'regression_l2', 'bagging_fraction': 0.3576688874000573, 'bagging_freq': 0, 'feature_fraction': 0.2457162859554748, 'lambda_l1': 0.697194590872183, 'lambda_l2': 0.31189989669135243, 'max_bin': 28, 'max_depth': 5, 'min_data_in_leaf': 2, 'min_gain_to_split': 0.1796958782513518, 'num_leaves': 50, 'num_trees': 30}
# analyze_features(param, input_data.get_data_with_label_included(), feature)