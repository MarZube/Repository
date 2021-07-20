import pandas as pd
from datetime import datetime

liste = []
data = pd.DataFrame()

df = pd.read_csv (r'C:\Users\mario\Documents\UZH\UZH 6. Semester\Bachelorarbeit\Chainlink Data.csv')
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

result.to_csv("C:/Users/mario/Documents/UZH/UZH 6. Semester/Bachelorarbeit/Chainlink_My analysis.csv")