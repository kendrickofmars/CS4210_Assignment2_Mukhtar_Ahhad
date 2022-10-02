# -------------------------------------------------------------------------
# AUTHOR: Ahhad Mukhtar
# FILENAME: decision_tree_2_Mukhtar_Ahhad
# SPECIFICATION: decision tree that iterates through test and training data and makes predictions which we check the accuracy of
# FOR: CS 4210- Assignment #2
# TIME SPENT: 6 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = [
    r'C:\Users\fourf\Documents\SchoolDocuments\CS4210 Notes & HW\Assignment2_Mukhtar_Ahhad\contact_lens_training_1.csv',
    r'C:\Users\fourf\Documents\SchoolDocuments\CS4210 Notes & HW\Assignment2_Mukhtar_Ahhad\contact_lens_training_2.csv',
    r'C:\Users\fourf\Documents\SchoolDocuments\CS4210 Notes & HW\Assignment2_Mukhtar_Ahhad\contact_lens_training_3.csv']
count = 0
for ds in dataSets:
    count += 1
    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    # X =
age_dict = {"Young": 1, "Prepresbyopic": 2, "Presbyopic": 3}
spectacle_dict = {"Myope": 1, "Hypermetrope": 2}
astigmatism_dict = {"Yes": 1, "No": 2}
tear_dict = {"Normal": 1, "Reduced": 2}
lens_bin_dict = {"Yes": 1, "No": 2}

# all dictionaries here are for training data
for data in dbTraining:
    X.append([age_dict[data[0]], spectacle_dict[data[1]], astigmatism_dict[data[2]], tear_dict[data[3]]])
    # transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> addd your Python code here
    Y.append(lens_bin_dict[data[4]])

dbTest = []  # we will add the test data in here
X_Test = []
Y_Test = []
age_dict_2 = {"Young": 1, "Prepresbyopic": 2, "Presbyopic": 3}
spectacle_dict_2 = {"Myope": 1, "Hypermetrope": 2}
astigmatism_dict_2 = {"Yes": 1, "No": 2}
tear_dict_2 = {"Normal": 1, "Reduced": 2}
lens_bin_dict_2 = {"Yes": 1, "No": 2}
# all dictionaries here are for test data
# loop your training and test tasks 10 times here
for i in range(10):
    # fitting the decision tree to the data setting max_depth=3
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
    clf = clf.fit(X, Y)

    # read the test data and add this data to dbTest
    # --> add your Python code here
    # dbTest =
with open(r"C:\Users\fourf\Documents\SchoolDocuments\CS4210 Notes & HW\Assignment2_Mukhtar_Ahhad\contact_lens_test.csv",
          'r') as csvfile2:
    reader2 = csv.reader(csvfile2)
    for i, row in enumerate(reader2):
        if i > 0:  # skipping the header
            dbTest.append(row)
    true_positive_test = 0
    true_negative_test = 0
    false_positive_test = 0
    false_negative_test = 0  # counters of true positive/negative, & false positive/negative
    lowest_acc_test = 1

    true_positive_training = 0
    false_positive_training = 0
    true_negative_training = 0
    false_negative_training = 0
    lowest_acc_training = 1

    for data in dbTest:
        X_Test.append(
            [age_dict_2[data[0]], spectacle_dict_2[data[1]], astigmatism_dict_2[data[2]], tear_dict_2[data[3]]])
        Y_Test.append(lens_bin_dict_2[data[4]])

        # transform the features of the test instances to numbers following the same strategy done during training,
        # and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
        # where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        # --> add your Python code here
        class_predicted_training = \
            clf.predict([[age_dict[data[0]], spectacle_dict[data[1]], astigmatism_dict[data[2]], tear_dict[data[3]]]])[
                0]
        class_predicted = clf.predict(
            [[age_dict_2[data[0]], spectacle_dict_2[data[1]], astigmatism_dict_2[data[2]], tear_dict_2[data[3]]]])[0]

        # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        # --> add your Python code here

        # same thing for test data
        if class_predicted_training == lens_bin_dict[data[4]]:
            true_positive_training += 1
        if class_predicted_training == 1 and lens_bin_dict[data[4]] != 1:
            false_positive_training += 1
        if class_predicted_training == 0 and class_predicted_training == lens_bin_dict[data[4]]:
            true_negative_training += 1
        if class_predicted_training == 0 and lens_bin_dict[data[4]] != 0:
            false_negative_training += 1

        # if class_predicted == 1 and class_predicted == lens_bin_dict_2[data[4]]:
        if class_predicted == lens_bin_dict_2[data[4]]:
            true_positive_test += 1
        if class_predicted == 1 and lens_bin_dict_2[data[4]] != 1:
            false_positive_test += 1
        if class_predicted == 0 and class_predicted == lens_bin_dict_2[data[4]]:
            true_negative_test += 1
        if class_predicted == 0 and lens_bin_dict_2[data[4]] != 0:
            false_negative_test += 1

        prediction_accuracy_training = (true_positive_training + true_negative_training) / (
                false_negative_training + false_positive_training + true_negative_training + true_positive_training)
        prediction_accuracy_test = (true_positive_test + true_negative_test) / (
                false_negative_test + false_positive_test + true_negative_test + true_positive_test)

        # find the lowest accuracy of this model during the 10 runs (training and test set)
        # --> add your Python code here
        if prediction_accuracy_test < lowest_acc_test:
            lowest_acc_test = prediction_accuracy_test
        if prediction_accuracy_training < lowest_acc_training:
            lowest_acc_training = prediction_accuracy_training
        # print the lowest accuracy of this model during the 10 runs (training and test set).
        # your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
        # --> add your Python code here
        print('Lowest accuracy for training set {} is {}'.format(ds, lowest_acc_training))
        print('Lowest accuracy for test set is: {}'.format(lowest_acc_test))
