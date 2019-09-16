import pandas as pd
import requests

def api(method='get',endpoint='info',options='',ip='localhost',port=19999,version='v1/',return_json=True):
    ''' Function to wrap calls to the netdata api.
    '''
    # build request url
    base=f'http://{ip}:{port}/api/'
    request_url = f'{base}{version}{endpoint}{options}'
    # make request according to method specified
    if method == 'get':
        response = requests.get(request_url)
    else:
        raise ValueError(f'... unsupported method ({method}) ...')
    if return_json:
        ret = response.json()
    else:
        ret = response
    return ret

def get_metrics(metrics=['system.cpu'],n_points=10,after=-600,before=0,options='seconds,jsonwrap',format='json',ip='localhost',add_timestamp=True):
    ''' Function to get a long df of metric values from the api.
    '''
    # make empty dataframe
    df = pd.DataFrame()
    for metric in metrics:
        response_json = api(
            ip=ip,
            endpoint='data',
            options=f'?chart={metric}&after={after}&before={before}&points={n_points}&group=average&gtime=0&format={format}&options={options}'
        )
        df_tmp = pd.DataFrame(data=response_json['result']['data'],columns=response_json['result']['labels'])
        df_tmp.columns = ['time_idx'] + list(df_tmp.columns[1:])
        df_tmp['name'] = response_json['name']
        obj_cols = df_tmp.select_dtypes(include='O').columns
        df_tmp['key'] = df_tmp[obj_cols].fillna('').astype(str).values.sum(axis=1)
        df_tmp = df_tmp.drop(columns=obj_cols)
        df_tmp = df_tmp.melt(id_vars=['time_idx','key'],var_name='label')
        df = df.append(df_tmp)
    if add_timestamp:
        df['timestamp'] = pd.to_datetime(df['time_idx'],unit='s')
        del df['time_idx']
    df = df[['timestamp','key','label','value']]
    return df