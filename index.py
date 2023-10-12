import pandas as pd

import csv
with open ("advertising.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("cabeçalho: " + str(linha))
        else:
            print("valor: " + str(linha)) 
            




        


