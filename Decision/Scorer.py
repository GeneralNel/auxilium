import pandas as pd
from sklearn import tree


# Number of siblings
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

clfSiblings = tree.DecisionTreeClassifier()
clfSiblings = clfSiblings.fit(X, Y)



# Number of device
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
Y = [10, 10, 8, 8, 6, 6, 4, 4, 2, 2]

clfDevices = tree.DecisionTreeClassifier()
clfDevices = clfDevices.fit(X, Y)



# Income
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

clfIncome = tree.DecisionTreeClassifier()
clfIncome = clfIncome.fit(X, Y)



print("Hello rest of HackDFW, behold, the AUXILIAM project, hail us")
df = pd.read_csv("bigDataFeatures.csv")

for idx, each in enumerate(df.iloc):
    scoreSum = 0

    sib, lap, val = each[1], each[2], int(each[3])

    if sib < 0: sib = 0
    if sib > 9: sib = 9 
    pred = clfSiblings.predict([[val]])
    scoreSum += pred[0]


    if lap < 0: lap = 0
    if lap > 9: lap = 9 
    pred = clfDevices.predict([[val]])
    scoreSum += pred[0]

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


    df.at[idx, "Score"] = scoreSum / 3

df.sort_values('Score')

df.to_csv('Result.csv')
