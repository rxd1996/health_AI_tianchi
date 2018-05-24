import pandas as pd
import numpy as np
old_feature=pd.read_csv('feat_history_5_5_00_00.csv',low_memory=False)
data_history_5_5=pd.read_csv('data_history_feat_clash8_5_4_21_02.csv',low_memory=False)
def get_feat_1873(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('<')):
            i=x.index('<')
            x=x[i+1:]
            x=float(x)
            return x
        if(x.count('＜')):
            i=x.index('＜')
            x=float(x[i+1:])
            return x
        if(x.count('>')):
            return 22
        if(x.count('+')):
            return 30
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        return np.nan
data_history_5_5['feat_1873']=data_history_5_5['1873'].map(lambda x:get_feat_1873(x))

def get_feat_189(x):
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
        if (x.count('<')):
            i = x.index('<')
            x = x[i + 1:]
            x = float(x)
            return x
        #if(x.count('+')):
         #   return 15
        if(x.count('2..99')):
            return 2.99
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan

data_history_5_5['feat_189'] = data_history_5_5['189'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_2371'] = data_history_5_5['2371'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_269026'] = data_history_5_5['269026'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_300035'] = data_history_5_5['300035'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_30006'] = data_history_5_5['30006'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_300078'] = data_history_5_5['300078'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_321'] = data_history_5_5['321'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_809002'] = data_history_5_5['809002'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_809007'] = data_history_5_5['809007'].map(lambda x: get_feat_189(x))
data_history_5_5['feat_809024'] = data_history_5_5['809024'].map(lambda x: get_feat_189(x))

def get_feat_A701(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count('k')):
            i = x.index('k')
            x = x[:i]
            x = float(x)
            return x
#        if (x.count('<')):
 #           i = x.index('<')
  #          x = x[i + 1:]
   #         x = float(x)
    #        return x
        if(x.count('6,3')):
            return 6.3
     #   if(x.count('2..99')):
      #      return 2.99
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan

data_history_5_5['feat_A701'] = data_history_5_5['A701'].map(lambda x: get_feat_A701(x))
#data_history_5_5[data_history_5_5['feat_A703'].isnull()]['A703'].unique()
def get_feat_A703(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if (x.count('d')):
            i = x.index('d')
            x = x[:i]
            x = float(x)
            return x
#        if (x.count('<')):
 #           i = x.index('<')
  #          x = x[i + 1:]
   #         x = float(x)
    #        return x
        if(x.count('6,3')):
            return 6.3
     #   if(x.count('2..99')):
      #      return 2.99
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_5['feat_A703'] = data_history_5_5['A703'].map(lambda x: get_feat_A703(x))

data_history_5_5_2=pd.read_csv('data_history_feat_clash8_5_5_13_02.csv',low_memory=False)


def get_feat_0104(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('-') or x.count('阴')):
            return np.nan
        if(x.count('阳性(低水平)')):
            return 0.5
        if(x.count('阳') or x.count('+')):
            return 0.76
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('<6')):
            return 6
        if(x.count('3.0.0')):
            return 3.0
        if(x.count('<1.00')):
            return 0.97
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan


#vid', '0104', '0105', '0106', '0107', '0108', '0109', '0218', '0224',
 #      '0441', '1104', '1124', '1331', '1335', '1337', '1363', '1842', '2165',
  #     '2282', '2390', '2407', '2410', '2412', '2986', '300006', '300044',
   #    '300048', '310', '311', '3184', '319100', '459154', '459155', '459156',
    #   '459158', '459159', '669024', '809020', '809031', '809032', '809033',
     #  '809034', '809035'],
def get_feat_1363(x):
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
        if(x.count('<=')):
            return 10
        if(x.count('<')):
            i = x.index('<')
            x = x[i+1:]
            x = float(x)
            return x
        if(x.count('＜')):
            return 10
        if(x.count('>')):
            return 4000
        if(x.count('+')):
            return 1000
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan

#vid', '0104', '0105', '0106', '0107', '0108', '0109', '0218', '0224',
 #      '0441', '1104', '1124', '1331', '1335', '1337', '1363', '1842', '2165',
  #     '2282', '2390', '2407', '2410', '2412', '2986', '300006', '300044',
   #    '300048', '310', '311', '3184', '319100', '459154', '459155', '459156',
    #   '459158', '459159', '669024', '809020', '809031', '809032', '809033',
     #  '809034', '809035'],
