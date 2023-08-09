import pandas as pd

test = pd.read_csv("./card_test.csv")
train = pd.read_csv("./card_train.csv")

fraud_col = test["fraud"].value_counts()
print(fraud_col)

print(test.info())
print(train.info())
