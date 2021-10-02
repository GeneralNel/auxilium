import pandas as pd
# from sklearn import tree

scoreSum = 0

# Number of siblings
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

clfSiblings = tree.DecisionTreeClassifier()
clfSiblings = clfSiblings.fit(X, Y)

val = int(input("Enter val: "))
if val < 0: val = 0
if val > 9: val = 9

pred = clfSiblings.predict([[val]])
scoreSum += pred[0]


# Number of device
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
Y = [10, 10, 8, 8, 6, 6, 4, 4, 2, 2]

clfDevices = tree.DecisionTreeClassifier()
clfDevices = clfDevices.fit(X, Y)

val = int(input("Enter val: "))
if val < 0: val = 0
if val > 9: val = 9

pred = clfSiblings.predict([[val]])
scoreSum += pred[0]


# Income
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

clfIncome = tree.DecisionTreeClassifier()
clfIncome = clfIncome.fit(X, Y)

val = int(input("Enter val: "))
if val < 0: val = 0
if val > 100000: val = 100000

if val in range(0, 10000): val = 10
elif val in range(10000, 200000): val = 9
elif val in range(0, 10000): val = 8
elif val in range(0, 10000): val = 7
elif val in range(0, 10000): val = 6
elif val in range(0, 10000): val = 5
elif val in range(0, 10000): val = 4
elif val in range(0, 10000): val = 3
elif val in range(0, 10000): val = 2
elif val in range(0, 10000): val = 1 


pred = clfIncome.predict([[val]])
scoreSum += pred[0]

print(scoreSum / 3)

print("Hello rest of HackDFW, behold, the AUXILIAM project, hail us")
df = pd.read_csv("bigDataFeatures.csv")
df.head()

# X = 
# Y = 

# classifier = tree.DecisionTreeClassifier()
# classifier.fit(X, Y)


# CSV to python data table
# Take each value from the python data table
# Predict using on the Decision Treeclear
# Add each predicted score to the p
# ython data table
# Add python data table to CSV file