def get_feat_669024(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('-') or x.count('阴')):
            return np.nan
        if(x.count('弱')):
            return 0.5
        if(x.count('阳') or x.count('+')):
            return 0.76
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('<6')):
            return 6
        if(x.count('3.0.0')):
            return 3.0
        if(x.count('<1.00')):
            return 0.97
        #if(x.count('<1')):
       #     return 1
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan
data_history_5_5_2['feat_0104'] = data_history_5_5_2['0104'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_0107'] = data_history_5_5_2['0107'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_1363'] = data_history_5_5_2['1363'].map(lambda x: get_feat_1363(x))
data_history_5_5_2['feat_1842'] = data_history_5_5_2['1842'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_2165'] = data_history_5_5_2['2165'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_2390'] = data_history_5_5_2['2390'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_2407'] = data_history_5_5_2['2407'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_2410'] = data_history_5_5_2['2410'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_2412'] = data_history_5_5_2['2412'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_2986'] = data_history_5_5_2['2986'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_300044'] = data_history_5_5_2['300044'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_300048'] = data_history_5_5_2['300048'].map(lambda x: get_feat_0104(x))
data_history_5_5_2['feat_669024'] = data_history_5_5_2['669024'].map(lambda x: get_feat_669024(x))
#data_history_5_5_2[data_history_5_5_2['feat_669024'].isnull()]['669024'].unique()

data_history_5_5_3=pd.read_csv('data_history_feat_clash8_5_5_17_50.csv',low_memory=False)





def get_feat_100008(x):
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
        if (x.count('(')):
            i = x.index('(')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('<2.00')):
            return 2.0
        if(x.count('>400')):
            return 400
        if(x.count('%')):
            i = x.index('%')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('<0.5')):
            return 0.5
        if(x.count('<1.00')):
            return 1.00
        if(x.count('<0.200')):
            return 0.2
        if(x.count('<1')):
            return 1
        if(x.count('>300.000')):
            return 302
        if(x.count('+++')):
            return 66
        if(x.count('2.01.')):
            return 2.01
     #   if(x.count('2..99')):
      #      return 2.99
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan


