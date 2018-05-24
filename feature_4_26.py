import pandas as pd
import numpy as np
#test_id=pd.read_csv('meinian_round1_test_a_20180408.csv',encoding='gbk')
#train_data=pd.read_csv('train_data.csv')
data_history=pd.read_csv('data_history_feat_clash4_4_26.csv',low_memory=False)
data_history_vid=pd.read_csv('history_first_data.csv',usecols=['vid'])
#################################################################################################################
#['vid', '0119', '0201', '0202', '0203', '0207', '0208', '0209', '0210',
#       '0212', '0215', '0216', '0217', '0222', '0405', '0973', '0978', '0979',
#       '0980', '10002', '1115', '1301', '1302', '1303', '1304', '1305', '1315',
#       '183', '2174', '314', '3207', '3399', '3400', 'A201', 'A202'],
def get_feat_10002(x):
    try:
        x=float(x)
        if(x<=0):
            return np.nan
        return x
    except:
        if(x.count(' ')==1):
            i=x.index(' ')
            x=x[:i]
            x=float(x)
            return x
        return np.nan
data_history['feat_10002']=data_history['10002'].map(lambda x:get_feat_10002(x))
#data_history[data_history['feat_10002'].isnull()]['10002']
b=data_history['feat_10002']
b=pd.DataFrame(b)
data_history['feat_10002']=b.fillna(b.mean())
del data_history['10002']
####################################################################################################################

def get_feat_1115(x):
    try:
        x=float(x)
     #   if(x<=0):
      #      return np.nan
        return x
    except:
        if(x.count(' ')==1):
            i=x.index(' ')
            x=x[:i]
            x=float(x)
            return x
        return np.nan
data_history['feat_1115']=data_history['1115'].map(lambda x:get_feat_1115(x))
#data_history[data_history['feat_10002'].isnull()]['10002']
b=data_history['feat_1115']
b=pd.DataFrame(b)
data_history['feat_1115']=b.fillna(b.mean())
del data_history['1115']
###################################################################################################################
def get_feat_183(x):
    try:
        x=float(x)
        if(x<=30):
            return np.nan
        return x
    except:
        if(x.count(' ')==1):
            i=x.index(' ')
            x=x[:i]
            x=float(x)
            return x
        if(x.count('77..21')):
            return 77.21
        return np.nan
data_history['feat_183']=data_history['183'].map(lambda x:get_feat_183(x))
#data_history[data_history['feat_10002'].isnull()]['10002']
b=data_history['feat_183']
b=pd.DataFrame(b)
data_history['feat_183']=b.fillna(b.mean())
del data_history['183']
########################################################################################################################
def get_feat_2174(x):
    try:
        x=float(x)
       # if(x<=30):
        #    return np.nan
        return x
    except:
        if(x.count(' ')==1):
            i=x.index(' ')
            x=x[:i]
            x=float(x)
            return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history['feat_2174']=data_history['2174'].map(lambda x:get_feat_2174(x))
#data_history[data_history['feat_10002'].isnull()]['10002']
b=data_history['feat_2174']
b=pd.DataFrame(b)
data_history['feat_2174']=b.fillna(b.mean())
del data_history['2174']
#data_history[data_history['feat_2174'].isnull()]['2174']
########################################################################################################################
def get_feat_314(x):
    try:
        x=float(x)
       # if(x<=30):
        #    return np.nan
        return x
    except:
        if(x.count(' ')==1):
            i=x.index(' ')
            x=x[:i]
            x=float(x)
            return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history['feat_314']=data_history['314'].map(lambda x:get_feat_314(x))
#data_history[data_history['feat_10002'].isnull()]['10002']
b=data_history['feat_314']
b=pd.DataFrame(b)
data_history['feat_314']=b.fillna(b.mean())
del data_history['314']
###########################################################################################################################
data_history_4_27=pd.read_csv('data_history_feat_clash5_4_26_22_24.csv',low_memory=False)
#vid', '0120', '0206', '0425', '0977', '100006', '10003', '1102',
#       '1103', '1313', '1314', '1321', '1322', '1328', '1845', '2333', '2372',
#       '31', '312', '313', '315', '316', '317', '319', '32', '320', '33', '37',
#       '38'],
############################################################################################################################
#data_history_4_27[data_history_4_27['0425']=='18']
def get_feat_100006(x):
    try:
        x=float(x)
        if(x==0):
            return np.nan
        return x
    except:
        if(x.count('---')==1):
            return np.nan
        if(x.count('-')):
            return 16.2
        #    i=x.index(' ')
        #    x=x[:i]
        #    x=float(x)
         #   return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_27['feat_100006']=data_history_4_27['100006'].map(lambda x:get_feat_100006(x))
