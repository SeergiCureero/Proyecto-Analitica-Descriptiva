import csv
import math

CPbarcelona = '08'
CPgirona = '17'
CPlleida = '25'
CPtarragona = '43'

municipis08 = []
municipis17 = []
municipis25 = []
municipis43 = []

def FiltraPerProvincies():
    # Divideix els municipis per provincies
    for fila in lector:
        if fila[1][:2] == CPbarcelona:
            municipis08.append(fila)
        elif fila[1][:2] == CPgirona:
            municipis17.append(fila)
        elif fila[1][:2] == CPlleida:
            municipis25.append(fila)
        elif fila[1][:2] == CPtarragona:
            municipis43.append(fila)

def CalculaPreuMitjaPerProvincia():
    FiltraPerProvincies()
    cont08 = 0
    cont17 = 0
    cont25 = 0
    cont43 = 0
    mitja08 = 0.0
    mitja17 = 0.0
    mitja25 = 0.0
    mitja43 = 0.0
    for fila in municipis08:
        if fila[6] != '':
            mitja08 += float(fila[6])
            cont08 += 1  
    for fila in municipis17:
        if fila[6] != '':
            mitja17 += float(fila[6])
            cont17 += 1
    for fila in municipis25:
        if fila[6] != '':
            mitja25 += float(fila[6])
            cont25 += 1
    for fila in municipis43:
        if fila[6] != '':
            mitja43 += float(fila[6])
            cont43 += 1
    mitja08 = round((mitja08/cont08), 2)
    mitja17 = round((mitja17/cont17), 2)
    mitja25 = round((mitja25/cont25), 2)
    mitja43 = round((mitja43/cont43), 2)
    return(mitja08,mitja17,mitja25,mitja43)
    
    
def PreuMesAltPerProvincia():
    FiltraPerProvincies()
    preuMesAlt08 = 0.0
    municipiMesAlt08 = ''
    preuMesAlt17 = 0.0
    municipiMesAlt17 = ''
    preuMesAlt25 = 0.0
    municipiMesAlt25 = ''
    preuMesAlt43 = 0.0
    municipiMesAlt43 = ''
    for fila in municipis08:
        if fila[6] != '':
            if float(fila[6]) >= preuMesAlt08:
                preuMesAlt08 = float(fila[6])
                municipiMesAlt08 = fila[2]
    for fila in municipis17:
        if fila[6] != '':
            if float(fila[6]) >= preuMesAlt17:
                preuMesAlt17 = float(fila[6])
                municipiMesAlt17 = fila[2]
    for fila in municipis25:
        if fila[6] != '':
            if float(fila[6]) >= preuMesAlt25:
                preuMesAlt25 = float(fila[6])
                municipiMesAlt25 = fila[2]
    for fila in municipis43:
        if fila[6] != '':
            if float(fila[6]) >= preuMesAlt43:
                preuMesAlt43 = float(fila[6])
                municipiMesAlt43 = fila[2]
    return(preuMesAlt08,preuMesAlt17,preuMesAlt25,preuMesAlt43,municipiMesAlt08,municipiMesAlt17,municipiMesAlt25,municipiMesAlt43)

def PreuMesBaixPerProvincia():
    FiltraPerProvincies()
    preuMesBaix08 = 100000000.0
    municipiMesBaix08 = ''
    preuMesBaix17 = 100000000.0
    municipiMesBaix17 = ''
    preuMesBaix25 = 100000000.0
    municipiMesBaix25 = ''
    preuMesBaix43 = 100000000.0
    municipiMesBaix43 = ''
    for fila in municipis08:
        if fila[6] != '':
            if float(fila[6]) <= preuMesBaix08:
                preuMesBaix08 = float(fila[6])
                municipiMesBaix08 = fila[2]
    for fila in municipis17:
        if fila[6] != '':
            if float(fila[6]) <= preuMesBaix17:
                preuMesBaix17 = float(fila[6])
                municipiMesBaix17 = fila[2]
    for fila in municipis25:
        if fila[6] != '':
            if float(fila[6]) <= preuMesBaix25:
                preuMesBaix25 = float(fila[6])
                municipiMesBaix25 = fila[2]
    for fila in municipis43:
        if fila[6] != '':
            if float(fila[6]) <= preuMesBaix43:
                preuMesBaix43 = float(fila[6])
                municipiMesBaix43 = fila[2]
    return(preuMesBaix08,preuMesBaix17,preuMesBaix25,preuMesBaix43,municipiMesBaix08,municipiMesBaix17,municipiMesBaix25,municipiMesBaix43)







# Obrir l'arxiu CSV
with open('dades/PreuLloguer20250117.csv', mode='r', encoding='utf-8') as file:
    lector = csv.reader(file)
    print(f'Provincia de Barcelona:\n    Mitja: {CalculaPreuMitjaPerProvincia()[0]}€/mes\n    Preu més alt: {PreuMesAltPerProvincia()[0]}€ ({PreuMesAltPerProvincia()[4]})\n    Preu més baix: {PreuMesBaixPerProvincia()[0]}€ ({PreuMesBaixPerProvincia()[4]})\nProvincia de Girona:\n    Mitja: {CalculaPreuMitjaPerProvincia()[1]}€/mes\n    Preu més alt: {PreuMesAltPerProvincia()[1]}€ ({PreuMesAltPerProvincia()[5]})\n    Preu més baix: {PreuMesBaixPerProvincia()[1]}€ ({PreuMesBaixPerProvincia()[5]})\nProvincia de Lleida:\n    Mitja: {CalculaPreuMitjaPerProvincia()[2]}€/mes\n    Preu més alt: {PreuMesAltPerProvincia()[2]}€ ({PreuMesAltPerProvincia()[6]})\n    Preu més baix: {PreuMesBaixPerProvincia()[2]}€ ({PreuMesBaixPerProvincia()[6]})\nProvincia de Tarragona:\n    Mitja: {CalculaPreuMitjaPerProvincia()[3]}€/mes\n    Preu més alt: {PreuMesAltPerProvincia()[3]}€ ({PreuMesAltPerProvincia()[7]})\n    Preu més baix: {PreuMesBaixPerProvincia()[3]}€ ({PreuMesBaixPerProvincia()[7]})')
    


import pandas as pd
df_datos = pd.read_csv("dades/PreuLloguer20250117.csv")