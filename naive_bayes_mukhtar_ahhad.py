# -------------------------------------------------------------------------
# AUTHOR: Ahhad Mukhtar
# FILENAME: naive_bayes_mukhtar_ahhad.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hrs
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
db = []
X = []
Y = []

# reading the training data in a csv file
# --> add your Python code here
with open(r"C:\Users\fourf\Documents\SchoolDocuments\CS4210 Notes & HW\Assignment2_Mukhtar_Ahhad\weather_training.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
# transform the original training features to numbers and add them to the 4D array X.
# For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
outlook_dict = {"Sunny": 1, "Overcast": 2, "Rain": 3}
humidity_bin_dict = {"High": 1, "Normal": 2}
wind_dict = {"Weak": 1, "Strong": 2}
temp_dict = {"Hot": 1, "Mild": 2, "Cool": 3}
play_bin_dict = {"Yes": 1, "No": 2}



#-->add your Python code here
    #Outlook,Temperature,Humidity,Wind,PlayTennis will all have dictionaries that will be appended to X
for data in db:
    X.append([outlook_dict[data[1]], humidity_bin_dict[data[2]], wind_dict[data[3]], temp_dict[data[4]]])
    Y.append([play_bin_dict[data[5]]])
#skip over the days and go straight to outlook and the rest of the attributes
# X =

# transform the original training classes to numbers and add them to the vector Y.
# For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# Y =
X_Test = []
Y_Test = []
db_Test = []

outlook_dict_test = {"Sunny": 1, "Overcast": 2, "Rain": 3}
humidity_bin_dict_test = {"High": 1, "Normal": 2}
wind_dict_test = {"Weak": 1, "Strong": 2}
temp_dict_test = {"Hot": 1, "Mild": 2, "Cool": 3}
play_bin_dict_test = {"Yes": 1, "No": 2}

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the test data in a csv file
# --> add your Python code here
with open(r"C:\Users\fourf\Documents\SchoolDocuments\CS4210 Notes & HW\Assignment2_Mukhtar_Ahhad\weather_test.csv", 'r') as csvfile2:
    reader2 = csv.reader2(csvfile2)
    for j, row in enumerate(reader2):
        if j > 0:  # skipping the header
            db_Test.append(row)
confidence_floor = 0.75

for data in db_Test:
    X_Test.append([outlook_dict_test[data[1]], humidity_bin_dict_test[data[2]], wind_dict_test[data[3]], temp_dict_test[data[4]]])
    Y_Test.append([play_bin_dict_test[data[4]]])
# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(
    15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))
class_prediction = clf.predict_proba([X_Test[0]])[0]
# use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
# --> add your Python code here

if class_prediction >= confidence_floor:
    print("Confidence is {}".format(class_prediction))