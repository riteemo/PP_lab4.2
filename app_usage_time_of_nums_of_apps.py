import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("user_behavior_dataset.csv")
data = dataframe[["App Usage Time (min/day)", "Number of Apps Installed"]]
app = data["Number of Apps Installed"].sort_values().unique()
dct = {"app time": [], "num": []}
for a in app:
    res = data[data["Number of Apps Installed"] == a]
    dct["num"].append(a)
    dct["app time"].append(res["App Usage Time (min/day)"].mean())

df = pd.DataFrame(dct)
plt.xlabel('Количество установленных приложений')
plt.ylabel('Экранное время в приложениях (мин/день)')

plt.plot(df["num"], df["app time"])
plt.grid(True)
plt.show()

# надо доказать: с ростом числа приложений растет количество экранного времении
# нулевая гипотеза: с ростом числа приложений количество экранного времени не меняется
# альтернативная гипотеза: с ростом числа приложений количество экранного времени меняется
differences = []
num_of_apps = df["num"].sort_values()
app_time = df["app time"]

# проверка на нулевую гипотезу (проверим, что для каждого числа приложений экранное время отличается незначительно)
for i in range(1, len(num_of_apps)):
    print(f"{num_of_apps[i - 1]} apps and {num_of_apps[i]} apps: {app_time[i - 1] - app_time[i]}")
    differences.append(app_time[i - 1] - app_time[i])

print(sum(differences)) # сумма разниц отрицательна, следовательно - в большинстве каждая разность A(i) - A(i + 1) отрицательно,
# что означает, что при росте числа приложений экранное время увиличивается