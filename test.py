import akshare as ak
import pandas as pd
import numpy as np

print(f'pandas version: {pd.__version__}')
print(f'akshare version: {ak.__version__}')

# 单支基金

# 易方达蓝筹精选， 005827
# 前海开源公共事业股票 005669

years = ['2019', '2020', '2021']

data = pd.DataFrame()
for yr in years:
    df_tmp = ak.fund_portfolio_hold_em(symbol='005827', date=yr)
    data = data.append(df_tmp)

data['季度'] = data['季度'].apply(lambda x:x[:6])
data['季度'] = data['季度'].str.replace('年', 'Q')
data['占净值比例'] = pd.to_numeric(data['占净值比例'])

print(data)
