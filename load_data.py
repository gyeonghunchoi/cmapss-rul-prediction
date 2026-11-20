import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/CMAPSSData/train_FD001.txt", sep=r"\s+", header=None)
columns = ["unit", "cycle", "os1", "os2", "os3"]
for i in range(1,22):
    columns.append(f"s{i}")
df.columns = columns
df["max_cycle"] = df.groupby("unit")["cycle"].transform("max")
df["RUL"] = df["max_cycle"] - df["cycle"]
df = df.drop(columns=["max_cycle"])
engine1 = df[df["unit"] == 1]

fig, axes = plt.subplots(7, 3, figsize=(15,20))
axes = axes.flatten()

for i in range(0, 21):
    sensor = f"s{i+1}"
    axes[i].plot(engine1["cycle"], engine1[sensor])
    axes[i].set_title(sensor)

plt.tight_layout()
plt.savefig("figures/engine1_all_sensors.png")