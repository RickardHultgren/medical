from datetime import datetime
#from pandas import *
import pandas as pd
start = datetime(2023, 8, 28)
end = datetime(2023, 11, 15)
index1 = pd.date_range(start, end, freq='B').strftime("%Y-%m-%d").tolist()
#print(index1)
print("\n".join(index1))