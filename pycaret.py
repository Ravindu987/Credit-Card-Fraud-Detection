import pandas as pd

from sklearn.preprocessing import StandardScaler
from pycaret.classification import setup, compare_models

data = pd.read_csv("./card_train.csv")
# print(data.head())

# fraud_col = data["fraud"].value_counts()
# print(fraud_col)

columns_to_transform = [
    "distance_from_home",
    "distance_from_last_transaction",
    "ratio_to_median_purchase_price",
]

norm_data = data.copy()
norm_data[columns_to_transform] = StandardScaler().fit_transform(
    data[columns_to_transform]
)

s = setup(norm_data, target="fraud", session_id=123)

best = compare_models()
