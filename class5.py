import pandas as pd
import numpy as np
import seaborn as sns
import scipy as sc
import matplotlib.pyplot as plt

dataset = pd.read_csv('Data/dataset.csv')
print(dataset.head())

#Medidas de dispersao
##Desvio medio absoluto
media_renda = dataset['Renda'].mean()
dataset['DesvioRenda'] = dataset['Renda'] - media_renda

ax = dataset['Renda'].plot(style = 'o')
ax.figure.set_size_inches(14, 6)
ax.hlines(y = media_renda, xmin = 0, xmax = dataset.shape[0] - 1, colors = 'red')
for i in range(dataset.shape[0]):
    ax.vlines(x = i, ymin = media_renda, ymax = dataset['Renda'][i], linestyle='dashed')
plt.show()

desvio_medio_absoluto = dataset['Renda'].mad()

##Variancia
dataset['Renda (Desvio)^2'] = dataset['DesvioRenda'].pow(2)
dataset['Renda (Desvio)^2'].sum() / (len(dataset) - 1)
variancia = dataset['Renda'].var()

##Desvio Padrao
desvio_padrao = np.sqrt(variancia)
desvio_padrao = dataset['Renda'].std()