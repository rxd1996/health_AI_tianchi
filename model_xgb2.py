import pandas as pd

test_id=pd.read_csv('[new] meinian_round1_test_a_20180409.csv',encoding='gbk',usecols=['vid'])

train_id=pd.read_csv('train_data.csv',usecols=['vid'])

train_label=pd.read_csv('train_data.csv',usecols=[1,2,3,4,5])

train_label1=train_label['收缩压']
train_label2=train_label['舒张压']
train_label3=train_label['血清甘油三酯']
train_label4=train_label['血清高密度脂蛋白']
train_label5=train_label['血清低密度脂蛋白']
feat_history=pd.read_csv('feat_history_4_21_18_24.csv')

train_data=pd.merge(train_id,feat_history,on='vid',how='left')
test_data=pd.merge(test_id,feat_history,on='vid',how='left')
feat_history_second=pd.read_csv('feat_second_history_4_21_19_23.csv')

train_data=pd.merge(train_data,feat_history_second,on='vid',how='left')
test_data=pd.merge(test_data,feat_history_second,on='vid',how='left')
feat_history_float=pd.read_csv('data_history_float_mean_4_23.csv')
train_data=pd.merge(train_data,feat_history_float,on='vid',how='left')
test_data=pd.merge(test_data,feat_history_float,on='vid',how='left')
del train_data['vid']
del test_data['vid']
#######################################################################################################


#import lightgbm as lgb
# lgb算法
#train = lgb.Dataset(x_train, label=y_train)
#test = lgb.Dataset(x_val, label=y_val)

from sklearn.model_selection import train_test_split
#preds_sub = gbm.predict(testt_feat)
import xgboost as xgb
x_train,x_val,y_train,y_val=train_test_split(train_data,train_label1,test_size=0.2,random_state=100)
print ('start running ....')
dtrain = xgb.DMatrix(x_train,label=y_train)
dval = xgb.DMatrix(x_val,label=y_val)
param = {'learning_rate' : 0.1,
        'n_estimators': 1000,
        'max_depth': 4,
        'min_child_weight': 7,
        'gamma': 0,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'eta': 0.05,
        'silent': 1,
        }

num_round =200
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=50)
dtest = xgb.DMatrix(test_data)
y1 = bst.predict(dtest)
x_train,x_val,y_train,y_val=train_test_split(train_data,train_label2,test_size=0.2,random_state=100)
print ('start running ....')
dtrain = xgb.DMatrix(x_train,label=y_train)
dval = xgb.DMatrix(x_val,label=y_val)
param = {'learning_rate' : 0.1,
        'n_estimators': 1000,
        'max_depth': 4,
        'min_child_weight': 7,
        'gamma': 0,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'eta': 0.05,
        'silent': 1,
        }

num_round =200
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=50)
dtest = xgb.DMatrix(test_data)
y2 = bst.predict(dtest)
test_data['y1']=y1
test_data['y2']=y2
#test_data['y5']=y5
train_data['y1']=train_label1
train_data['y2']=train_label2
#Qtrain_data['y5']=train_label5
x_train,x_val,y_train,y_val=train_test_split(train_data,train_label3,test_size=0.2,random_state=100)
print ('start running ....')
dtrain = xgb.DMatrix(x_train,label=y_train)
dval = xgb.DMatrix(x_val,label=y_val)
param = {'learning_rate' : 0.1,
        'n_estimators': 1000,
        'max_depth': 3,
        'min_child_weight': 8,
        'gamma': 0,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'eta': 0.05,
        'silent': 1,
        }

num_round =150
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=50)
dtest = xgb.DMatrix(test_data)
y3 = bst.predict(dtest)

x_train,x_val,y_train,y_val=train_test_split(train_data,train_label4,test_size=0.2,random_state=100)
print ('start running ....')
dtrain = xgb.DMatrix(x_train,label=y_train)
dval = xgb.DMatrix(x_val,label=y_val)
param = {'learning_rate' : 0.1,
        'n_estimators': 1000,
        'max_depth': 4,
        'min_child_weight': 7,
        'gamma': 0,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'eta': 0.05,
        'silent': 1,
        }

num_round =250
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=50)
dtest = xgb.DMatrix(test_data)
y4 = bst.predict(dtest)

x_train,x_val,y_train,y_val=train_test_split(train_data,train_label5,test_size=0.2,random_state=100)
print ('start running ....')
dtrain = xgb.DMatrix(x_train,label=y_train)
dval = xgb.DMatrix(x_val,label=y_val)
param = {'learning_rate' : 0.1,
        'n_estimators': 1000,
        'max_depth': 4,
        'min_child_weight': 7,
        'gamma': 0,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'eta': 0.05,
        'silent': 1,
        }

num_round =200
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=50)
dtest = xgb.DMatrix(test_data)
y5 = bst.predict(dtest)

test_id['y1']=y1
test_id['y2']=y2
test_id['y3']=y3
test_id['y4']=y4
test_id['y5']=y5
test_id.to_csv('tijiao_new_4_23_19_31_xgb.csv',index=False,header=None)
