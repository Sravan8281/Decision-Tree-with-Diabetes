import pandas as pd 
accno=[123,124,125,126,127,128]
ser=pd.Series(accno)
print(ser)
print(pd.__version__)
# series from dictionary
# {key : values}  - key index
temp_dict ={'London' : 14, 'scotland':12 ,'liverpool':11 }
temp_series=pd.Series(temp_dict)
print(temp_series)
import numpy as np
import seaborn as sns
import matplotlib as plt 