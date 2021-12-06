#Import required modules
import numpy as np
from sklearn import datasets, linear_model, metrics, preprocessing


#Download KDD Cup 99 data set.
kdd = datasets.fetch_kddcup99()
print(kdd.data.shape) #(494021, 41) A dataset in scikit-learn is a dictionary-like object that holds all the data and some metadata about the data. This data is stored in the “.data” member, which is an (n_samples x n_features) array. In the case of supervised problem, one or more response variables are stored in the “.target” member. In kdd data set, there are 494,021 samples, and each of them has 41 features and 1 response variable.
print(kdd.target.shape) #(494021,)


#Target transformation
#There are many different attack types in this data set, each type is represented by a string. Our target is to detect network intrusion. The trained model should be able to classify a connection into normal connection or attack, but do not need to detect the attach type. So we need to transform the labels into class 0 or class 1
#print the network connection type, “normal” represent “good ”
#connection, the others represent network attack
print(set(kdd.target))
kdd.target = np.where(kdd.target == b'normal.', 0, 1)


#Feature transformation
#Because the second, third and fourth features are text variables, we need to transform them to numeric features
le = preprocessing.LabelEncoder()
for i in (1, 2, 3):
    kdd.data[:, i] = le.fit_transform(kdd.data[:, i])


#Split the data set into train and test part
train_data_percentage = 0.75
train_data_number = int(kdd.data.shape[0] * train_data_percentage)
train_data, train_target = kdd.data[:train_data_number], kdd.target[:train_data_number]
test_data, test_target = kdd.data[train_data_number:], kdd.target[train_data_number:]


#Create a logistic regression model object
#Logistic regression algorithm has already been implemented in Scikit-Learn package. We just need to create an instance of logistic regression class.
lr = linear_model.LogisticRegression()


#Fit the model on the data set
#Find the best solution for logistic regression on training data set
lr.fit(train_data, train_target)

print(lr.coef_) # the trained value for variable w

print(lr.intercept_) # the trained value for variable b

print(lr.classes_) # the label values for this model, 0 represent normal connection, 1 represent attack connection


#Evaluate the model’s performance on test data set
#The accuracy score function computes the accuracy, it computes the fraction of corrected predictions.
acc = metrics.accuracy_score(test_target, test_data)
print(acc)