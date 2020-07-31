from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 

#Use normal Kneighbors model to compare to my model

col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.csv",names=col)
print(iris.head())

x=iris.iloc[:,:4]
y=iris["type"]

neigh=KNeighborsClassifier(n_neighbors=9)
neigh.fit(iris.iloc[:,:4],iris["type"])

test1= [[1,.3,1.5,1.5]]
#Setosa
print(test1)
print("predicted:",neigh.predict(test1))
print("neighbors",neigh.kneighbors(test1))


test2 = [[3, 6, 5, 2]]
# Virginica
test2 = pd.DataFrame(test2)
print(test2)
print("predicted:",neigh.predict(test2))
print("neighbors",neigh.kneighbors(test2))


test3 = [[1, 8, 4, 2.3]]
test3 = pd.DataFrame(test3)
print(test3)
print("predicted:",neigh.predict(test3))
print("neighbors",neigh.kneighbors(test3))

