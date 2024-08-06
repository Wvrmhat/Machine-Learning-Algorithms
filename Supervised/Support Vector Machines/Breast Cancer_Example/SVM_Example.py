import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()

print(cancer.feature_names)
print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)

print(x_train, y_train)

classes = ['malignant' 'benign']

# classifier
#parameters with kernel being used and C(soft-margin)
clf = svm.SVC(kernel="linear", C=4)
clf.fit(x_train, y_train)

y_predict = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_predict)
print("Accuracy: \n")
print(acc)
print("-"*100)

# Comparing KNN to SVM by checking accuracy
print("KNN: \n")
clf_k = KNeighborsClassifier(n_neighbors=9)
clf_k.fit(x_train, y_train)
y_predictKNN = clf_k.predict(x_test)
acc_knn = metrics.accuracy_score(y_test, y_predictKNN)
print(f"Accuracy {acc_knn}")