#data_history_4_27[data_history_4_27['feat_100006']==0]['100006']
b=data_history_4_27['feat_100006']
b=pd.DataFrame(b)
data_history_4_27['feat_100006']=b.fillna(b.mean())
del data_history_4_27['100006']
###############################################################################################################################
def get_feat_10003(x):
    try:
        x=float(x)
       # if(x==0):
       #     return np.nan
        return x
    except:
   #     if(x.count('---')==1):
    #        return np.nan
        if(x.count(' ')):
            i=x.index(' ')
            x=x[:i]
            x=float(x)
            return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_27['feat_10003']=data_history_4_27['10003'].map(lambda x:get_feat_10003(x))
#data_history_4_27[data_history_4_27['feat_100006']==0]['100006']
b=data_history_4_27['feat_10003']
b=pd.DataFrame(b)
data_history_4_27['feat_10003']=b.fillna(b.mean())
del data_history_4_27['10003']
################################################################################################################################
def get_feat_1845(x):
    try:
        x=float(x)
      #  if(x==0):
      #      return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        return np.nan
data_history_4_27['feat_1845']=data_history_4_27['1845'].map(lambda x:get_feat_1845(x))
#data_history_4_27[data_history_4_27['feat_1845'].isnull()]['1845']
b=data_history_4_27['feat_1845']
b=pd.DataFrame(b)
data_history_4_27['feat_1845']=b.fillna(b.mean())
del data_history_4_27['1845']
#######################################################################################################################
def get_feat_2333(x):
    try:
        x=float(x)
        if(x==0):
            return np.nan
        return x
    except:
          if (x.count(' ')):
              i = x.index(' ')
              x1 = x[:i]
              x1 = float(x1)
              x2=x[i+1:]
              x2=float(x2)
              x=(x1+x2)/2
              return x
          if(x.count('<')):
              return 0.03
          if(x.count('.')==2):
              return 5.0
          return np.nan
data_history_4_27['feat_2333']=data_history_4_27['2333'].map(lambda x:get_feat_2333(x))
#data_history_4_27[data_history_4_27['feat_1845']==0]['1845']
b=data_history_4_27['feat_2333']
b=pd.DataFrame(b)
data_history_4_27['feat_2333']=b.fillna(b.mean())
del data_history_4_27['2333']
#####################################################################################################################
def get_feat_2372(x):
    try:
        x=float(x)
      #  if(x==0):
      #      return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            x1 = x[:i]
            x1 = float(x1)
            x2 = x[i + 1:]
            x2 = float(x2)
            x = (x1 + x2) / 2
            return x
        if(x.count('<')):
            i=x.index('<')
            x=x[i+1:]
            x=float(x)
            return x
        if(x.count('＜')):
            return 0.6
        if(x.count('.')==2):
            return 2.792
        return np.nan
data_history_4_27['feat_2372']=data_history_4_27['2372'].map(lambda x:get_feat_2372(x))
#data_history_4_27[data_history_4_27['feat_2372'].isnull()]['2372']
b=data_history_4_27['feat_2372']
b=pd.DataFrame(b)
data_history_4_27['feat_2372']=b.fillna(b.mean())
del data_history_4_27['2372']
#########################################################################################################################
def get_feat_31(x):
    try:
        x=float(x)
       # if(x==0):
       #     return np.nan
        return x
    except:
        if(x.count('.')==2):
            return 5.1
       # if(x.count(' ')):
       #     i=x.index(' ')
       #     x=x[:i]
       #     x=float(x)
       #     return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_27['feat_31']=data_history_4_27['31'].map(lambda x:get_feat_31(x))
#data_history_4_27[data_history_4_27['feat_31']==0]['31']
b=data_history_4_27['feat_31']
b=pd.DataFrame(b)
data_history_4_27['feat_31']=b.fillna(b.mean())
del data_history_4_27['31']
###############################################################################################################################
def get_feat_313(x):
    try:
        x=float(x)
       # if(x==0):
       #     return np.nan
        return x
    except:
        if(x.count('脂血')):
            return 189
       # if(x.count(' ')):
       #     i=x.index(' ')
       #     x=x[:i]
       #     x=float(x)
       #     return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_27['feat_313']=data_history_4_27['313'].map(lambda x:get_feat_313(x))
