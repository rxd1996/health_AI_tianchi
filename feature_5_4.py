import pandas as pd
import numpy as np
old_feature=pd.read_csv('feat_history_5_4_16_20.csv',low_memory=False)
data_history_5_4=pd.read_csv('data_history_feat_clash8_5_4_18_52.csv',low_memory=False)
#, '004997', '0213', '0415', '0439', '0546', '0732', '100012',
 #      '100013', '10009', '1110', '1112', '1319', '1320', '1844', '20002',
  #     '2177', '2376', '2386', '2409', '279006', '300001', '300007', '300008',
   #    '300009', '300011', '300012', '300013', '300014', '300068', '300074',
    #   '300076', '300092', '300131', '3101', '3813', '669003', '669004',
     #  '669005', '669007', '669008', '669009', '669021', '809003', '809004',
      # '809008', '809010', '809013', '809017', '809018', '809019', '809021',
       #'809022', '809023', '809025', '809026', '809027', '809037', '809038',
       ##'809039', '809040', '809041', '809042', '809043', '809044', '809045',
       #'809046', '809047', '809048', '809049', '809050', '809051', '809052',
       #'809053', '809054', '809055', '809056', '809057', '809058', '809059',
       #'809060', '809061', 'A705'],
def get_feat_100012(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('4.3.')):
            return 4.3
        if(x.count('.45.21')):
            return 45.21
        if(x.count('6.31.0.45')):
            return 6.31
        if(x.count('<0.8')):
            return 0.8
        if(x.count('<2.00')):
            return 2.00
        if(x.count('<0.6')):
            return 0.6
        if(x.count('<0.003')):
            return 0.003
        if(x.count('2.70.')):
            return 2.70
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_4['feat_100012']=data_history_5_4['100012'].map(lambda x:get_feat_100012(x))
data_history_5_4['feat_100013']=data_history_5_4['100013'].map(lambda x:get_feat_100012(x))
data_history_5_4['feat_10009']=data_history_5_4['10009'].map(lambda x:get_feat_100012(x))
def get_feat_1110(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('4.3.')):
            return 4.3
        if(x.count('<1')):
            return 0.99
        if(x.count('<0.050')):
            return 0.049
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_4['feat_1110'] = data_history_5_4['1110'].map(lambda x: get_feat_1110(x))
data_history_5_4['feat_1112'] = data_history_5_4['1112'].map(lambda x: get_feat_1110(x))
def get_feat_1319(x):
    try:
        x=float(x)
        if(x>100):
            return 16.14
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count('m')):
            i = x.index('m')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('正常') or x.count('无法检查')):
            return np.nan
        if(x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if (x.count(' ')):
            i = x.index(' ')
            x = x[i+1:]
            x = float(x)
            return x
        if(x.count('眼压偏高')):
            return 25
        if(x.count('压高可疑')):
            return 25
      #      return 4.3
      #  if(x.count('<1')):
       #     return 0.99
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_4['feat_1319'] = data_history_5_4['1319'].map(lambda x: get_feat_1319(x))
b=data_history_5_4['feat_1319']
b=pd.DataFrame(b)
data_history_5_4['feat_1319']=b.fillna(b.mean())

data_history_5_4['feat_1320'] = data_history_5_4['1320'].map(lambda x: get_feat_1319(x))
b=data_history_5_4['feat_1320']
b=pd.DataFrame(b)
data_history_5_4['feat_1320']=b.fillna(b.mean())

data_history_5_4['feat_1844'] = data_history_5_4['1844'].map(lambda x: get_feat_1110(x))
data_history_5_4['feat_20002'] = data_history_5_4['20002'].map(lambda x: get_feat_1110(x))
data_history_5_4['feat_2386'] = data_history_5_4['2386'].map(lambda x: get_feat_1110(x))

def get_feat_1110(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('>20')):
            return 25
        if (x.count('>40')):
            return 45
        if (x.count('+')):
            return 28
        if(x.count('<7.0')):
            return 6.9
        if(x.count('<20')):
            return 19.9
        if(x.count('<1')):
            return 10
        return np.nan


data_history_5_4['feat_2177'] = data_history_5_4['2177'].map(lambda x: get_feat_1110(x))
def get_feat_1110(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('<200')):
            return 190
        if (x.count('<20')):
            return 19
        if (x.count('<4')):
            return 3.9
        if(x.count('<50')):
            return 49
        if(x.count('>201')):
            return 202
        if(x.count('+')):
            return 548
        return np.nan

data_history_5_4['feat_2376'] = data_history_5_4['2376'].map(lambda x: get_feat_1110(x))
def get_feat_2409(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('%')==2):
            i=x.index('%')
            x=x[:i]
            x=float(x)
            return x
        if (x.count('%') == 1):
            i = x.index('(')
            x = x[:i]
            x = float(x)
            return x
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        #if(x.count('4.3.')):
         #   return 4.3
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan

data_history_5_4['feat_2409'] = data_history_5_4['2409'].map(lambda x: get_feat_2409(x))
##################################################################################################################
#, '004997', '0213', '0415', '0439', '0546', '0732', '100012',
 #      '100013', '10009', '1110', '1112', '1319', '1320', '1844', '20002',
  #     '2177', '2376', '2386', '2409', '279006', '300001', '300007', '300008',
   #    '300009', '300011', '300012', '300013', '300014', '300068', '300074',
    #   '300076', '300092', '300131', '3101', '3813', '669003', '669004',
     #  '669005', '669007', '669008', '669009', '669021', '809003', '809004',
      # '809008', '809010', '809013', '809017', '809018', '809019', '809021',
       #'809022', '809023', '809025', '809026', '809027', '809037', '809038',
       ##'809039', '809040', '809041', '809042', '809043', '809044', '809045',
       #'809046', '809047', '809048', '809049', '809050', '809051', '809052',
       #'809053', '809054', '809055', '809056', '809057', '809058', '809059',
       #'809060', '809061', 'A705'],

data_history_5_4['feat_300001'] = data_history_5_4['300001'].map(lambda x: get_feat_100012(x))

data_history_5_4['feat_300007'] = data_history_5_4['300007'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300008'] = data_history_5_4['300008'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300009'] = data_history_5_4['300009'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300011'] = data_history_5_4['300011'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300012'] = data_history_5_4['300012'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300013'] = data_history_5_4['300013'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300014'] = data_history_5_4['300014'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300068'] = data_history_5_4['300068'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300074'] = data_history_5_4['300074'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300076'] = data_history_5_4['300076'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_300092'] = data_history_5_4['300092'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_669003'] = data_history_5_4['669003'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_669008'] = data_history_5_4['669008'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_669009'] = data_history_5_4['669009'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_669021'] = data_history_5_4['669021'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_809003'] = data_history_5_4['809003'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_809004'] = data_history_5_4['809004'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_809021'] = data_history_5_4['809021'].map(lambda x: get_feat_100012(x))
data_history_5_4['feat_809025'] = data_history_5_4['809025'].map(lambda x: get_feat_100012(x))

def get_feat_A705(x):
    try:
        if(x.count('脂肪')):
            return 1
        else:
            return 0
    except:
         return 0

data_history_5_4['feat_A705']=data_history_5_4['A705'].map(lambda x:get_feat_A705(x))

#data_history_5_4[data_history_5_4['feat_A705']==0]['A705'].unique()
def feat_combine():
    a=pd.get_dummies(data_history_5_4['feat_A705'],prefix='feat_A705__')
    feat_now=pd.concat([old_feature,data_history_5_4['feat_100012'],data_history_5_4['feat_100013'],data_history_5_4['feat_10009'],data_history_5_4['feat_1110'],
                        data_history_5_4['feat_1112'],data_history_5_4['feat_1319'],data_history_5_4['feat_1320'],data_history_5_4['feat_1844'],
                        data_history_5_4['feat_20002'],data_history_5_4['feat_2177'],data_history_5_4['feat_2376'],data_history_5_4['feat_2386'],
                        data_history_5_4['feat_2409'],data_history_5_4['feat_300001'],data_history_5_4['feat_300007'],data_history_5_4['feat_300008'],
                        data_history_5_4['feat_300009'],data_history_5_4['feat_300011'],data_history_5_4['feat_300012'],data_history_5_4['feat_300013'],
                        data_history_5_4['feat_300014'],data_history_5_4['feat_300068'],data_history_5_4['feat_300074'],data_history_5_4['feat_300076'],
                        data_history_5_4['feat_300092'],data_history_5_4['feat_669003'],data_history_5_4['feat_669008'],data_history_5_4['feat_669009'],
                        data_history_5_4['feat_669021'],data_history_5_4['feat_809003'],data_history_5_4['feat_809004'],data_history_5_4['feat_809021'],
                        data_history_5_4['feat_809025'],a],axis=1)
    return feat_now
feat_now=feat_combine()
feat_now.to_csv('feat_history_5_5_00_00.csv',index=False)