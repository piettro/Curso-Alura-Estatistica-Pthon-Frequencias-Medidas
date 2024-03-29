import pandas as pd
import numpy as np
import seaborn as snb
import scipy as sc

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

unique_anos_estudo = dataset['Anos de Estudo'].unique()

sorted_list_anos_estudo = sorted(dataset['Anos de Estudo'].unique())
sorted_list_sex = sorted(dataset['Sexo'].unique())
sorted_list_cor = sorted(dataset['Cor'].unique())
sorted_list_uf = sorted(dataset['UF'].unique())

min_age = dataset.Idade.min()

print(f"De {dataset['Idade'].min()} até {dataset['Idade'].max()} anos")
print(f"De {dataset['Altura'].min()} até {dataset['Altura'].max()} metros")