import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
DataSet = pd.read_csv("SalaryData.csv")
x = DataSet["YearsExperience"]
y = DataSet["Salary"]
x = x.values.reshape(30,1)
y = y.values.reshape(30,1)
model = LinearRegression()
model = model.fit(x,y)
model.coef_
print("""*********************************************\n""")
pred = int(input("Enter Year of Experience : "))
Out = model.predict([[pred]])
print("""*********************************************\n""")
print("Predicted Salary : ",int(Out),"RS\n")



