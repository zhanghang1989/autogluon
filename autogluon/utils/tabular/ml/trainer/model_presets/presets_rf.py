from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, ExtraTreesClassifier, ExtraTreesRegressor
from ...models.rf.rf_model import RFModel


def rf_classifiers(hyperparameters, path, problem_type, objective_func):
    models = []
    params = {'n_estimators': 300, 'n_jobs': -1}
    params.update(hyperparameters.copy())  # TODO: Move into RFModel, currently ignores hyperparameters
    params_gini = params.copy()
    params_gini['criterion'] = 'gini'
    models.append(
        RFModel(path=path, name='RandomForestClassifierGini', model=RandomForestClassifier(**params_gini), problem_type=problem_type,
                objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    )
    params_entro = params.copy()
    params_entro['criterion'] = 'entropy'
    models.append(
        RFModel(path=path, name='RandomForestClassifierEntr', model=RandomForestClassifier(**params_entro), problem_type=problem_type,
                objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    )
    # if objective_func.name == 'roc_auc':  # TODO: Update to any metric that is negatively impacted by class imbalance
    #     params_gini_balanced = params.copy()
    #     params_gini_balanced['criterion'] = 'gini'
    #     params_gini_balanced['class_weight'] = 'balanced'
    #     models.append(
    #         RFModel(path=path, name='RandomForestClassifierGiniBalanced', model=RandomForestClassifier(**params_gini_balanced), problem_type=problem_type,
    #                 objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    #     )
    #     params_entro_balanced = params.copy()
    #     params_entro_balanced['criterion'] = 'entropy'
    #     params_entro_balanced['class_weight'] = 'balanced'
    #     models.append(
    #         RFModel(path=path, name='RandomForestClassifierEntrBalanced', model=RandomForestClassifier(**params_entro_balanced), problem_type=problem_type,
    #                 objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    #     )


    return models


def xt_classifiers(hyperparameters, path, problem_type, objective_func):
    models = []
    params = {'n_estimators': 300, 'n_jobs': -1}
    params.update(hyperparameters.copy())  # TODO: Move into RFModel, currently ignores hyperparameters
    params_gini = params.copy()
    params_gini['criterion'] = 'gini'
    models.append(
        RFModel(path=path, name='ExtraTreesClassifierGini', model=ExtraTreesClassifier(**params_gini), problem_type=problem_type,
                objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    )
    params_entro = params.copy()
    params_entro['criterion'] = 'entropy'
    models.append(
        RFModel(path=path, name='ExtraTreesClassifierEntr', model=ExtraTreesClassifier(**params_entro), problem_type=problem_type,
                objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    )
    # if objective_func.name == 'roc_auc':  # TODO: Update to any metric that is negatively impacted by class imbalance
    #     params_gini_balanced = params.copy()
    #     params_gini_balanced['criterion'] = 'gini'
    #     params_gini_balanced['class_weight'] = 'balanced'
    #     models.append(
    #         RFModel(path=path, name='ExtraTreesClassifierGiniBalanced', model=ExtraTreesClassifier(**params_gini_balanced), problem_type=problem_type,
    #                 objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    #     )
    #     params_entro_balanced = params.copy()
    #     params_entro_balanced['criterion'] = 'entropy'
    #     params_entro_balanced['class_weight'] = 'balanced'
    #     models.append(
    #         RFModel(path=path, name='ExtraTreesClassifierEntrBalanced', model=ExtraTreesClassifier(**params_entro_balanced), problem_type=problem_type,
    #                 objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    #     )

    return models


def rf_regressors(hyperparameters, path, problem_type, objective_func):
    models = []
    params = {'n_estimators': 300, 'n_jobs': -1}
    params.update(hyperparameters.copy())  # TODO: Move into RFModel, currently ignores hyperparameters
    params_mse = params.copy()
    params_mse['criterion'] = 'mse'
    models.append(
        RFModel(path=path, name='RandomForestRegressorMSE', model=RandomForestRegressor(**params_mse), problem_type=problem_type,
                objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    )
    # TODO: Slow, perhaps only do mae if objective func is mae
    # params_mae = params.copy()
    # params_mae['criterion'] = 'mae'
    # models.append(
    #     RFModel(path=path, name='RandomForestRegressorMAE', model=RandomForestRegressor(**params_mae), problem_type=problem_type,
    #             objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    # )
    return models


def xt_regressors(hyperparameters, path, problem_type, objective_func):
    models = []
    params = {'n_estimators': 300, 'n_jobs': -1}
    params.update(hyperparameters.copy())  # TODO: Move into RFModel, currently ignores hyperparameters
    params_mse = params.copy()
    params_mse['criterion'] = 'mse'
    models.append(
        RFModel(path=path, name='ExtraTreesRegressorMSE', model=ExtraTreesRegressor(**params_mse), problem_type=problem_type,
                objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    )
    # TODO: Slow, perhaps only do mae if objective func is mae
    # params_mae = params.copy()
    # params_mae['criterion'] = 'mae'
    # models.append(
    #     RFModel(path=path, name='ExtraTreesRegressorMAE', model=ExtraTreesRegressor(**params_mae), problem_type=problem_type,
    #             objective_func=objective_func, hyperparameters=hyperparameters.copy()),
    # )
    return models