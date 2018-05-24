import pandas as pd
import numpy as np

test_id=pd.read_csv('meinian_round1_test_a_20180408.csv',encoding='gbk')
train_data=pd.read_csv('train_data.csv')
data_history=pd.read_csv('data_history_4_21_17_51.csv')
data_history_vid=pd.read_csv('data_history_4_21_17_51.csv',usecols=['vid'])
###############################################################################################################
def get_num_status5(x):
    try:
        if((x.count('正常')>0) or (x.count('未')>0) or  (x.count('有力')>0) or (x.count('未见明显占位性病变')>0)):
            return 1
        if((x.count('弱')>0)):
            return 2
        if ((x.count('强') > 0)):
            return 3
        if ((x.count('右位心') > 0)):
            return 4
        if ((x.count('分裂') > 0)):
            return 5
        if ((x.count('心音遥远') > 0)):
            return 6
        else:
            return 1
    except:
        return 1
data_history['heart_voice_'] = data_history['0420'].map(lambda x: get_num_status5(x))
del data_history['0420']
#########################################################################################
def get_num_status6(x):
    try:
        if((x.count('血压')>0) and (x.count('高')>0) ):
            return 1
        else:
            return 0
    except:
        return 0
data_history['xueyaya_'] = data_history['0434'].map(lambda x: get_num_status6(x))
#############################################################################################
def get_num_status7(x):
    try:
        if((x.count('血脂')>0) and (x.count('高')>0) ):
            return 1
        else:
            return 0
    except:
        return 0
data_history['xuezhizhi_'] = data_history['0434'].map(lambda x: get_num_status7(x))
#################################################################################################
def get_num_status8(x):
    try:
        if((x.count('糖尿病')>0)):
            return 1
        else:
            return 0
    except:
        return 0
data_history['tt_'] = data_history['0434'].map(lambda x: get_num_status8(x))
del data_history['0434']
################################################################################################
def get_num_status9(x):
    try:
        if( (x.count('未见异常')>0)or (x.count('正常')>0)):
            return 1
        if((x.count('未触及')>0)):
            return 2
        if((x.count('软')>0)):
            return 3
        if ((x.count('中') > 0)):
            return 4
        if ((x.count('硬') > 0)):
            return 5
    except:
        return 1
data_history['zezeze_'] = data_history['0430'].map(lambda x: get_num_status9(x))
del data_history['0430']
########################################################################################################
def get_num_status10(x):
    try:
        if( (x.count('未见异常')>0)or (x.count('正常')>0)):
            return 1
        if((x.count('压痛')>0)):
            return 2
        if((x.count('叩击痛')>0)):
            return 3
        if ((x.count('未触及') > 0) or (x.count('无') > 0)):
            return 4
    except:
        return 1
data_history['ayaya_'] = data_history['0431'].map(lambda x: get_num_status10(x))
del data_history['0431']
##################################################################################################
def feat_combine():
    a=pd.get_dummies(data_history['heart_voice_'],prefix='heart_voice_')
    b=pd.get_dummies(data_history['xueyaya_'],prefix='xueyaya_')
    c=pd.get_dummies(data_history['tt_'],prefix='tt_')
    d=pd.get_dummies(data_history['zezeze_'],prefix='zezeze_')
    e=pd.get_dummies(data_history['ayaya_'],prefix='ayaya_')
    feat_now=pd.concat([data_history_vid,a,b,c,d,e],axis=1)
    return feat_now
feat_now=feat_combine()
feat_now.to_csv('feat_second_history_4_21_19_23.csv',index=False)