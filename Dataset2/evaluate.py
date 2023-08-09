import pandas as pd

from sklearn.metrics import precision_score, recall_score, f1_score

result = pd.read_csv("./output.csv")

actual_column = result["Expected"].astype(int)
pred_column = result["Predicted"]

print(actual_column.value_counts())
print(pred_column.value_counts())

precision = precision_score(actual_column, pred_column)
recall = recall_score(actual_column, pred_column)
f1 = f1_score(actual_column, pred_column)

print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
