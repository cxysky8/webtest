import csv
import pandas as pd

with open("data.csv","w") as csvfile:
    fidldnames=["id","name","age"]
    writer=csv.DictWriter(csvfile,fieldnames=fidldnames)
    writer.writeheader()
    writer.writerows([{"id":"1001","name":"jack","age":20},{"id":"1002","name":"bob","age":22}])

'''with open("data.csv","r") as readFile:
    read=csv.reader(readFile)
    for row in read:
        print(row)'''
df=pd.read_csv("data.csv")
print(df)