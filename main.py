import pandas as pd
tabela = pd.read_csv("advertising.csv", sep=",")
print(tabela["tv"].sum())