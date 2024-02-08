import pandas as pd
import numpy as np
import seaborn as sns
import scipy as sc
import matplotlib.pyplot as plt

dataset = pd.DataFrame(data = {'Aluno 1': [8, 10, 4, 8, 6, 10, 8],
                          'Aluno 2': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Aluno 3': [2.5, 8, 7, 8, 6, 3.5, 7]
                          'Aluno 4': [7.5, 8, 7, 7, 4, 8.5, 6]
                          'Aluno 5': [4, 7, 4, 8.5, 6, 9.5, 7]
                          'Aluno 6': [7.5, 8, 7.5, 8, 9, 8.5, 5]
                          'Aluno 7': [5.5, 6, 5, 6, 8, 6.5, 7]
                          'Aluno 8': [7.5, 8, 6, 8.5, 10, 8.5, 3]},
                 index = ['Matemática',
                          'Português',
                          'Inglês',
                          'Geografia',
                          'História',
                          'Física',
                          'Química'])
dataset.rename_axis('Matérias', axis = 'columns', inplace = True)

print(dataset.head())

##Medidas de tendencia central

#Media
for i in dataset.index:
    media = dataset.loc[i].mean()
    print(f"A nota media de {i} foi {round(media,1)}")

for i in dataset.index:
    media = dataset.loc[i].sum() / dataset.loc[i].shape[0]
    print(f"A nota media de {i} foi {round(media,1)}")

#Mediana
for i in dataset.index:
    mediana = dataset.loc[i].median()
    print(f"A nota media de {i} foi {round(mediana,1)}")

for i in dataset.index:
    mediana = dataset.loc[i].quantile()
    print(f"A nota media de {i} foi {round(mediana,1)}")

##Moda
for i in dataset.index:
    media = dataset.loc[i].mode()
    print(f"A moda de {i} foi {round(media,1)}")

