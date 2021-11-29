import pandas as pd
from pathlib import Path
from match import *

path = Path("database")
def verify(vid,passw):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Passw','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid and match(str(df['Passw'].iloc[index]),str(passw))==True:
            return True
    return False


def isEligible(vid):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','City','Passw','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==10003 and df['hasVoted'].iloc[index]==0:
            return True
    return False

a=verify(10002,'101_1.tif')
print(a)
