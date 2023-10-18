'''
Visualizamos la variable Clase
'''
survived_class = train_df[train_df['Survived']==1]['Pclass'].value_counts(sort=False)
dead_class = train_df[train_df['Survived']==0]['Pclass'].value_counts(sort=False)
class_df = pd.DataFrame([survived_class,dead_class],index=['Survived','Dead'])
class_df.plot(kind='bar', stacked=True)
plt.xlabel('Class')
plt.ylabel('Number of passengers')
plt.title('Survival rate by class')
st.pyplot()