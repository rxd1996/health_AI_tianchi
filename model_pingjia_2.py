
import pandas as pd

test_id=pd.read_csv('[new] meinian_round1_test_a_20180409.csv',encoding='gbk',usecols=['vid'])

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
del train_data['vid']
del test_data['vid']
##################################################################################################
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
x_train,x_val,y_train,y_val=train_test_split(train_data,train_label3,test_size=0.2,random_state=100)
import operator


def ceate_feature_map(features):
    outfile = open('xgb.fmap', 'w')
    i = 0
    for feat in features:
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
        i = i + 1
    outfile.close()
features = [x for x in train_data.columns]
ceate_feature_map(features)

import xgboost as xgb
from  xgboost import plot_importance
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
bst=xgb.train(plst,dtrain,num_round,evallist,early_stopping_rounds=50)
dtest = xgb.DMatrix(test_data)
y3 = bst.predict(dtest)
plot_importance(bst)
plt.show()
importance = bst.get_fscore(fmap='xgb.fmap')
importance = sorted(importance.items(), key=operator.itemgetter(1))