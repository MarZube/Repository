import pandas as pd
from datetime import datetime

liste = []
data = pd.DataFrame()

df = pd.read_csv (r'file directory on your pc\name of the file.csv')
for transaction in df["timestamp"]:
    date = datetime.utcfromtimestamp(transaction).strftime('%Y-%m-%d')

    liste.append(date)

for i in liste:
   data_new = pd.DataFrame(
       {'date': [i]}
   )

   data = pd.concat([data, data_new])


result = pd.concat([df, data.reset_index()], axis=1)
print(result)

result.to_csv("file directory where you want to save the file/new document name.csv")