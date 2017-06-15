from sklearn import tree

#[height, weight, shoe size]

X=[[181,80,7],[177,70,4],[160,60,5],[154,54,6],[166,65,8],[190,90,9],[175,64,10],[177,70,7],[159,55,9],[171,75,6],[181,85,8]]
Y=['male','female','female','female','male','male','male','female','male','female','male']

clf=tree.DecisionTreeClassifier();
clf.fit(X,Y)
prediction=clf.predict([[168,57,8]])
print prediction
