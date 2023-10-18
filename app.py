# Developer 3 - Parte 1
'''
Generamos Variables dependientes e independientes
'''
variables=['Pclass', 'Age', 'Sex', 'SibSp', 'Parch', 'Fare', 'CabinBool', 'Embarked_C',
'Embarked_S', 'Embarked_Q']
X = train_df[variables]
y = train_df['Survived']
# Developer 3 - Parte 2
'''
Creamos el modelo
'''
X = train_df[['Pclass', 'Age', 'Sex', 'SibSp', 'Parch', 'Fare', 'CabinBool', 'Embarked_C',
'Embarked_S', 'Embarked_Q]]
y = train_df[[Survived']]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=0)
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)