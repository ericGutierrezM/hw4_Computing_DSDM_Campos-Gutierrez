from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def fit_model(X_train, X_test, y_train):
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std  = sc.transform(X_test)
    modelLogistic = LogisticRegression(penalty=None, solver='lbfgs', max_iter=2000, random_state=102)
    modelLogistic.fit(X_train_std, y_train)
    train_y_pred = modelLogistic.predict_proba(X_train_std)[:, 1]
    test_y_pred = modelLogistic.predict_proba(X_test_std)[:, 1]
    updated_X_train = X_train
    updated_X_train['prediction'] = train_y_pred
    updated_X_test = X_test
    updated_X_test['prediction'] = test_y_pred
    return updated_X_train, updated_X_test
