import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(expenses_df):

    if len(expenses_df) < 5:
        return pd.DataFrame()

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    expenses_df = expenses_df.copy()

    expenses_df["anomaly"] = model.fit_predict(
        expenses_df[["amount"]]
    )

    anomalies = expenses_df[
        expenses_df["anomaly"] == -1
    ]

    return anomalies