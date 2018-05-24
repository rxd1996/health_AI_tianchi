
import pandas as pd

test_id=pd.read_csv('meinian_round1_test_a_20180408.csv',encoding='gbk',usecols=['vid'])
#test_id=test_id[0:7637]
train_id=pd.read_csv('train_data.csv',usecols=['vid'])
#train_id=train_id[0:7637]
train_label=pd.read_csv('train_data.csv',usecols=[1,2,3,4,5])

train_label1=train_label['收缩压']
train_label2=train_label['舒张压']
train_label3=train_label['血清甘油三酯']
train_label4=train_label['血清高密度脂蛋白']
train_label5=train_label['血清低密度脂蛋白']
feat_history=pd.read_csv('feat_history_4_21.csv')

train_data=pd.merge(train_id,feat_history,on='vid',how='left')
test_data=pd.merge(test_id,feat_history,on='vid',how='left')
feat_history_second=pd.read_csv('feat_second_history_4_21_19_23.csv')

train_data=pd.merge(train_data,feat_history_second,on='vid',how='left')
test_data=pd.merge(test_data,feat_history_second,on='vid',how='left')
del train_data['vid']
del test_data['vid']
#######################################################################################################
#test_id.to_csv('tijiao.csv',index=False,header=None)

from sklearn.model_selection import train_test_split
x_train,x_val,y_train,y_val=train_test_split(train_data,train_label3,test_size=0.2,random_state=100)
import lightgbm as lgb
# lgb算法
#train = lgb.Dataset(x_train, label=y_train)
#test = lgb.Dataset(x_val, label=y_val)


#preds_sub = gbm.predict(testt_feat)
import xgboost as xgb
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

num_round =100
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=30)
dtest = xgb.DMatrix(x_val)
y3 = bst.predict(dtest)
true=pd.DataFrame(y_val)

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

num_round =100
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=30)
dtest = xgb.DMatrix(x_val)
y4 = bst.predict(dtest)

true['y4']=y_val

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

num_round =100
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=30)
dtest = xgb.DMatrix(x_val)
y5 = bst.predict(dtest)
true['y5']=y_val

#test_data['y3']=y3
#test_data['y4']=y4
#test_data['y5']=y5
#train_data['y3']=train_label3
#train_data['y4']=train_label4
#train_data['y5']=train_label5

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

num_round =100
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=30)
dtest = xgb.DMatrix(x_val)
y1 = bst.predict(dtest)
true['y1']=y_val
#del test_data['y3']
#del test_data['y4']
#del test_data['y5']
#del train_data['y3']
#del train_data['y4']
#del train_data['y5']
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

num_round =100
plst = list(param.items())
plst += [('eval_metric', 'rmse')]
evallist = [(dval, 'eval'), (dtrain, 'train')]
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=30)
dtest = xgb.DMatrix(x_val)
y2 = bst.predict(dtest)
true['y2']=y_val
#test_id['y1']=y1
#test_id['y2']=y2
#test_id['y3']=y3
#test_id['y4']=y4
#test_id['y5']=y5

pre=pd.DataFrame(y3)
pre['y4']=y4
pre['y5']=y5
pre['y1']=y1
pre['y2']=y2

pre.columns=['a','b','c','d','e']
true.columns=['a','b','c','d','e']
from math import log1p,pow
def calc_logloss(true_df,pred_df):
    loss_sum=0
    rows=true_df.shape[0]
    for c in true_df.columns:
        #预测结果必须要>0,否则log函数会报错，导致最终提交结果没有分数
        true_df[c]=true_df[c].apply(lambda x:log1p(x))
        pred_df[c]=pred_df[c].apply(lambda x:log1p(x))
        true_df[c+'new']=pred_df[c]-true_df[c]
        true_df[c+'new']=true_df[c+'new'].apply(lambda x:pow(x,2))
        loss_item=(true_df[c+'new'].sum())/rows
        loss_sum+=loss_item
        print('%s的loss：%f'%(c,loss_item))
    print('总的loss：',loss_sum)
calc_logloss(true,pre)
