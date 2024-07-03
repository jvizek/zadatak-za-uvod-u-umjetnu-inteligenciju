import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LogisticRegression
#importano sve kako bi ovo možda profunkcioniralo. 
#podatci = np.read_csv ("20test_BoW.csv")
#podatci nisu prepoznati vjerojatno zato što ne znam napravit put ili sam slučajno napravio put ali put nije pravilan
#ok ajmo rec da imamo neke podatke... i zanemarit ćemo analizu sentimenta, pa čak i bag of words
x = np.array[1,2,3,4,5,6,7,8,9,10,] #broj popušenih cigara
y = np.array[0,0,0,0,0,1,1,1,1,1)] #0 predstavlja ne rak, a 1 predstavlja rak
model = LogisticRegression
model.fit(x,y)
x = 3
prediction = model.predict(np.array y)
if prediction = 0 print ("bravo majstore")
else prediction = 1 print ("ajoj")
#ne valja 
#ako proradi ovaj podatci onda treba prvo napravit training, a onda testing i treba napisati formulu za sigmodovu funkciju

