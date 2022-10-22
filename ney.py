import pandas as pd
import numpy as np

ney = pd.read_csv('https://raw.githubusercontent.com/cristiandarioortegayubro/base/main/dataset/neymar.csv')

# change dtypes
ney['Tournament'] = ney['Tournament'].astype('string')
ney['Matchday'] = ney['Matchday'].astype('string')
ney['Date'] = ney['Date'].astype('datetime64[ns]')
ney['Venue'] = ney['Venue'].astype('string')
ney['Club'] = ney['Club'].astype('string')
ney['Opponent'] = ney['Opponent'].astype('string')
ney['Result'] = ney['Result'].astype('string')
ney['Position'] = ney['Position'].astype('string')
ney['Minute'] = ney['Minute'].astype('string')
ney['When Scored'] = ney['When Scored'].astype('string')
ney['Goal Type'] = ney['Goal Type'].astype('string')
ney['Assist'] = ney['Assist'].astype('string')

print(ney.dtypes)