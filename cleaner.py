import pandas as pd

path = "/home/mauricemohamed/PycharmProjects/Scrapper mk1/boiler.csv"

df = pd.read_csv(path)
#deleate collumn 5
prob = df.drop(df.columns[4], axis=1, inplace=True)
print(prob)
#save new csv
df.to_csv(path , index=False)



