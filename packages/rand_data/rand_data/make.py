import numpy as np
import pandas as pd

def make_data(shape=(1000,5),rand_range=(0,100),anom_len=250,anom_range=(500,510)):
    data = np.random.randint(rand_range[0],rand_range[1],size=shape)
    df = pd.DataFrame(data,columns=[f'col_{n}'for n in range(shape[1])])
    if anom_len > 0:
        df['is_anom'] = 0 
        data_anom = np.random.randint(anom_range[0],anom_range[1],size=(anom_len,shape[1]))
        df_anom = pd.DataFrame(data_anom,columns=[f'col_{n}'for n in range(shape[1])])
        df_anom['is_anom'] = 1
        df = df.append(df_anom)
    return df