import pandas as pd
df=pd.read_csv("data/CMAPSSData/train_FD001.txt", sep=r"\s+", header=None)
print(df.shape)
print(df.head())
