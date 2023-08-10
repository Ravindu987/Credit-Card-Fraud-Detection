import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import mlflow
import mlflow.tensorflow

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.losses import BinaryCrossentropy
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


learning_rate = 0.001
epochs = 5

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

# print(data.head())

train_x = norm_data.drop("fraud", axis=1)
train_y = norm_data["fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    train_x, train_y, test_size=0.2, stratify=train_y, random_state=42
)

# print(train_x.head())
# print(y_test.value_counts())

check = ModelCheckpoint(
    filepath="./model2.hdf5", save_best_only=True, monitor="val_accuracy", verbose=True
)
stop = EarlyStopping(monitor="val_loss", patience=5)

with mlflow.start_run():
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("epochs", epochs)

    model = Sequential(
        [
            Dense(
                16, activation="relu", kernel_initializer="he_uniform", input_shape=(7,)
            ),
            Dense(4, activation="relu", kernel_initializer="he_uniform"),
            Dense(1, activation="sigmoid"),
        ]
    )

    model.compile(
        loss="binary_crossentropy",
        optimizer=Adam(learning_rate=learning_rate),
        metrics="accuracy",
    )

    hist = model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=16,
        callbacks=[check, stop],
    )

    mlflow.log_metric("final_loss", hist.history["loss"][-1])
    mlflow.log_metric("final_accuracy", hist.history["accuracy"][-1])

    mlflow.tensorflow.log_model(model, "tensorflow-model")

train_loss = hist.history["loss"]
val_loss = hist.history["val_loss"]

plt.plot(train_loss, label="Training Loss")
plt.plot(val_loss, label="Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()
