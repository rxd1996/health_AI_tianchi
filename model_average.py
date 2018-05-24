import pandas as pd
xgb_results=pd.read_csv('tijiao_new_5_6_11_b_xgb.csv',header=None)
lgb_results=pd.read_csv('tijiao_new_5_6_b_lgb.csv',header=None)
cat_results=pd.read_csv('tijiao_new_5_6_B_catboost.csv',header=None)
#xgb_results.columns={'vid','a','b','c','d','e'}
#lgb_results.columns={'vid','a','b','c','d','e'}
#c e b vid a
def change_float(df1,df2,df3):
    df1[1].map(lambda x:float(x))
    df2[1].map(lambda x: float(x))
    df3[1].map(lambda x: float(x))
    df1[2].map(lambda x: float(x))
    df2[2].map(lambda x: float(x))
    df3[2].map(lambda x: float(x))
    df1[3].map(lambda x: float(x))
    df2[3].map(lambda x: float(x))
    df3[3].map(lambda x: float(x))
    df1[4].map(lambda x: float(x))
    df2[4].map(lambda x: float(x))
    df3[4].map(lambda x: float(x))
    df1[5].map(lambda x: float(x))
    df2[5].map(lambda x: float(x))
    df3[5].map(lambda x: float(x))
    return df1,df2,df3
xgb_results,lgb_results,cat_results=change_float(xgb_results,lgb_results,cat_results)
xgb_results['vid']=xgb_results[0]
del xgb_results[0]
xgb_results['收缩压']=(0.2*xgb_results[1]+0.5*lgb_results[1]+0.3*cat_results[1])
del xgb_results[1]

xgb_results['舒张压']=(0.2*xgb_results[2]+0.5*lgb_results[2]+0.3*cat_results[2])
del xgb_results[2]
xgb_results['bb1']=(0.2*xgb_results[3]+0.5*lgb_results[3]+0.3*cat_results[3])
del xgb_results[3]
xgb_results['aaa']=(0.2*xgb_results[4]+0.5*lgb_results[4]+0.3*cat_results[4])
del xgb_results[4]
xgb_results['aew1']=(0.2*xgb_results[5]+0.5*lgb_results[5]+0.3*cat_results[5])
del xgb_results[5]

xgb_results.to_csv('model_average_by_lgb_xgb_cat_0_5_0_3_0_2_b_no_choicefeat.csv',header=None,index=None)
