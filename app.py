
'''
Importamos librerías
'''

survived_class = train_df[train_df['Survived']==1]['Pclass'].value_counts(sort=False)
dead_class = train_df[train_df['Survived']==0]['Pclass'].value_counts(sort=False)
class_df = pd.DataFrame([survived_class,dead_class],index=['Survived','Dead'])
class_df.plot(kind='bar', stacked=True)
plt.xlabel('Class')
plt.ylabel('Number of passengers')
plt.title('Survival rate by class')
st.pyplot()
'''
Visualizamos la variable Sexo
'''
survived_sex = train_df[train_df['Survived']==1]['Sex'].value_counts(sort=False)
dead_sex = train_df[train_df['Survived']==0]['Sex'].value_counts(sort=False)
sex_df = pd.DataFrame([survived_sex,dead_sex],index=['Survived','Dead'])
sex_df.plot(kind='bar', stacked=True)
plt.xlabel('Sex')
plt.ylabel('Number of passengers')
plt.title('Survival rate by sex')
st.pyplot()

'''
Visualizamos la variable Embarked
'''
survived_embark =
train_df[train_df['Survived']==1]['Embarked'].value_counts(sort=False)
dead_embark = train_df[train_df['Survived']==0]['Embarked'].value_counts(sort=False)
embark_df =
pd.DataFrame([survived_embark,dead_embark],index=['Survived','Dead'])
embark_df.plot(kind='bar', stacked=True)
plt.xlabel('Embarked')
plt.ylabel('Number of passengers')
plt.title('Survival rate by port of embarkation')
st.pyplot()

'''
Visualizamos la importancia de las variables
'''
survived_embark =
train_df[train_df['Survived']==1]['Embarked'].value_counts(sort=True)
dead_embark = train_df[train_df['Survived']==0]['Embarked'].value_counts(sort=False)
st.write('Visualización del modelo y datos')
st.write('Importancia de características en el modelo')
st.bar_chart(importances)
=======
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
Importamos librerías
'''
import pandas
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
st.set_option('deprecation.showPyplotGlobalUse', False)
'''
Cargamos los datos
'''
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')
train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})
test_df['Sex'] = test_df['Sex'].map({'male': 0, 'female': 1})
train_df['Sex'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Sex'].fillna(test_df['Age'].mean(), inplace=True)
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(), inplace=True)
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)
test_df['Embarked'].fillna(test_df['Embarked'].mode()[0], inplace=True)
train_df['CabinBool'] = (train_df['Cabin'].notnull().astype('int'))
test_df['CabinBool'] = (test_df['Cabin'].notnull().astype('int'))
train_df = pd.concat([train_df, pd.get_dummies(train_df['Embarked'],
prefix='Embarked')], axis=0)
test_df = pd.concat([test_df, pd.get_dummies(test_df['Embarked'], prefix='Embarked')],
axis=0)
train_df = pd.concat([train_df, pd.get_dummies(train_df['Embarked'],
prefix='Embarked')], axis=1)
test_df = pd.concat([test_df, pd.get_dummies(test_df['Embarked'], prefix='Embarked')],
axis=1)
test_df['Fare'].fillna(test_df['Fare'].dropna().mean(), inplace=True)


