import pandas as pd

person = {"Name":["Raj","Aakash","Ayush","Raju"],
          "Age":[20,None,21,22],
          "Salary":[1000,2000,3000,None],
        }
print(person)
# filling the missing values 
df = pd.DataFrame(person)
# df.fillna()
print(df)

df2 = pd.DataFrame({"Gender":["Male","Female"]})
df2["Gender_encoded"] = df2["Gender"].map({"Male":0,"Female":1})
print(df2)





