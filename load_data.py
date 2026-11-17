import pandas as pd
df = pd.read_csv("data/CMAPSSData/train_FD001.txt", sep=r"\s+", header=None)
columns = ["unit", "cycle", "os1", "os2", "os3"]
for i in range(1,22):
    columns.append(f"s{i}")
df.columns = columns
df["max_cycle"] = df.groupby("unit")["cycle"].transform("max")
df["RUL"] = df["max_cycle"] - df["cycle"]
df = df.drop(columns=["max_cycle"])
print(df[["unit", "cycle", "RUL"]].head())
print(df[["unit", "cycle", "RUL"]].tail())