import pandas as pd
data = [111, 112, 234]
series = pd.Series(data, index["a", "b", "c"])
print(series.loc["a"])
