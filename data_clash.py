# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:06:44 2018

@author: Administrator
"""
#label drop 收缩压or舒张压：弃查  未查  轻度乳糜  ++ +   >
import pandas as pd
import numpy as np
data_history=pd.read_csv('tmp.csv',encoding='utf-8',low_memory=False)
train_vid=pd.read_csv('meinian_round1_train_20180408.csv',encoding='gbk',usecols=['vid'])
test_data=pd.read_csv('meinian_round1_test_a_20180408.csv',encoding='gbk',usecols=['vid'])
train_label=pd.read_csv('meinian_round1_train_20180408.csv',encoding='gbk',usecols=[1,2,3,4,5])
#对label进行清洗
def how_clean_label(x):
    x=str(x)
    if '+' in x:
        i=x.index('+')
        x=x[0:i]
    if '>' in x:
        i=x.index('>')
        x=x[i+1:]
    if len(x.split(sep='.'))>2:
        i=x.rindex('.')
        x=x[0:i]+x[i+1:]
    if '轻' in x:
        i=x.index('轻')
        x=x[0:i]
    if '未查' in x or '弃查' in x or '未做' in x:
        x=np.nan
    if str(x).isdigit()==False and len(str(x))>4:
        x=x[0:4]
    if float(x)>500:
        x=np.nan
    if float(x)<=0:
        x=np.nan
    return x
def clean_label(df):
    for c in ['收缩压','舒张压','血清甘油三酯','血清高密度脂蛋白','血清低密度脂蛋白']:
        df[c]=df[c].apply(how_clean_label)
        df[c]=df[c].astype('float64')
    return df
train_label=clean_label(train_label)



train_data=pd.concat([train_vid,train_label],axis=1)
train_data.dropna(axis=0,inplace=True)
train_vid=train_data['vid']
train_vid=pd.DataFrame(train_vid)
#data_history.dropna(axis=1,how='all',inplace=True)
#data_history_vid=data_history['vid']



def fun():
    feat_name=data_history.columns
    feat_name=np.array(feat_name)
    for i in feat_name:
        if(i=='vid'):
            continue
        if(len(data_history[data_history[i].isnull()]['vid'])<56000 or len(data_history[data_history[i].isnull()]['vid'])>57000):
            del data_history[i]

fun()
data_history.to_csv('data_history_feat_clash8_5_5_19_33.csv',index=False)
