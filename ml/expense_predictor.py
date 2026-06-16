import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def predict_next_expense(expenses_df):

    if len(expenses_df) < 3:
        return None

    X = np.arange(len(expenses_df)).reshape(-1, 1)

    y = expenses_df["amount"]

    model = LinearRegression()

    model.fit(X, y)

    next_period = np.array([[len(expenses_df)]])

    prediction = model.predict(next_period)[0]

    return prediction