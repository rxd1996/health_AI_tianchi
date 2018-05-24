import pandas as pd
import numpy as np
feature_old=pd.read_csv('feat_history_5_2_21_09.csv',low_memory=False)
data_history_5_3=pd.read_csv('data_history_feat_clash7_5_2_19_52.csv',low_memory=False)
#data_history_vid=pd.read_csv('data_history_feat_clash7_5_2_19_52.csv',usecols=['vid'])
#(['vid', '0225', '0414', '0428', '0436', '0440', '0981', '0982', '0983',
     #  '0984', '0987', '100014', '1106', '1107', '1127', '1325', '1326',
      # '1330', '139', '1402', '143', '1474', '269003', '269005', '269006',
      # '269007', '269008', '269009', '269010', '269011', '269012', '269014',
      # '269016', '269017', '269019', '300017', '300018', '300019', '300021',
      # '360', '669001', '669002', '669006', '809001', '809009', '979001',
      # '979002', '979003', '979004', '979005', '979006', '979007', '979008',
      # '979009', '979011', '979012', '979013', '979014', '979015', '979016',
      # '979017', '979018', '979019', '979020', '979021', '979022', '979023',
      # 'A301', 'A302'],
      #dtype='object')
def get_feat_100014(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
     #   if(x==0):
      #      return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('.')==2):
            return 20.908
        if(x.count('>')):
            return 100.00
        return np.nan
data_history_5_3['feat_100014']=data_history_5_3['100014'].map(lambda x:get_feat_100014(x))
#data_history_5_3[data_history_5_3['feat_100014'].isnull()]['100014'].unique()
b=data_history_5_3['feat_100014']
b=pd.DataFrame(b)
data_history_5_3['feat_100014']=b.fillna(b.mean())
del data_history_5_3['100014']
##########################################################################################################################
def get_feat_1106(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
     #   if(x==0):
      #      return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('1..75')):
            return 1.75
        if(x.count('1.81.')):
            return 1.81
        return np.nan
data_history_5_3['feat_1106']=data_history_5_3['1106'].map(lambda x:get_feat_1106(x))
#data_history_5_3[data_history_5_3['feat_1106'].isnull()]['1106'].unique()
b=data_history_5_3['feat_1106']
b=pd.DataFrame(b)
data_history_5_3['feat_1106']=b.fillna(b.mean())
del data_history_5_3['1106']
######################################################################################################################
def get_feat_1107(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
        if(x==0):
            return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
     #   if(x.count('1..75')):
     #       return 1.75
     #   if(x.count('1.81.')):
     #       return 1.81
        return np.nan
data_history_5_3['feat_1107']=data_history_5_3['1107'].map(lambda x:get_feat_1107(x))
#data_history_5_3[data_history_5_3['feat_1107'].isnull()]['1107'].unique()
b=data_history_5_3['feat_1107']
b=pd.DataFrame(b)
data_history_5_3['feat_1107']=b.fillna(b.mean())
del data_history_5_3['1107']
###########################################################################################################################
def get_feat_1127(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
     #   if(x.count('1..75')):
     #       return 1.75
     #   if(x.count('1.81.')):
     #       return 1.81
        return np.nan
data_history_5_3['feat_1127']=data_history_5_3['1127'].map(lambda x:get_feat_1127(x))
#data_history_5_3[data_history_5_3['feat_1127'].isnull()]['1127'].unique()
b=data_history_5_3['feat_1127']
b=pd.DataFrame(b)
data_history_5_3['feat_1127']=b.fillna(b.mean())
del data_history_5_3['1127']
########################################################################################################################
def get_feat_139(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('<0.30')):
            return 0.3
     #   if(x.count('1.81.')):
     #       return 1.81
        return np.nan
data_history_5_3['feat_139']=data_history_5_3['139'].map(lambda x:get_feat_139(x))
#data_history_5_3[data_history_5_3['feat_139'].isnull()]['139'].unique()
b=data_history_5_3['feat_139']
b=pd.DataFrame(b)
data_history_5_3['feat_139']=b.fillna(b.mean())
del data_history_5_3['139']
##################################################################################################################
def get_feat_143(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('>5')):
            return 50.2
        if(x.count('>100')):
            return 100
        return np.nan
data_history_5_3['feat_143']=data_history_5_3['143'].map(lambda x:get_feat_143(x))
#data_history_5_3[data_history_5_3['feat_143'].isnull()]['143'].unique()
b=data_history_5_3['feat_143']
b=pd.DataFrame(b)
data_history_5_3['feat_143']=b.fillna(b.mean())
del data_history_5_3['143']
###########################################################################################################################################
def get_feat_1474(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
      #  if(x.count('>5')):
       #     return 50.2
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_1474']=data_history_5_3['1474'].map(lambda x:get_feat_1474(x))
#data_history_5_3[data_history_5_3['feat_1474'].isnull()]['1474'].unique()
b=data_history_5_3['feat_1474']
b=pd.DataFrame(b)
data_history_5_3['feat_1474']=b.fillna(b.mean())
del data_history_5_3['1474']
##############################################################################################################################################
def get_feat_269003(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('14.4.')):
            return 14.4
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269003']=data_history_5_3['269003'].map(lambda x:get_feat_269003(x))
#data_history_5_3[data_history_5_3['feat_269003'].isnull()]['269003'].unique()
b=data_history_5_3['feat_269003']
b=pd.DataFrame(b)
data_history_5_3['feat_269003']=b.fillna(b.mean())
del data_history_5_3['269003']
#####################################################################################################################
def get_feat_269005(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
      #  if(x.count('14.4.')):
       #     return 14.4
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269005']=data_history_5_3['269005'].map(lambda x:get_feat_269005(x))
#data_history_5_3[data_history_5_3['feat_269005'].isnull()]['269005'].unique()
b=data_history_5_3['feat_269005']
b=pd.DataFrame(b)
data_history_5_3['feat_269005']=b.fillna(b.mean())
del data_history_5_3['269005']
#####################################################################################################################################
def get_feat_269006(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('126.0.')):
            return 126.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269006']=data_history_5_3['269006'].map(lambda x:get_feat_269006(x))
#data_history_5_3[data_history_5_3['feat_269006'].isnull()]['269006'].unique()
b=data_history_5_3['feat_269006']
b=pd.DataFrame(b)
data_history_5_3['feat_269006']=b.fillna(b.mean())
del data_history_5_3['269006']
########################################################################################################################
def get_feat_269007(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('126.0.')):
     #       return 126.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269007']=data_history_5_3['269007'].map(lambda x:get_feat_269007(x))
#data_history_5_3[data_history_5_3['feat_269007'].isnull()]['269007'].unique()
b=data_history_5_3['feat_269007']
b=pd.DataFrame(b)
data_history_5_3['feat_269007']=b.fillna(b.mean())
del data_history_5_3['269007']
#############################################################################################################################
def get_feat_269008(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('126.0.')):
     #       return 126.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269008']=data_history_5_3['269008'].map(lambda x:get_feat_269008(x))
#data_history_5_3[data_history_5_3['feat_269008'].isnull()]['269008'].unique()
b=data_history_5_3['feat_269008']
b=pd.DataFrame(b)
data_history_5_3['feat_269008']=b.fillna(b.mean())
del data_history_5_3['269008']
#############################################################################################################################
def get_feat_269009(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('126.0.')):
     #       return 126.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269009']=data_history_5_3['269009'].map(lambda x:get_feat_269009(x))
#data_history_5_3[data_history_5_3['feat_269009'].isnull()]['269009'].unique()
b=data_history_5_3['feat_269009']
b=pd.DataFrame(b)
data_history_5_3['feat_269009']=b.fillna(b.mean())
del data_history_5_3['269009']
####################################################################################################################################
def get_feat_269010(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('126.0.')):
     #       return 126.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269010']=data_history_5_3['269010'].map(lambda x:get_feat_269010(x))
#data_history_5_3[data_history_5_3['feat_269010'].isnull()]['269010'].unique()
b=data_history_5_3['feat_269010']
b=pd.DataFrame(b)
data_history_5_3['feat_269010']=b.fillna(b.mean())
del data_history_5_3['269010']
####################################################################################################################################
def get_feat_269011(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('126.0.')):
     #       return 126.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269011']=data_history_5_3['269011'].map(lambda x:get_feat_269011(x))
#data_history_5_3[data_history_5_3['feat_269011'].isnull()]['269011'].unique()
b=data_history_5_3['feat_269011']
b=pd.DataFrame(b)
data_history_5_3['feat_269011']=b.fillna(b.mean())
del data_history_5_3['269011']
##############################################################################################################################
def get_feat_269012(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('116.0.')):
            return 116.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269012']=data_history_5_3['269012'].map(lambda x:get_feat_269012(x))
#data_history_5_3[data_history_5_3['feat_269012'].isnull()]['269012'].unique()
b=data_history_5_3['feat_269012']
b=pd.DataFrame(b)
data_history_5_3['feat_269012']=b.fillna(b.mean())
del data_history_5_3['269012']
#################################################################################################################################
def get_feat_269014(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('116.0.')):
     #       return 116.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269014']=data_history_5_3['269014'].map(lambda x:get_feat_269014(x))
#data_history_5_3[data_history_5_3['feat_269014'].isnull()]['269014'].unique()
b=data_history_5_3['feat_269014']
b=pd.DataFrame(b)
data_history_5_3['feat_269014']=b.fillna(b.mean())
del data_history_5_3['269014']
###########################################################################################################
def get_feat_269016(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('116.0.')):
     #       return 116.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269016']=data_history_5_3['269016'].map(lambda x:get_feat_269016(x))
#data_history_5_3[data_history_5_3['feat_269016'].isnull()]['269016'].unique()
b=data_history_5_3['feat_269016']
b=pd.DataFrame(b)
data_history_5_3['feat_269016']=b.fillna(b.mean())
del data_history_5_3['269016']
###############################################################################################################################
#(['vid', '0225', '0414', '0428', '0436', '0440', '0981', '0982', '0983',
     #  '0984', '0987', '100014', '1106', '1107', '1127', '1325', '1326',
      # '1330', '139', '1402', '143', '1474', '269003', '269005', '269006',
      # '269007', '269008', '269009', '269010', '269011', '269012', '269014',
      # '269016', '269017', '269019', '300017', '300018', '300019', '300021',
      # '360', '669001', '669002', '669006', '809001', '809009', '979001',
      # '979002', '979003', '979004', '979005', '979006', '979007', '979008',
      # '979009', '979011', '979012', '979013', '979014', '979015', '979016',
      # '979017', '979018', '979019', '979020', '979021', '979022', '979023',
      # 'A301', 'A302'],
def get_feat_269017(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('116.0.')):
     #       return 116.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269017']=data_history_5_3['269017'].map(lambda x:get_feat_269017(x))
#data_history_5_3[data_history_5_3['feat_269017'].isnull()]['269017'].unique()
b=data_history_5_3['feat_269017']
b=pd.DataFrame(b)
data_history_5_3['feat_269017']=b.fillna(b.mean())
del data_history_5_3['269017']
#########################################################################
def get_feat_269019(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('116.0.')):
     #       return 116.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_269019']=data_history_5_3['269019'].map(lambda x:get_feat_269019(x))
#data_history_5_3[data_history_5_3['feat_269019'].isnull()]['269019'].unique()
b=data_history_5_3['feat_269019']
b=pd.DataFrame(b)
data_history_5_3['feat_269019']=b.fillna(b.mean())
del data_history_5_3['269019']
#######################################################################################################################
def get_feat_300017(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('阴性1.496')):
            return 1.496
        if(x.count('<')):
            return 0.003
        if(x.count('阳') or x.count('+')):
            return 21
        return np.nan
data_history_5_3['feat_300017']=data_history_5_3['300017'].map(lambda x:get_feat_300017(x))
#data_history_5_3[data_history_5_3['feat_300017'].isnull()]['300017'].unique()
b=data_history_5_3['feat_300017']
b=pd.DataFrame(b)
data_history_5_3['feat_300017']=b.fillna(b.mean())
del data_history_5_3['300017']
###################################################################################################################
def get_feat_300018(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('阴性') or x.count('-')):
            return np.nan
        if (x.count(' ')):
            i = x.index(' ')
    #       #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
      #  if(x.count('阴性1.496')):
       #     return 1.496
       # if(x.count('<')):
      #      return 0.003
        if(x.count('阳') or x.count('+')):
            return 11
        return np.nan
data_history_5_3['feat_300018']=data_history_5_3['300018'].map(lambda x:get_feat_300018(x))
#data_history_5_3[data_history_5_3['feat_300018'].isnull()]['300018'].unique()
b=data_history_5_3['feat_300018']
b=pd.DataFrame(b)
data_history_5_3['feat_300018']=b.fillna(b.mean())
del data_history_5_3['300018']
###############################################################################################
def get_feat_300019(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('阴性') or x.count('-')):
            return np.nan
        if (x.count(' ')):
            i = x.index(' ')
    #       #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
      #  if(x.count('阴性1.496')):
       #     return 1.496
        if(x.count('<')):
            return 5
        if(x.count('阳') or x.count('+')):
            return 10
        return np.nan
data_history_5_3['feat_300019']=data_history_5_3['300019'].map(lambda x:get_feat_300019(x))
#data_history_5_3[data_history_5_3['feat_300019'].isnull()]['300019'].unique()
b=data_history_5_3['feat_300019']
b=pd.DataFrame(b)
data_history_5_3['feat_300019']=b.fillna(b.mean())
del data_history_5_3['300019']
###########################################################################################
def get_feat_300021(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('阴性') or x.count('-')):
            return np.nan
        if (x.count('<0.60')):
            return 0.55
        if(x.count('<2')):
            return 1.95
        if(x.count('<3.4')):
            return 3.36
        if(x.count('<')):
            return 0.95
        if (x.count(' ')):
            i = x.index(' ')
    #       #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
      #  if(x.count('阴性1.496')):
       #     return 1.496
    #    if(x.count('阳') or x.count('+')):
     #       return 10
        return np.nan
data_history_5_3['feat_300021']=data_history_5_3['300021'].map(lambda x:get_feat_300021(x))
#data_history_5_3[data_history_5_3['feat_300021'].isnull()]['300021'].unique()
b=data_history_5_3['feat_300021']
b=pd.DataFrame(b)
data_history_5_3['feat_300021']=b.fillna(b.mean())
del data_history_5_3['300021']
###############################################################################
def get_feat_669001(x):
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
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('116.0.')):
     #       return 116.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_669001']=data_history_5_3['669001'].map(lambda x:get_feat_669001(x))
#data_history_5_3[data_history_5_3['feat_669001'].isnull()]['669001'].unique()
b=data_history_5_3['feat_669001']
b=pd.DataFrame(b)
data_history_5_3['feat_669001']=b.fillna(b.mean())
del data_history_5_3['669001']
#######################################################################################################################
#(['vid', '0225', '0414', '0428', '0436', '0440', '0981', '0982', '0983',
     #  '0984', '0987', '100014', '1106', '1107', '1127', '1325', '1326',
      # '1330', '139', '1402', '143', '1474', '269003', '269005', '269006',
      # '269007', '269008', '269009', '269010', '269011', '269012', '269014',
      # '269016', '269017', '269019', '300017', '300018', '300019', '300021',
      # '360', '669001', '669002', '669006', '809001', '809009', '979001',
      # '979002', '979003', '979004', '979005', '979006', '979007', '979008',
      # '979009', '979011', '979012', '979013', '979014', '979015', '979016',
      # '979017', '979018', '979019', '979020', '979021', '979022', '979023',
      # 'A301', 'A302'],
def get_feat_669002(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count('<2')):
            return 1.95
        if(x.count('-')):
            return np.nan
        if(x.count('<0.200')):
            return 0.195
        if (x.count(' ')):
            i = x.index(' ')
      #      #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
    #    if(x.count('116.0.')):
     #       return 116.0
        #if(x.count('>100')):
        #    return 100
        return np.nan
data_history_5_3['feat_669002']=data_history_5_3['669002'].map(lambda x:get_feat_669002(x))
#data_history_5_3[data_history_5_3['feat_669002'].isnull()]['669002'].unique()
b=data_history_5_3['feat_669002']
b=pd.DataFrame(b)
data_history_5_3['feat_669002']=b.fillna(b.mean())
del data_history_5_3['669002']
#############################################
def get_feat_669006(x):
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
        if(x.count('<1')):
            return 1
        if(x.count('<0.60')):
            return 0.55
        if(x.count('<2.00')):
            return 1.96
        return np.nan
data_history_5_3['feat_669006']=data_history_5_3['669006'].map(lambda x:get_feat_669006(x))
#data_history_5_3[data_history_5_3['feat_669006'].isnull()]['669006'].unique()
b=data_history_5_3['feat_669006']
b=pd.DataFrame(b)
data_history_5_3['feat_669006']=b.fillna(b.mean())
del data_history_5_3['669006']
############################################################
def get_feat_809001(x):
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
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_3['feat_809001']=data_history_5_3['809001'].map(lambda x:get_feat_809001(x))
#data_history_5_3[data_history_5_3['feat_809001'].isnull()]['809001'].unique()
b=data_history_5_3['feat_809001']
b=pd.DataFrame(b)
data_history_5_3['feat_809001']=b.fillna(b.mean())
del data_history_5_3['809001']
#####################################################################################################
def get_feat_809009(x):
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
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_3['feat_809009']=data_history_5_3['809009'].map(lambda x:get_feat_809009(x))
#data_history_5_3[data_history_5_3['feat_809009'].isnull()]['809009'].unique()
b=data_history_5_3['feat_809009']
b=pd.DataFrame(b)
data_history_5_3['feat_809009']=b.fillna(b.mean())
del data_history_5_3['809009']
###########################################################################
def get_feat_979001(x):
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
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_3['feat_979001']=data_history_5_3['979001'].map(lambda x:get_feat_979001(x))
#data_history_5_3[data_history_5_3['feat_979001'].isnull()]['979001'].unique()
b=data_history_5_3['feat_979001']
b=pd.DataFrame(b)
data_history_5_3['feat_979001']=b.fillna(b.mean())
del data_history_5_3['979001']
#############################################
def get_feat_979002(x):
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
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_3['feat_979002']=data_history_5_3['979002'].map(lambda x:get_feat_979002(x))
#data_history_5_3[data_history_5_3['feat_979002'].isnull()]['979002'].unique()
b=data_history_5_3['feat_979002']
b=pd.DataFrame(b)
data_history_5_3['feat_979002']=b.fillna(b.mean())
del data_history_5_3['979002']
##############################################3
def get_feat_979003(x):
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
        if(x.count('320.00.')):
            return 320.00
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_3['feat_979003']=data_history_5_3['979003'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979003'].isnull()]['979003'].unique()
b=data_history_5_3['feat_979003']
b=pd.DataFrame(b)
data_history_5_3['feat_979003']=b.fillna(b.mean())
del data_history_5_3['979003']
###################################################################
data_history_5_3['feat_979004']=data_history_5_3['979004'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979004'].isnull()]['979004'].unique()
b=data_history_5_3['feat_979004']
b=pd.DataFrame(b)
data_history_5_3['feat_979004']=b.fillna(b.mean())
del data_history_5_3['979004']
#####################################################################################################
data_history_5_3['feat_979005']=data_history_5_3['979005'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979005'].isnull()]['979005'].unique()
b=data_history_5_3['feat_979005']
b=pd.DataFrame(b)
data_history_5_3['feat_979005']=b.fillna(b.mean())
del data_history_5_3['979005']
###########################################################################
data_history_5_3['feat_979006']=data_history_5_3['979006'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979006'].isnull()]['979006'].unique()
b=data_history_5_3['feat_979006']
b=pd.DataFrame(b)
data_history_5_3['feat_979006']=b.fillna(b.mean())
del data_history_5_3['979006']
##########################################
data_history_5_3['feat_979007']=data_history_5_3['979007'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979007'].isnull()]['979007'].unique()
b=data_history_5_3['feat_979007']
b=pd.DataFrame(b)
data_history_5_3['feat_979007']=b.fillna(b.mean())
del data_history_5_3['979007']
################################################3
data_history_5_3['feat_979008']=data_history_5_3['979008'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979008'].isnull()]['979008'].unique()
b=data_history_5_3['feat_979008']
b=pd.DataFrame(b)
data_history_5_3['feat_979008']=b.fillna(b.mean())
del data_history_5_3['979008']
###############################################
data_history_5_3['feat_979009']=data_history_5_3['979009'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979009'].isnull()]['979009'].unique()
b=data_history_5_3['feat_979009']
b=pd.DataFrame(b)
data_history_5_3['feat_979009']=b.fillna(b.mean())
del data_history_5_3['979009']
##############################################################
data_history_5_3['feat_979011']=data_history_5_3['979011'].map(lambda x:get_feat_979003(x))
#data_history_5_3[data_history_5_3['feat_979011'].isnull()]['979011'].unique()
b=data_history_5_3['feat_979011']
b=pd.DataFrame(b)
data_history_5_3['feat_979011']=b.fillna(b.mean())
del data_history_5_3['979011']


# '979011', '979012', '979013', '979014', '979015', '979016',
      # '979017', '979018', '979019', '979020', '979021', '979022', '979023',
      # 'A301', 'A302'],
a=[12,13,14,15,16,17,18,19,20,21,22,23]
for i in a:
    data_history_5_3['feat_9790'+str(i)] = data_history_5_3['9790'+str(i)].map(lambda x: get_feat_979003(x))

def feat_combine():
    feat_now=pd.concat([feature_old,data_history_5_3['feat_100014'],data_history_5_3['feat_1106'],data_history_5_3['feat_1107'],
                        data_history_5_3['feat_1127'],data_history_5_3['feat_139'],data_history_5_3['feat_143'],data_history_5_3['feat_1474'],
                        data_history_5_3['feat_269003'],data_history_5_3['feat_269005'],data_history_5_3['feat_269006'],data_history_5_3['feat_269007'],
                        data_history_5_3['feat_269008'],data_history_5_3['feat_269009'],data_history_5_3['feat_269010'],data_history_5_3['feat_269011'],
                        data_history_5_3['feat_269012'],data_history_5_3['feat_269014'],data_history_5_3['feat_269016'],data_history_5_3['feat_269017'],
                        data_history_5_3['feat_269019'],data_history_5_3['feat_300017'],data_history_5_3['feat_300018'],data_history_5_3['feat_300019'],
                        data_history_5_3['feat_300021'],data_history_5_3['feat_669001'],data_history_5_3['feat_669002'],data_history_5_3['feat_669006'],
                        data_history_5_3['feat_809001'],data_history_5_3['feat_809009'],data_history_5_3['feat_979001'],data_history_5_3['feat_979002'],
                        data_history_5_3['feat_979003'],data_history_5_3['feat_979004'],data_history_5_3['feat_979005'],data_history_5_3['feat_979006'],
                        data_history_5_3['feat_979007'],data_history_5_3['feat_979008'],data_history_5_3['feat_979009'],data_history_5_3['feat_979011'],
                        data_history_5_3['feat_979012'],data_history_5_3['feat_979013'],data_history_5_3['feat_979014'],data_history_5_3['feat_979015'],
                        data_history_5_3['feat_979016'],data_history_5_3['feat_979017'],data_history_5_3['feat_979018'],data_history_5_3['feat_979019'],
                        data_history_5_3['feat_979020'],data_history_5_3['feat_979021'],data_history_5_3['feat_979022'],data_history_5_3['feat_979023']],axis=1)
    return feat_now
feat_now=feat_combine()
feat_now.to_csv('feat_history_5_4_16_20.csv',index=False)