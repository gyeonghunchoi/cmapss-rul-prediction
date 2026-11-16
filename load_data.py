import pandas as pd
df = pd.read_csv("data/CMAPSSData/train_FD001.txt", sep=r"\s+", header=None)
print(df.shape)
columns = ["unit", "cycle", "os1", "os2", "os3"]
for i in range(1,22):
    columns.append(f"s{i}")
print(len(columns))
df.columns = columns
print(df.head())
print(df["unit"].max())
print(df["cycle"].max())
print(df.describe().T["std"])