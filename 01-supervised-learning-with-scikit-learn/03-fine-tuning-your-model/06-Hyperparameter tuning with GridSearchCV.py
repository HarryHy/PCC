# Import necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Setup the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space}

# Instantiate a logistic regression classifier: logreg
logreg = LogisticRegression()

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

# Fit it to the data
logreg_cv.fit(X,y)

# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_)) 
print("Best score is {}".format(logreg_cv.best_score_))

<script.py> output:
    Tuned Logistic Regression Parameters: {'C': 3.7275937203149381}
    Best score is 0.7708333333333334

'''
Import LogisticRegression from sklearn.linear_model and GridSearchCV from sklearn.model_selection.
Setup the hyperparameter grid by using c_space as the grid of values to tune C over.
Instantiate a logistic regression classifier called logreg.
Use GridSearchCV with 5-fold cross-validation to tune C:
Inside GridSearchCV(), specify the classifier, parameter grid, and number of folds to use.
Use the .fit() method on the GridSearchCV object to fit it to the data X and y.
Print the best parameter and best score obtained from GridSearchCV by accessing the best_params_ and best_score_ attributes of logreg_cv.
'''
