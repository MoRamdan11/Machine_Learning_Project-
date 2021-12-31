# -*- coding: utf-8 -*-
"""Copy of jko.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JdwW01Cj7oS4HI__hr_1JETq9vaYaMkR
"""

# Importing the libraries

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
# Part 1 - Data Preprocessing

# Importing the dataset

dataset = pd.read_csv('employee_attrition_test.csv')
#X = dataset.iloc[:, 3:-1].values
#y = dataset.iloc[:, -1].values
#print(X)
#print(y)
print(dataset.shape)
print(dataset.info())
print("/////////////////////////////////////////////////////////////////")
dataset.Department
print("///////////////////////////////////////////////////////")
dataset.head()
print("////////////////////////////")
q1=dataset.quantile(0.25)
q2=dataset.quantile(0.75)
IQR=q2-q1
print(IQR)
print("//////////////////////")
#to show if that is big differense between max and q3
print((dataset<q1-1.5*IQR)|(dataset>q2+1.5*IQR))

dataset.head(272)

dataset.head(272
            )[['Gender','HourlyRate','JobInvolvement','JobLevel','JobRole','JobSatisfaction','MaritalStatus','MonthlyIncome','MonthlyRate','NumCompaniesWorked','Over18','OverTime','PercentSalaryHike','PerformanceRating']]

#dataset=dataset.drop('hourInSecond')
#pd.drop('hourInSecond'
#dataset.drop('hourInSecond' , inplace=True, axis=1)
#dataset['hourInSecond']

q1=dataset.quantile(0.25)
q2=dataset.quantile(0.75)
IQR=q2-q1
print(IQR)
print((dataset<q1-1.5*IQR)|(dataset>q2+1.5*IQR))
print(dataset.skew())

print(dataset['YearsSinceLastPromotion'].quantile(0.20))
print(dataset['YearsSinceLastPromotion'].quantile(0.80))
print(dataset.skew())
Q1=dataset['YearsSinceLastPromotion'].quantile(0.25)
Q3=dataset['YearsSinceLastPromotion'].quantile(0.75)
IQR=Q3-Q1
Min= Q1 - 1.5 * IQR
Max= Q3 + 1.5 * IQR

dataset['YearsSinceLastPromotion'] = np.where(dataset['YearsSinceLastPromotion'] <Min, 0.0,dataset['YearsSinceLastPromotion'])
dataset['YearsSinceLastPromotion'] = np.where(dataset['YearsSinceLastPromotion'] >Max, 4.0,dataset['YearsSinceLastPromotion'])
print(dataset['YearsSinceLastPromotion'].skew())
import matplotlib.pyplot as plt
plt.boxplot(dataset['YearsSinceLastPromotion'])

# Encoding categorical data
# Label Encoding the "Marital" column
dataset.info() 
from sklearn.preprocessing import LabelEncoder
 
l1= LabelEncoder()
dataset['Department']=l1.fit_transform(dataset['Department'])
dataset['EducationField']=l1.fit_transform(dataset['EducationField'])
dataset['Gender']=l1.fit_transform(dataset['Gender'])
dataset['JobRole']=l1.fit_transform(dataset['JobRole'])
#dataset['Over18']=l1.fit_transform(dataset['Over18'])
dataset['OverTime']=l1.fit_transform(dataset['OverTime'])
dataset['JobRole'].unique()

#replace strings to numbers
dataset['MaritalStatus']=dataset['MaritalStatus'].replace('Single',0)
dataset['MaritalStatus']=dataset['MaritalStatus'].replace('Married',1)
dataset['MaritalStatus']=dataset['MaritalStatus'].replace('Divorced',2)
dataset['Over18']=dataset['Over18'].replace('Y',1)
#dataset['OverTime']=dataset['OverTime'].replace('Yes',1)
#dataset['OverTime']=dataset['OverTime'].replace('No',0)
dataset['BusinessTravel']=dataset['BusinessTravel'].replace('Non-Travel',0 )
dataset['BusinessTravel']=dataset['BusinessTravel'].replace('Travel_Rarely',1 )
dataset['BusinessTravel']=dataset['BusinessTravel'].replace('Travel_Frequently',2 )

dataset['OverTime'].unique()

#handel null value
dataset['Age'].fillna(value=dataset['Age'].mean(),inplace=True)
dataset['BusinessTravel'].fillna(value=-1,inplace=True)
dataset['DistanceFromHome'].fillna(value=dataset['DistanceFromHome'].mean(),inplace=True)
dataset['MaritalStatus'].fillna(value=-1,inplace=True)
dataset['DailyRate'].fillna(value= dataset['DailyRate'].mean(),inplace=True)
#search if there are any null or not
dataset.isna().any()

