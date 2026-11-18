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
sensor = "s2"
plt.plot(engine1["cycle"], engine1[sensor])
plt.xlabel("cycle")
plt.ylabel(sensor)
plt.title(f"Engine 1 - cycle - {sensor}")
plt.savefig(f"figures/engine1_{sensor}.png")
plt.show()