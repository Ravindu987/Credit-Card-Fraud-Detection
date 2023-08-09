import tensorflow as tf
import pandas as pd
import csv

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.losses import BinaryCrossentropy
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint

from sklearn.preprocessing import StandardScaler

model = tf.keras.models.load_model("./model2.hdf5", compile=False)

model.compile(loss=BinaryCrossentropy(), optimizer="adam", metrics="accuracy")

output = open("./output.csv", mode="w", newline="")
writer = csv.DictWriter(output, fieldnames=["Expected", "Predicted"])
writer.writeheader()

test_data = pd.read_csv("./card_test.csv")
test_x = test_data.drop(columns=["fraud"])

columns_to_transform = [
    "distance_from_home",
    "distance_from_last_transaction",
    "ratio_to_median_purchase_price",
]

test_x[columns_to_transform] = StandardScaler().fit_transform(
    test_x[columns_to_transform]
)

# print(test_x.head())

m = test_x.shape[0]

for i in range(m):
    inp = test_x.iloc[i].values.reshape(-1, 7)
    pred = model.predict(inp)

    if pred[0][0] >= 0.5:
        pred = 1
    else:
        pred = 0

    writer.writerow({"Expected": test_data["fraud"].iloc[i], "Predicted": pred})