dataset['OverTime'].unique()

dataset.head(435)[['Gender','HourlyRate','JobInvolvement','JobLevel','JobRole','JobSatisfaction','MaritalStatus','MonthlyIncome','MonthlyRate','NumCompaniesWorked','Over18','OverTime','PercentSalaryHike','PerformanceRating']]

dataset=dataset.drop_duplicates()
dataset

from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

#X = dataset.iloc[:,:33].values
#y = dataset.iloc[:,3].values 

#features = dataset.drop(["OverTime"], axis=1).values
features =dataset.iloc[:,:-1].values
target = dataset.iloc[:,21].values
pca =PCA(n_components=30)
X2=pca.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(X2,target, test_size=0.25,random_state = 0)
print(X_test)
y_test

X_train.shape



y_test

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)

from sklearn.svm import SVC

c =SVC(C= 0.1, kernel='linear', gamma= 0.1)
c.fit(X_train, y_train )
#svc_model.fit(X_train, y_train)

#from sklearn.model_selection import train_test_split
#target = dataset["Department"]
#features = dataset.drop(["Department"], axis=1)
#X_train, X_test, y_train, y_test = train_test_split(features,target, test_size = 0.25, random_state = 0)
# To calculate the accuracy score of the model

#print(c.predict(sc.transform([[49.0,2.0,1064.0,1,2.000000,1,1,1,1941,2,1,42,3,5,5,4,1.0,19161,13738,3,1,15,3,4,80,0,28,3,3,5,4,4.0,3]])))
print(y_test )

#y_train



#target=y_train
#y_pred =c.predict(X_train)
#print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

#plotconfusion( y_pred,y_test)

"""model = sequential
model.compile(optimizer'adam',loss='binary_crossentropy',metrics=['accuracy'])
"""

from tensorflow import keras
from keras import regularizers
model = keras.Sequential([keras.layers.Flatten(),
        keras.layers.Dense(100,activation='relu',kernel_regularizer=regularizers.l2(0.0001)),
        keras.layers.Dense(10,activation='sigmoid')                  
                         
                         ])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.optimizer.lr=0.001
mo=model.fit(X_train,y_train,batch_size=32,epochs=5)

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_pred = c.predict(X_test).ravel()
nn_fpr_keras, nn_tpr_keras, nn_thresholds_keras = roc_curve(y_test  , y_pred)
auc_keras = auc(nn_fpr_keras, nn_tpr_keras)
plt.plot(nn_fpr_keras, nn_tpr_keras, marker='.', label='Neural Network (auc = %0.3f)' % auc_keras)

from sklearn.metrics import confusion_matrix, accuracy_score

y_pred = c.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)

accuracy_score(y_test, y_pred)

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC  
#target = dataset["Department"]
#features = dataset.drop(["Department"], axis=1)
#X_train, X_test, y_train, y_test = train_test_split(features,target, test_size = 0.2, random_state = 0)
# Building a Support Vector Machine on train data
#svc_model = SVC(C= 0.1, kernel='linear', gamma= 0.01)
#svc_model.fit(X_train, y_train)
prediction = c.predict(X_test )
# check the accuracy on the training set
print( c.score(X_train, y_train))
print( c.score(X_test, y_test ))
cm = confusion_matrix(y_test,prediction)
print(cm)
accuracy_score(y_test,prediction)

from sklearn.metrics  import roc_auc_score
from sklearn.metrics  import roc_curve
log_roc=roc_auc_score(y_test, prediction)
fpr,tpr,thre =roc_curve(y_test,c.predict(X_test))

y_train

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

train_sizes, train_scores, test_scores = learning_curve(c,
                                                         X_train,  y_train, cv=10, scoring='accuracy',
                                                        train_sizes=np.linspace(0.01, 1.0, 50))
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.subplots(1, figsize=(6,6))
plt.plot(train_sizes, train_mean, '--', color='blue',  label="Training score")
plt.plot(train_sizes, test_mean, color='blue', label="Cross-validation score")

plt.title("Learning Curve")
plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), plt.legend(loc="best")
plt.tight_layout()
plt.show()

from sklearn.metrics  import roc_auc_score
from sklearn.metrics  import roc_curve ,auc
import matplotlib.pyplot as plt
y_pred=c.predict(X_test).ravel()
nn_fpr_keras,nn_tpr_keras,nn_thresholds_keras=roc_curve(y_test,prediction)
auc_keras=auc(nn_fpr_keras,nn_tpr_keras)
plt.plot(nn_fpr_keras,nn_tpr_keras, marker='.',label='  SVM (auc=%0.3f)'%auc_keras)

