import pandas as pd
import numpy as np
import seaborn as sns
import scipy as sc
import matplotlib.pyplot as plt

dataset = pd.read_csv('Data/dataset.csv')
print(dataset.head())

##Medidas separatrizes
##Quartis, decis e percentis

quartis = dataset['Renda'].quantile([0.25,0.5,0.75])

decis = dataset['Renda'].quantile([i/10 for i in range(1,10)])

percentis = dataset['Renda'].quantile([i/100 for i in range(1,100)])

ax = sns.distplot(dataset['Idade'],
                  hist_kws = {'cumulative': True},
                  kde_kws = {'cumulative': True}
)
ax.figure.set_size_inches(14, 6)
ax.set_title('Distribuição de Frequências Acumulada', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
plt.show()

##Box plot
ax = sns.boxplot( x = 'Altura', y='Sexo', data = dataset, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
plt.show()

ax = sns.boxplot( x = 'Renda', y='Sexo', data = dataset.query('Renda < 25000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
plt.show()
