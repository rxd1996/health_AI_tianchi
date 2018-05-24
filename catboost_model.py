import numpy as np
import pandas as pd

import pandas as pd

test_id=pd.read_csv('meinian_round1_test_b_20180505.csv',encoding='gbk',usecols=['vid'])

train_id=pd.read_csv('train_data.csv',usecols=['vid'])

train_label=pd.read_csv('train_data.csv',usecols=[1,2,3,4,5])

train_label1=train_label['收缩压']
train_label2=train_label['舒张压']
train_label3=train_label['血清甘油三酯']
train_label4=train_label['血清高密度脂蛋白']
train_label5=train_label['血清低密度脂蛋白']
feat_history=pd.read_csv('feat_history_4_24_21_25.csv')

train_data=pd.merge(train_id,feat_history,on='vid',how='left')
test_data=pd.merge(test_id,feat_history,on='vid',how='left')
feat_history_second=pd.read_csv('feat_second_history_4_21_19_23.csv')

train_data=pd.merge(train_data,feat_history_second,on='vid',how='left')
test_data=pd.merge(test_data,feat_history_second,on='vid',how='left')
feat_history_float=pd.read_csv('ata_history_float_.csv')
train_data=pd.merge(train_data,feat_history_float,on='vid',how='left')
test_data=pd.merge(test_data,feat_history_float,on='vid',how='left')
#del train_data['vid']
#del test_data['vid']
####################################################################################################################
import lightgbm as lgb
from sklearn.model_selection import train_test_split
#preds_sub = gbm.predict(testt_feat)
import xgboost as xgb
import operator


#importance = sorted(importance.items(), key=operator.itemgetter(1))
#importance=list(importance)
#for i in range(len(importance)):
#    if(importance[i]<2):
#        del train_data[features[i]]
#        del test_data[features[i]]
#train_data=pd.read_csv('train_data_by_feature_choice_lgb_4_25.csv')
#test_data=pd.read_csv('test_data_by_feature_choice_lgb_4_25.csv')
#train_data=pd.concat([train_id,train_data],axis=1)
#test_data=pd.concat([test_id,test_data],axis=1)
new_feature=pd.read_csv('feat_history_5_5_20_43.csv')
train_data=pd.merge(train_data,new_feature,on='vid',how='left')
test_data=pd.merge(test_data,new_feature,on='vid',how='left')
del train_data['vid']
del test_data['vid']
import lightgbm as lgb
#from sklearn.model_selection import train_test_split
#preds_sub = gbm.predict(testt_feat)
import xgboost as xgb
import operator
from catboost import CatBoostRegressor

x_train,x_val,y_train,y_val=train_test_split(train_data,train_label1,test_size=0.2,random_state=100)
model=CatBoostRegressor(iterations=500,depth=3,learning_rate=0.1,loss_function='RMSE')
model.fit(x_train,y_train,eval_set=(x_val,y_val),plot=True)
y1=model.predict(test_data)


x_train,x_val,y_train,y_val=train_test_split(train_data,train_label2,test_size=0.2,random_state=100)
model=CatBoostRegressor(iterations=500,depth=3,learning_rate=0.1,loss_function='RMSE')
model.fit(x_train,y_train,eval_set=(x_val,y_val),plot=True)
y2=model.predict(test_data)

x_train,x_val,y_train,y_val=train_test_split(train_data,train_label3,test_size=0.2,random_state=100)
model=CatBoostRegressor(iterations=130,depth=3,learning_rate=0.1,loss_function='RMSE')
model.fit(x_train,y_train,eval_set=(x_val,y_val),plot=True)
y3=model.predict(test_data)

x_train,x_val,y_train,y_val=train_test_split(train_data,train_label4,test_size=0.2,random_state=100)
model=CatBoostRegressor(iterations=500,depth=3,learning_rate=0.1,loss_function='RMSE')
model.fit(x_train,y_train,eval_set=(x_val,y_val),plot=True)
y4=model.predict(test_data)

x_train,x_val,y_train,y_val=train_test_split(train_data,train_label5,test_size=0.2,random_state=100)
model=CatBoostRegressor(iterations=440,depth=3,learning_rate=0.1,loss_function='RMSE')
model.fit(x_train,y_train,eval_set=(x_val,y_val),plot=True)
y5=model.predict(test_data)

test_id['y1']=y1
test_id['y2']=y2
test_id['y3']=y3
test_id['y4']=y4
test_id['y5']=y5
test_id.to_csv('tijiao_new_5_6_B_catboost.csv',index=False,header=None)