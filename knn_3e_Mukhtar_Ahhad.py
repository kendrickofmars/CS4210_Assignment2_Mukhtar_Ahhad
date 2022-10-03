# -------------------------------------------------------------------------
# AUTHOR: Ahhad Mukhtar
# FILENAME: knn_Mukhtar_Ahhad
# SPECIFICATION: 1NN LOOCV
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
X = []
Y = []
num_right = 0
num_wrong = 0 #number of correct versus correct, we will use these counters
#for errno calculation
# reading the data in a csv file
with open(r"C:\Users\fourf\Documents\SchoolDocuments\CS4210 Notes & HW\Assignment2_Mukhtar_Ahhad\binary_points.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

# loop your data to allow each instance to be your test set
for i, instance in enumerate(db):
    # add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    # For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages

    # transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    # For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages
    transformation_dict = {"+": 1, "-": 2}
    # --> add your Python code here
    for j in db:
       # X.append(float(db[i]),float(db[instance])) arg must real number not a list
        X.append([float(j[0]), float(j[1])])#wrap in brackets so argument is interpreted as one argument only
        Y.append(float(transformation_dict[j[2]]))
    testSample = X[i], Y[i] # instances of list X and list Y
    del X[i], Y[i] #removing test instance for LOO CV


    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    # use your test sample in this iteration to make the class prediction. For instance:
    # class_predicted = clf.predict([[1, 2]])[0]
    # --> add your Python code here
    class_predicted = clf.predict([testSample[0]])[0]
    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here
    if class_predicted == testSample[1]:
        num_right += 1
    elif class_predicted != testSample[1]:
        num_wrong += 1
# print the error rate
    errno = num_wrong / (num_wrong + num_right)
    print(errno)
# --> add your Python code here