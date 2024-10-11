import warnings
# Suppress all warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    recall_score,
    accuracy_score,
    precision_score,
    f1_score,
    cohen_kappa_score,
    make_scorer
)

import numpy as np
import pandas as pd
import time
import pickle
import warnings

warnings.filterwarnings("ignore")






def classification_parameter_finder(model,
                                    parameters : dict,
                                    X_train : np.array,
                                    y_train : np.array,
                                    X_test : np.array,
                                    y_test : np.array) -> None:
    start = time.time()

    kappa_scorer = make_scorer(cohen_kappa_score)

    grid = GridSearchCV(model,
                        param_grid=parameters,
                        refit=True,
                        cv=2, 
                        n_jobs=-1,
                        scoring=kappa_scorer)
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    print(type(best_model))
    with open("model.pkl", 'wb') as file:
        pickle.dump(best_model, file)
    print(f"Best model saved to local")
