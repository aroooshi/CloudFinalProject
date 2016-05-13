import pandas as pd
import re
import sys
import pickle
from sklearn.externals import joblib
clf2 = joblib.load('tree.pkl') 
df110 = pd.read_pickle("df1.pkl")
wordcount2 = joblib.load('wordcount2.pkl') 
df10 = df110.transpose()
#line = "I am win lottery call now prize 1231232134235"
#line = "I am happy"
def spamclass(line,clf2,df10,wordcount2):
    new_words = []
    if sum(1 for c in line if c == "/") >= 1:
        temp = sum(1 for c in line if c == "/")
        new_words.append(["/",temp])
    if sum(1 for c in line if c == "+") >= 1: 
        temp = sum(1 for c in line if c == "+")
        new_words.append(["+",temp])
    k = line.lower()
    k = k.replace("'","")
    k = re.sub(r'[^\w]', ' ', k)
    k = k.split()
    if len(k) <= 10:
        new_words.append(["len<=10",1])
    for word in k:
        if sum(1 for c in word if c.isdigit()) >= 10:
            new_words.append(["digit>=10",1])
        elif sum(1 for c in word if c.isdigit()) >= 5:
            new_words.append(["digit>=5",1])
        elif sum(1 for c in word if c.isdigit()) >= 3:
            new_words.append(["digit>=3",1])
        if word in wordcount2:
            new_words.append([word,1])
    sub_dict = {}
    for word in new_words:
        if word[0] not in sub_dict:
            sub_dict[word[0]] = word[1]
        else:
            sub_dict[word[0]] += word[1]
    df10 = df10.append(sub_dict,ignore_index = True)
    df11 = df10.replace('NaN',0)
    return clf2.predict([df11.iloc[1]])[0]

line = sys.argv[1]
#print line
print spamclass(line,clf2,df10,wordcount2)

