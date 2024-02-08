import pandas as pd
import numpy as np
import seaborn as sns
import scipy as sc
import matplotlib.pyplot as plt

##Observations
##1.Foram eliminados os registros onde a Renda era invalida (999 999 999 999)
##2.Foram eliminados os registros onde a Renda era missing
##3.Foram considerados somente os registros das Pessoas de Referencia de cada domicilio (Responsavel pelo domicilio)

##Colunas
##Renda: calculará o rendimento mensal do trabalho principal para pessoas de 10 ou mais anos de idade;
##Idade: da moradora ou morador entrevistado contado em anos;
##Altura: foi elaborada para o curso, e a entenderemos melhor adiante;
##UF: Unidades da Federação com os códigos dos estados brasileiros como um dicionário;
##Sexo: feminino ou masculino com identificações numéricas também;
##Anos: de Estudo possuem uma codificação de acordo com a quantidade de tempo estabelecida na tabela;
##Cor: identifica a etnia da pessoa entrevistada com códigos.

dataset = pd.read_csv('Data/dataset.csv')
print(dataset.head())

sexo = {
    0:'Masculino',
    1:'Feminino'
}

cor = {
    0: 'Indigena',
    2: 'Branca',
    4: 'Preta',
    6: 'Amarela',
    8: 'Parda',
    9: 'Sem declaracao'
}

##Distribuicao de Frequencias - Variaveis Qualitativas
frequencia = dataset['Sexo'].value_counts()
percentual = dataset['Sexo'].value_counts(normalize=True) * 100

dist_freq_qualitativas = pd.DataFrame({
    'Frequencia': frequencia,
    'Porcentam (%)' : percentual
})
dist_freq_qualitativas.rename(index=sexo, inplace=True)
print(dist_freq_qualitativas.head())

crosstab_sexo_cor = pd.crosstab(dataset['Sexo'],dataset['Cor'],aggfunc='mean',values=dataset['Renda'])
crosstab_sexo_cor.rename(index=sexo, columns=cor, inplace=True)
print(crosstab_sexo_cor.head())

##Distribuicao de Frequencias - Variaveis Quantitativas
##Clase A - Acima de 15.760
##Clase B - Entre 7.880 e 15.760
##Clase C - Entre 3.152 e 7.880
##Clase D - Entre 1.576 e 3.152
##Clase E - Ate 1.576

classes = [0, 1576, 3152, 7880,15760,200000]
labels = ['E','D','C','B','A']

dataset['Classes'] = pd.cut(
    x = dataset['Renda'],
    bins = classes,
    labels= labels,
    include_lowest= True
)

frequencia_classes = dataset['Classes'].value_counts()
percentual_classes = dataset['Classes'].value_counts(normalize=True) * 100

dist_freq_quantitativas = pd.DataFrame({
    'Frequencia': frequencia_classes,
    'Porcentam (%)' : percentual_classes
})

dist_freq_quantitativas.sort_index(ascending=False, inplace=True)

##Regra de Sturges
n = dataset.shape[0]
k = 1 + (10 / 3) * np.log10(n)
k = int(k.round(0))

dataset['Classes Sturges'] = pd.cut(
    x = dataset['Renda'],
    bins = k,
    include_lowest= True
)

frequencia_classes = dataset['Classes Sturges'].value_counts(sort = False)
percentual_classes = dataset['Classes Sturges'].value_counts(normalize=True, sort = False) * 100

dist_freq_quantitativas_sturges = pd.DataFrame({
    'Frequencia': frequencia_classes,
    'Porcentam (%)' : percentual_classes
})

dist_freq_quantitativas_sturges.sort_index(ascending=False, inplace=True)

ax = sns.distplot(dataset['Altura'], kde=False)
ax.figure.set_size_inches(12,6)
ax.set_title('Distribuicao de Frequencia - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)

plt.show()