data_history_5_5_3['feat_100008'] = data_history_5_5_3['100008'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_10013'] = data_history_5_5_3['10013'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_2163'] = data_history_5_5_3['2163'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_2168'] = data_history_5_5_3['2168'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_2411'] = data_history_5_5_3['2411'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_2413'] = data_history_5_5_3['2413'].map(lambda x: get_feat_100008(x))
def get_feat_2247(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
        if(x.count('阴性')):
            return np.nan
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('<10')):
            return 10
        if(x.count('<15.00')):
            return 15
        if(x.count('<0.9')):
            return 0.9
        if(x.count('>4000')):
            return 4000
        if(x.count('弱阳性')):
            return 500
        if(x.count('阳') or x.count('+')):
            return 2000
      #  if(x.count('<2.00')):
       #     return 2.0
       # if(x.count('>400')):
        #    return 400
     #   if(x.count('2..99')):
      #      return 2.99
      #  if(x.count('<0.60')):
     #       return 0.55
    #    if(x.count('<2.00')):
   #         return 1.96
        return np.nan

data_history_5_5_3['feat_2247'] = data_history_5_5_3['2247'].map(lambda x: get_feat_2247(x))
data_history_5_5_3['feat_2414'] = data_history_5_5_3['2414'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_2421'] = data_history_5_5_3['2421'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300010'] = data_history_5_5_3['300010'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300028'] = data_history_5_5_3['300028'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300033'] = data_history_5_5_3['300033'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300034'] = data_history_5_5_3['300034'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300050'] = data_history_5_5_3['300050'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300051'] = data_history_5_5_3['300051'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300067'] = data_history_5_5_3['300067'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300093'] = data_history_5_5_3['300093'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300113'] = data_history_5_5_3['300113'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300125'] = data_history_5_5_3['300125'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300126'] = data_history_5_5_3['300126'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_300150'] = data_history_5_5_3['300150'].map(lambda x: get_feat_100008(x))

def get_feat_300151(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
      #  if(x.count('阴性')):
       #     return np.nan
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('--')):
            return 4.5
        if(x.count('+-') or ((x.count('-')) and len(x)==1) or x.count('阴')):
            return np.nan
        if(x.count('-')):
            i=x.index('-')
            x=(float(x[:i])+float(x[i+1:]))/2
            return x
        if(x.count('+')):
            return 66
        #if(x.count('弱阳性')):
        #    return 500
       # if(x.count('阳') or x.count('+')):
      #      return 2000
        return np.nan
data_history_5_5_3['feat_300151'] = data_history_5_5_3['300151'].map(lambda x: get_feat_300151(x))
data_history_5_5_3['feat_300152'] = data_history_5_5_3['300152'].map(lambda x: get_feat_100008(x))

def get_feat_3203(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
      #  if(x.count('阴性')):
       #     return np.nan
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('+2/HP')):
            return 2
        if (x.count('+21/HP')):
            return 21
        if (x.count('+3/HP')):
            return 3
        if(x.count('+1/HP')):
            return 1
        if(x.count('/')):
            i=x.index('-')
            j=x.index('/')
            x=(float(x[:i])+float(x[i+1:j]))/2
            return x
        if(x.count('大量')):
            return 10
    return np.nan

data_history_5_5_3['feat_3203'] = data_history_5_5_3['3203'].map(lambda x: get_feat_3203(x))
data_history_5_5_3['feat_669023'] = data_history_5_5_3['669023'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_709001'] = data_history_5_5_3['709001'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_709003'] = data_history_5_5_3['709003'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_809014'] = data_history_5_5_3['809014'].map(lambda x: get_feat_100008(x))

def get_feat_819007(x):
    try:
        x=float(x)
      #  if(x==-90):
      #      return 90
    #    if(x==0):
   #         return np.nan
        return x
    except:
      #  if(x.count('阴性')):
       #     return np.nan
        if (x.count(' ')):
            i = x.index(' ')
            x = x[:i]
            x = float(x)
            return x
        if(x.count('--')):
            return 4.5
        if(x.count('+-') or ((x.count('-')) and len(x)==1) or x.count('阴')):
            return np.nan
        if(x.count('-')):
            i=x.index('-')
            x=(float(x[:i])+float(x[i+1:]))/2
            return x
        if(x.count('+')):
            return 19
        #if(x.count('弱阳性')):
        #    return 500
       # if(x.count('阳') or x.count('+')):
      #      return 2000
        return np.nan
data_history_5_5_3['feat_819007'] = data_history_5_5_3['819007'].map(lambda x: get_feat_819007(x))
data_history_5_5_3['feat_819008'] = data_history_5_5_3['819008'].map(lambda x: get_feat_100008(x))
data_history_5_5_3['feat_819018'] = data_history_5_5_3['819018'].map(lambda x: get_feat_100008(x))
#vid', # '300126',

       #'809016', '809030', '809063', '819007', '819008', '819009', '819010',
       #'819011', '819012', '819013', '819014', '819015', '819016', '819017',
       #'819018', '819019', '819020', '819021', '819022', '819023', '819026',
       #'819027', '819029'],


#data_history_5_5_3[data_history_5_5_3['feat_819018'].isnull()]['819018'].unique()

def feat_combine():
    feat_now=pd.concat([old_feature,data_history_5_5['feat_1873'],data_history_5_5['feat_189'],data_history_5_5['feat_2371'],data_history_5_5['feat_269026'],
                        data_history_5_5['feat_300035'],data_history_5_5['feat_30006'],data_history_5_5['feat_300078'],data_history_5_5['feat_321'],
                        data_history_5_5['feat_809002'],data_history_5_5['feat_809007'],data_history_5_5['feat_809024'],data_history_5_5['feat_A701'],
                        data_history_5_5['feat_A703'],data_history_5_5_2['feat_0104'],data_history_5_5_2['feat_0107'],data_history_5_5_2['feat_1363'],
                        data_history_5_5_2['feat_1842'],data_history_5_5_2['feat_2165'],data_history_5_5_2['feat_2390'],data_history_5_5_2['feat_2407'] ,
                        data_history_5_5_2['feat_2410'],data_history_5_5_2['feat_2412'],data_history_5_5_2['feat_2986'],data_history_5_5_2['feat_300044'],
                        data_history_5_5_2['feat_300048'],data_history_5_5_2['feat_669024'],data_history_5_5_3['feat_100008'],data_history_5_5_3['feat_10013'],
                        data_history_5_5_3['feat_2163'],data_history_5_5_3['feat_2168'],data_history_5_5_3['feat_2247'],data_history_5_5_3['feat_2411'],
                        data_history_5_5_3['feat_2413'],data_history_5_5_3['feat_2414'],data_history_5_5_3['feat_2421'],data_history_5_5_3['feat_300010'],
                        data_history_5_5_3['feat_300028'],data_history_5_5_3['feat_300033'],data_history_5_5_3['feat_300034'],data_history_5_5_3['feat_300050'],
                        data_history_5_5_3['feat_300051'],data_history_5_5_3['feat_300067'],data_history_5_5_3['feat_300093'],data_history_5_5_3['feat_300113'],
                        data_history_5_5_3['feat_300125'],data_history_5_5_3['feat_300126'],data_history_5_5_3['feat_300150'],data_history_5_5_3['feat_300151'],
                        data_history_5_5_3['feat_300152'],data_history_5_5_3['feat_3203'],data_history_5_5_3['feat_669023'],data_history_5_5_3['feat_709001'],
                        data_history_5_5_3['feat_709003'],data_history_5_5_3['feat_809014'],data_history_5_5_3['feat_819007'],data_history_5_5_3['feat_819008'],
                        data_history_5_5_3['feat_819018'],],axis=1)
    return feat_now
feat_now=feat_combine()
feat_now.to_csv('feat_history_5_5_20_43.csv',index=False)