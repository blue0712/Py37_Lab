import pandas as pd
from pandas_datareader import data, wb

data = wb.download(indicator='SE.PRM.TENR',
                   country=['all'],
                   start='2002',
                   end='2017')
print(type(data), data.shape)
print(data.head())