#data_history_4_27[data_history_4_27['feat_313'].isnull()]['313']
b=data_history_4_27['feat_313']
b=pd.DataFrame(b)
data_history_4_27['feat_313']=b.fillna(b.mean())
del data_history_4_27['313']
#######################################################################################################################
def get_feat_32(x):
    try:
        x=float(x)
       # if(x==0):
       #     return np.nan
        return x
    except:
        if(x.count('.')==2):
            return 2.1
       # if(x.count(' ')):
       #     i=x.index(' ')
       #     x=x[:i]
       #     x=float(x)
       #     return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_27['feat_32']=data_history_4_27['32'].map(lambda x:get_feat_32(x))
#data_history_4_27[data_history_4_27['feat_32'].isnull()]['32']
b=data_history_4_27['feat_32']
b=pd.DataFrame(b)
data_history_4_27['feat_32']=b.fillna(b.mean())
del data_history_4_27['32']
#########################################################################################################################################
def get_feat_320(x):
    try:
        x=float(x)
        if(x==0):
            return np.nan
        return x
    except:
      #  if(x.count('.')==2):
       #     return 2.1
       # if(x.count(' ')):
       #     i=x.index(' ')
       #     x=x[:i]
       #     x=float(x)
       #     return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_27['feat_320']=data_history_4_27['320'].map(lambda x:get_feat_320(x))
#data_history_4_27[data_history_4_27['feat_320'].isnull()]['320'].unique()
b=data_history_4_27['feat_320']
b=pd.DataFrame(b)
data_history_4_27['feat_320']=b.fillna(b.mean())
del data_history_4_27['320']
############################################################################################################################
def get_feat_38(x):
    try:
        x=float(x)
      #  if(x==0):
    #        return np.nan
        return x
    except:
        if(x.count('.')==2):
            return 8.53
       # if(x.count(' ')):
       #     i=x.index(' ')
       #     x=x[:i]
       #     x=float(x)
       #     return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_27['feat_38']=data_history_4_27['38'].map(lambda x:get_feat_38(x))
#data_history_4_27[data_history_4_27['feat_38'].isnull()]['38'].unique()
b=data_history_4_27['feat_38']
b=pd.DataFrame(b)
data_history_4_27['feat_38']=b.fillna(b.mean())
del data_history_4_27['38']
##############################################################################################################
data_history_4_30=pd.read_csv('data_history_feat_clash6_4_30_14_42.csv',low_memory=False)
#['vid', '0121', '0122', '0123', '0124', '0403', '0429', '0501', '0503',
#       '0509', '0516', '0537', '0539', '0541', '0702', '0703', '0705', '0706',
#       '0707', '0709', '0715', '0726', '0728', '0730', '0731', '0972',
#       '100005', '100007', '1316', '2406', '34', '3601', '39'],
def get_feat_0403(x):
    try:

        if(x.count('正常') or x.count('无') or  x.count('不大') or  x.count('未见')):
            return 1
        else:
            return 0
    except:
        return 1
data_history_4_30['feat_0403']=data_history_4_30['0403'].map(lambda x:get_feat_0403(x))
del data_history_4_30['0403']
######################################################################################################################
#data_history_4_30['2406'].unique()
def get_feat_2406(x):
    try:
        x=float(x)
        if(x==-90):
            return 90
       # if(x==0):
       #     return np.nan
        return x
    except:
        #if(x.count('.')==2):
        #    return 2.1
        if(x.count(' ')):
            #i=x.index(' ')
            i = x.rindex(' ')
            x =x[i + 1:]
            x=float(x)
            return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_4_30['feat_2406']=data_history_4_30['2406'].map(lambda x:get_feat_2406(x))
