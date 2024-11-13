import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("user_behavior_dataset.csv")
data = dataframe[["Screen On Time (hours/day)", "Gender"]]
genders = data["Gender"].sort_values().unique()
dct = {"gender": [], "screen on time": []}
for gender in genders:
    res = data[data["Gender"] == gender]
    dct["gender"].append(gender)
    dct["screen on time"].append(res["Screen On Time (hours/day)"].mean())

print(dct)
df = pd.DataFrame(dct)
print(df.columns)
plt.xlabel('Пол')
plt.ylabel('Экранное время в часах')
plt.ylim(5.2, 5.3)
plt.bar(df["gender"], df["screen on time"])

plt.grid(True)
plt.show()