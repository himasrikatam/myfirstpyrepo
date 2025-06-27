import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('diabetes.csv')
print(df.columns)
input = df.drop(['Outcome'], axis='columns')
output = df['Outcome']
# print(input.head())
X_train, X_test, y_train, y_test = train_test_split(input, output, test_size=0.2, random_state=1)
model = LogisticRegression()
model.fit(X_train,y_train)
logRegAccuracy=model.score(X_test,y_test)
print("LogR ",logRegAccuracy)
model1 = DecisionTreeClassifier()
model1.fit(X_train,y_train)
dtAccuracy = model1.score(X_test,y_test)
print("DT: ", dtAccuracy)
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
knnAccuracy = knn.score(X_test, y_test)
print("KNN: ",knnAccuracy)
modelRF = RandomForestClassifier(n_estimators=100, random_state=42)
modelRF.fit(X_train, y_train)
rfAccuracy = modelRF.score(X_test,y_test)
print("RF:",rfAccuracy)
with open('model.pkl','wb') as file:
    pickle.dump(modelRF,file)