cycles=[3,4,5,6,7]
rul=[]
max_cycles=max(cycles)
for i in cycles:
    rul.append(max_cycles-i)
print(rul)

import pandas, matplotlib
print(pandas.__version__, matplotlib.__version__)