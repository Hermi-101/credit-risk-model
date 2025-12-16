import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Set a global random state for reproducibility
RANDOM_STATE = 42

# Load the data with the engineered target variable
df_final = pd.read_csv('data/processed/df_customer_target.csv')

# Define Features and Target
EXCLUDE_COLS = ['CustomerId', 'Cluster_ID', 'is_high_risk']
FEATURE_COLS = [col for col in df_final.columns if col not in EXCLUDE_COLS]
TARGET_COL = 'is_high_risk'

X = df_final[FEATURE_COLS]
y = df_final[TARGET_COL]

# Split the data (80% train, 20% test, stratified to maintain class balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

print(f"Data Split: Train samples={len(X_train)}, Test samples={len(X_test)}")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

def evaluate_model(y_test, y_pred, y_pred_proba):
    """Calculates and returns standard classification metrics."""
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_pred_proba),
    }
    return metrics

