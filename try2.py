import yfinance as yf
import numpy as np

df = yf.download('^GSPC',start='2010-01-01')
df ['returns'] = np.log(df.Close.pct_change()+1)
def lagit(df, lags):
    names = []
    for i in range(1,lags +1):
        df['Lag_'+str()] =df['returns'].shift(i)
        names.append('Lag_'+str(i))
    return names
lagnames = lagit(df,5)    
lagnames
['Lag_1','Lag_2','Lag_3','Lag_4','Lag_5']
df

