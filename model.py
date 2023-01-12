import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score
import pickle
recruit= pd.read_csv("train.csv")
recruit=recruit.drop(['sl_no'],axis=1)
recruit.head()

# transfer categorical vaeiables to dummy variables

recruit.loc[recruit['gender'] == 'M', 'gender'] = 1.0
recruit.loc[recruit['gender'] == 'F', 'gender'] = 0.0

recruit.loc[recruit['status'] == 'Placed', 'status'] = 1
recruit.loc[recruit['status'] == 'Not Placed', 'status'] = 0

recruit.loc[recruit['workex'] == 'Yes', 'workex'] = 1.0
recruit.loc[recruit['workex'] == 'No', 'workex'] = 0.0

recruit.loc[recruit['ssc_b'] == 'Others', 'ssc_b'] = 0.0
recruit.loc[recruit['ssc_b'] == 'Central', 'ssc_b'] = 1.0

recruit.loc[recruit['hsc_b'] == 'Others', 'hsc_b'] = 0.0
recruit.loc[recruit['hsc_b'] == 'Central', 'hsc_b'] = 1.0


recruit.loc[recruit['specialisation'] == 'Mkt&HR', 'specialisation'] = 0.0
recruit.loc[recruit['specialisation'] == 'Mkt&Fin', 'specialisation'] = 1.0

categorical_var = ['hsc_s','degree_t']


# create dummy variables for all the other categorical variables

for variable in categorical_var:
# #     fill missing data
#     recruit[variable].fillna('Missing',inplace=True)
#     create dummy variables for given columns
    dummies = pd.get_dummies(recruit[variable],prefix=variable)
#     update data and drop original columns
    recruit = pd.concat([recruit,dummies],axis=1)
    recruit.drop([variable],axis=1,inplace=True)

print(recruit.head())
x_lr = recruit.drop(['status','salary'], axis=1)
y_lr = recruit['status'].astype(float)

# split train and test dataset
train_x, test_x, train_y, test_y = train_test_split(x_lr,y_lr , test_size=0.25, random_state=31)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train_x, train_y)

rf = RandomForestRegressor(200, oob_score=True,max_features='sqrt',n_jobs=-1, random_state=42,min_samples_leaf=1)
rf.fit(train_x,train_y)
rs=[lr,rf]


pickle.dump(rs,open('model_fin.pkl','wb'))