#data_history_4_30[data_history_4_30['feat_2406'].isnull()]['2406'].unique()
b=data_history_4_30['feat_2406']
b=pd.DataFrame(b)
data_history_4_30['feat_2406']=b.fillna(b.mean())
del data_history_4_30['2406']
########################################################################################################################################
data_history_5_1=pd.read_csv('data_history_feat_clash6_5_1_19_52.csv',low_memory=False)
#['vid', '0422', '0427', '1329', '1345', '155', '2228', '2229', '2230',
#       '2231', '2233', '2420', '2501', '269004', '269013', '269015', '269018',
#       '269020', '269021', '269022', '269023', '269024', '269025', '300036',
#       '30007', '3189', '3194', '3301', '3485', '3486', '4001', 'A601'],
def get_feat_1345(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
       # if(x==0):
       #     return np.nan
        return x
    except:
        #if(x.count('.')==2):
        #    return 2.1
        if(x.count(' ')):
            i=x.index(' ')
  #         i = x.rindex(' ')
            x =x[:i]
            x=float(x)
            return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_5_1['feat_1345']=data_history_5_1['1345'].map(lambda x:get_feat_1345(x))
#data_history_5_1[data_history_5_1['feat_1345'].isnull()]['1345'].unique()
b=data_history_5_1['feat_1345']
b=pd.DataFrame(b)
data_history_5_1['feat_1345']=b.fillna(b.mean())
del data_history_5_1['1345']
########################################################################################################################
def get_feat_155(x):
    try:
        x=float(x)
        return x
    except:
        #if(x.count('.')==2):
        #    return 2.1
        if(x.count(' ')):
            i=x.index(' ')
            x =x[:i]
            x=float(x)
            return x
        if(x.count('<')):
            i=x.index('<')
            x=x[i+1:]
            x=float(x)
            return x
        if(x.count('>')):
            i=x.index('>')
            x=x[i+1:]
            x=float(x)
            return x
        if(x.count('S')):
            return 0.68
    #    if(x.count('77..21')):
     #      return 77.21
        if(x.count('(μIU/ml)')):
            return 0.017
        return np.nan
data_history_5_1['feat_155']=data_history_5_1['155'].map(lambda x:get_feat_155(x))
#data_history_5_1[data_history_5_1['feat_155'].isnull()]['155'].unique()
b=data_history_5_1['feat_155']
b=pd.DataFrame(b)
data_history_5_1['feat_155']=b.fillna(b.mean())
del data_history_5_1['155']
#######################################################################################################################
def get_feat_2228(x):
    try:

        if (x.count('-') or x.count('阴')):
            return 0
        if(x.count('+') or x.count('阳')):
            return 1
        return 0
    except:
        return 0
data_history_5_1['feat_2228']=data_history_5_1['2228'].map(lambda x:get_feat_2228(x))
########################################################################################################################
def get_feat_2229(x):
    try:

        if (x.count('-') or x.count('阴')):
            return 0
        if(x.count('+') or x.count('阳')):
            return 1
        return 0
    except:
        return 0
data_history_5_1['feat_2229']=data_history_5_1['2229'].map(lambda x:get_feat_2229(x))
###############################################################################################
def get_feat_2230(x):
    try:

        if (x.count('-') or x.count('阴')):
            return 0
        if(x.count('+') or x.count('阳')):
            return 1
        return 0
    except:
        return 0
data_history_5_1['feat_2230']=data_history_5_1['2230'].map(lambda x:get_feat_2230(x))
##########################################################################################################
def get_feat_2231(x):
    try:

        if (x.count('-') or x.count('阴')):
            return 0
        if(x.count('+') or x.count('阳')):
            return 1
        return 0
    except:
        return 0
data_history_5_1['feat_2231']=data_history_5_1['2231'].map(lambda x:get_feat_2231(x))
del data_history_5_1['2231']
##############################################################################################################
#['vid', '0422', '0427', '1329', '1345', '155', '2228', '2229', '2230',
#       '2231', '2233', '2420', '2501', '269004', '269013', '269015', '269018',
#       '269020', '269021', '269022', '269023', '269024', '269025', '300036',
#       '30007', '3189', '3194', '3301', '3485', '3486', '4001', 'A601'],
#data_history_5_1[data_history_5_1['feat_155'].isnull()]['155'].unique()
def get_feat_2233(x):
    try:

        if (x.count('-') or x.count('阴')):
            return 0
        if(x.count('+') or x.count('阳')):
            return 1
        return 0
    except:
        return 0
data_history_5_1['feat_2233']=data_history_5_1['2233'].map(lambda x:get_feat_2233(x))
del data_history_5_1['2233']
################################################################################################################
def get_feat_2420(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
       # if(x==0):
       #     return np.nan
        return x
    except:
        #if(x.count('.')==2):
        #    return 2.1
        if(x.count(' ')):
            i=x.index(' ')
          #  i = x.rindex(' ')
            x =x[:i]
            x=float(x)
            return x
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_5_1['feat_2420']=data_history_5_1['2420'].map(lambda x:get_feat_2420(x))
#data_history_5_1[data_history_5_1['feat_2420'].isnull()]['2420'].unique()
b=data_history_5_1['feat_2420']
b=pd.DataFrame(b)
data_history_5_1['feat_2420']=b.fillna(b.mean())
del data_history_5_1['2420']
#########################################################################################################################
def get_feat_269004(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
       # if(x==0):
       #     return np.nan
        return x
    except:
        #if(x.count('.')==2):
        #    return 2.1
        if(x.count(' ')):
            return 9.50
    #    if(x.count('77..21')):
     #      return 77.21
        return np.nan
data_history_5_1['feat_269004']=data_history_5_1['269004'].map(lambda x:get_feat_269004(x))
#data_history_5_1[data_history_5_1['feat_269004'].isnull()]['269004'].unique()
b=data_history_5_1['feat_269004']
b=pd.DataFrame(b)
data_history_5_1['feat_269004']=b.fillna(b.mean())
del data_history_5_1['269004']
##########################################################################################################################
def get_feat_269013(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
       # if(x==0):
       #     return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('-')):
            i=x.index('-')
            x1=float(x[i+1:])
            x2=float(x[:i])
            x=(x1+x2)/2
            return x
        return np.nan
data_history_5_1['feat_269013']=data_history_5_1['269013'].map(lambda x:get_feat_269013(x))
#data_history_5_1[data_history_5_1['feat_269013'].isnull()]['269013'].unique()
b=data_history_5_1['feat_269013']
b=pd.DataFrame(b)
data_history_5_1['feat_269013']=b.fillna(b.mean())
del data_history_5_1['269013']
###################################################################################################################
def get_feat_269022(x):
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
        return np.nan
data_history_5_1['feat_269022']=data_history_5_1['269022'].map(lambda x:get_feat_269022(x))
#data_history_5_1[data_history_5_1['feat_269022'].isnull()]['269022'].unique()
b=data_history_5_1['feat_269022']
b=pd.DataFrame(b)
data_history_5_1['feat_269022']=b.fillna(b.mean())
del data_history_5_1['269022']
###########################################################################################################################
def get_feat_269018(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
      #  if(x==0):
      #      return np.nan
        return x
    except:
        if (x.count(' ')):
            i = x.index(' ')
            #  i = x.rindex(' ')
            x = x[:i]
            x = float(x)
            return x
        return np.nan
data_history_5_1['feat_269018']=data_history_5_1['269018'].map(lambda x:get_feat_269018(x))
#data_history_5_1[data_history_5_1['feat_269022'].isnull()]['269018'].unique()
b=data_history_5_1['feat_269018']
b=pd.DataFrame(b)
data_history_5_1['feat_269018']=b.fillna(b.mean())
del data_history_5_1['269018']
#############################################################################################################################3
#['vid', '0422', '0427', '1329', '1345', '155', '2228', '2229', '2230',
#       '2231', '2233', '2420', '2501', '269004', '269013', '269015', '269018',
#       '269020', '269021', '269022', '269023', '269024', '269025', '300036',
#       '30007', '3189', '3194', '3301', '3485', '3486', '4001', 'A601'],
def get_feat_269015(x):
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
        return np.nan
data_history_5_1['feat_269015']=data_history_5_1['269015'].map(lambda x:get_feat_269015(x))
#data_history_5_1[data_history_5_1['feat_269015'].isnull()]['269015'].unique()
b=data_history_5_1['feat_269015']
b=pd.DataFrame(b)
data_history_5_1['feat_269015']=b.fillna(b.mean())
del data_history_5_1['269015']
#################################################################################################################
def get_feat_269021(x):
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
        return np.nan
data_history_5_1['feat_269021']=data_history_5_1['269021'].map(lambda x:get_feat_269021(x))
#data_history_5_1[data_history_5_1['feat_269021'].isnull()]['269021'].unique()
b=data_history_5_1['feat_269021']
b=pd.DataFrame(b)
data_history_5_1['feat_269021']=b.fillna(b.mean())
del data_history_5_1['269021']
###############################################################################################################################
def get_feat_269023(x):
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
        return np.nan
data_history_5_1['feat_269023']=data_history_5_1['269023'].map(lambda x:get_feat_269023(x))
#data_history_5_1[data_history_5_1['feat_269023'].isnull()]['269023'].unique()
b=data_history_5_1['feat_269023']
b=pd.DataFrame(b)
data_history_5_1['feat_269023']=b.fillna(b.mean())
del data_history_5_1['269023']
#############################################################################################################################
#['vid', '0422', '0427', '1329', '1345', '155', '2228', '2229', '2230',
#       '2231', '2233', '2420', '2501', '269004', '269013', '269015', '269018',
#       '269020', '269021', '269022', '269023', '269024', '269025', '300036',
#       '30007', '3189', '3194', '3301', '3485', '3486', '4001', 'A601'],
def get_feat_269025(x):
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
        return np.nan
data_history_5_1['feat_269025']=data_history_5_1['269025'].map(lambda x:get_feat_269025(x))
#data_history_5_1[data_history_5_1['feat_269025'].isnull()]['269025'].unique()
b=data_history_5_1['feat_269025']
b=pd.DataFrame(b)
data_history_5_1['feat_269025']=b.fillna(b.mean())
del data_history_5_1['269025']
#############################################
def get_feat_269024(x):
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
        return np.nan
data_history_5_1['feat_269024']=data_history_5_1['269024'].map(lambda x:get_feat_269024(x))
#data_history_5_1[data_history_5_1['feat_269024'].isnull()]['269024'].unique()
b=data_history_5_1['feat_269024']
b=pd.DataFrame(b)
data_history_5_1['feat_269024']=b.fillna(b.mean())
del data_history_5_1['269024']
########################################################################################################################
def get_feat_4001(x):
    try:
        if (x.count('减弱')>0 or x.count('硬化')>0 or x.count('钙化')>0):
            return 0
        if(x.count('未见') or x.count('良好') or x.count('结论详见报告单'),x.count('正常')):
            return 1
        if(x.count('减弱') or x.count('硬化') or x.count('钙化')):
            return 0
    except:
        return 1
data_history_5_1['feat_4001']=data_history_5_1['4001'].map(lambda x:get_feat_4001(x))
del data_history_5_1['4001']
#########################################################################################################################


def feat_combine():
    a=pd.get_dummies(data_history_4_30['feat_0403'],prefix='feat_0403')
    b=pd.get_dummies(data_history_5_1['feat_2228'],prefix='feat_2228_')
    c=pd.get_dummies(data_history_5_1['feat_2229'],prefix='feat_2229_')
    d = pd.get_dummies(data_history_5_1['feat_2230'], prefix='feat_2230_')
    e = pd.get_dummies(data_history_5_1['feat_2231'], prefix='feat_2231_')
    f = pd.get_dummies(data_history_5_1['feat_2233'], prefix='feat_2233_')
    g = pd.get_dummies(data_history_5_1['feat_4001'], prefix='feat_4001_')
    feat_now=pd.concat([data_history_vid,data_history['feat_10002'],data_history['feat_1115'],data_history['feat_183'],data_history['feat_2174'],data_history['feat_314'],
                        data_history_4_27['feat_100006'],data_history_4_27['feat_10003'],data_history_4_27['feat_1845'],data_history_4_27['feat_2333'],data_history_4_27['feat_2372'],
                        data_history_4_27['feat_31'],data_history_4_27['feat_313'],data_history_4_27['feat_32'],data_history_4_27['feat_320'],data_history_4_27['feat_38'],a,
                        data_history_4_30['feat_2406'],data_history_5_1['feat_1345'],data_history_5_1['feat_155'],b,c,d,e,f,data_history_5_1['feat_2420'],
                        data_history_5_1['feat_269004'],data_history_5_1['feat_269013'],data_history_5_1['feat_269022'],data_history_5_1['feat_269018'],
                        data_history_5_1['feat_269015'],data_history_5_1['feat_269023'],data_history_5_1['feat_269021'],data_history_5_1['feat_269024'],
                        data_history_5_1['feat_269025'],g],axis=1)
    return feat_now
feat_now=feat_combine()
feat_now.to_csv('feat_history_5_2_21_09.csv',index=False)