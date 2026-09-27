# Create a CSV dataset
import csv
import pandas as pd
empolye= [
  ["ID","Name","Gender","Salary","City","Company"],
  [1,"Ravi","Male",35000,"London","tcs"],
  [2,"Radha","Female",45000,"Scotland","wp"],
  [3,"viji","Female",25000,"London","cts"]
 ]
with open("record.csv",mode="w",newline="") as file:
    writer= csv.writer(file)
    writer.writerows(empolye)
print("csv file created")
print(empolye)
df =pd.read_csv("record.csv")
print("record.csv :\n ",df)
import seaborn as sns 
import matplotlib as plt
x =[1,2,3,4,5]
y =[12,43,52,56]
plt.plot(x,y)

