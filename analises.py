import pandas as pd

# Lendo a planilha Excel
df = pd.read_csv('dados_alunos_escola.csv')

# Exibindo os dados na tela
#print(df)

#print(df) # leiturada planilha inteira

# 1. Visualizar as primeiras linhas
#print(df.head())

# exibe  as primeiras 5 linhas so DataFrame

# 2. Verificar o resumo estatístico (médias mínimos, máximos)
#print(df.describe())

# 3. Ver os tipos de dados e se há valores nulos
print(df.info())
 
 
