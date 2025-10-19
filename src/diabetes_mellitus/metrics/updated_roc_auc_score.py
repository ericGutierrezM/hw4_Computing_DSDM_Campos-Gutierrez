from sklearn.metrics import roc_auc_score

def updated_roc_auc_score(updated_X_train, updated_X_test, y_train, y_test):
    train_roc_auc = roc_auc_score(y_train, updated_X_train['prediction'])
    test_roc_auc = roc_auc_score(y_test, updated_X_test['prediction'])
    return train_roc_auc, test_roc_auc