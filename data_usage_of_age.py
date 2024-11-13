import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("user_behavior_dataset.csv")
data = dataframe[["Data Usage (MB/day)", "Age"]]
ages = data["Age"].sort_values().unique()
dct = {"age": [], "data usage": []}

for age in ages:
    res = data[data["Age"] == age].mean()
    dct["age"].append(int(res["Age"]))
    dct["data usage"].append(int(res["Data Usage (MB/day)"]))

df = pd.DataFrame(dct)
print(df.columns)
plt.xlabel('Возраст')
plt.ylabel('Потребление данных')
plt.bar(df["age"], df["data usage"])

plt.grid(True)
plt.show()