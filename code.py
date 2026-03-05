# Analisando 1 cliente, se é BOM, OK ou RUIM (nota de crédito para ele = Score de crédito)
# Criar uma IA 

# Passo a passo do projeto 
# Passo 0: entender o desafio da empresa 
# Passo 1: Importar a base de dados 
# pip install scikit-learn

import pandas as pd     #apelido 'pd' para usar futuramente 

tabela = pd.read_csv("clientes.csv")    #lendo a base de dados
display(tabela)     #mostra a tabela 
display(tabela.info())

# Passo 2: Tratar e preparar a base de dados para a IA 

# IA só trabalha com numeros 
from sklearn.preprocessing import LabelEncoder #estou importando apenas uma bilbioteca do pacote sklearn
codificador_profissao = LabelEncoder()
tabela["profissao"] = codificador_profissao.fit_transform(tabela["profissao"])  #aplicando o codificador na coluna especifica 

codificador_mix = LabelEncoder()
tabela["mix_credito"] = codificador_mix.fit_transform(tabela["mix_credito"])

codificador_comportamento = LabelEncoder()
tabela["comportamento_pagamento"] = codificador_comportamento.fit_transform(tabela["comportamento_pagamento"])

display(tabela)
 
# Processo de criação de IA 
# x = quem ele vai usar // y = quem ele vai prever (NÃO PODE SER MAIS DE UM)
y = tabela["score_credito"]
x = tabela.drop(["score_credito", "id_cliente"], axis=1)   #pega todas as colunas MENOS score_credito e id_cliente(pois é desnecessario)  

# dividir a base de dados em base de treino e outro pedaço em base de treino (com gabarito e a previsão da IA)
# x_treino // y_treino
# x_teste // y_teste

from sklearn.model_selection import train_test_split 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)   #fazendo o treino e os testes da IA(sempre nessa ordem) e o percentual de teste e treino

# Passo 3: Modelo de previsão ou modelo de IA -> BOA, OK, RUIM

# Modelos: (existem infinitos modelos mas vou usar esses)
# Arvore de Decisão -> RandomForest
# KNN -> Nearest Neighbors 

y = tabela["score_credito"]
x = tabela.drop(["score_credito", "id_cliente"], axis=1)

from sklearn.model_selection import train_test_split 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# passo 1: Importar a IA (modelo)
from sklearn.ensemble import RandomForestClassifier 
from sklearn.neighbors import KNeighborsClassifier 

# passo 2: Criar a IA (modelo)
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

# passo 3: Treinar a IA (modelo)
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# Passo 4: Avaliar e escolher o melhor modelo 

# previsao 
previsao_arvore = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

# comparar a previsao com o y_teste
from sklearn.metrics import accuracy_score

print("Arvore de Decisão: ")
print(accuracy_score(y_teste, previsao_arvore))
print("KNN: ")
print(accuracy_score(y_teste, previsao_knn))

# Passo 5: Fazer novas previsões 

# melhor modelo = Arvore de decisão

# importar novos clientes 
novos_clientes = pd.read_csv("novos_clientes.csv")

# não usa o fit antes do transform, pois se não ia criar outros numeroa para cada str
novos_clientes["profissao"] = codificador_profissao.transform(novos_clientes["profissao"])  #aplicando o codificador na coluna especifica 

novos_clientes["mix_credito"] = codificador_mix.transform(novos_clientes["mix_credito"])

novos_clientes["comportamento_pagamento"] = codificador_comportamento.transform(novos_clientes["comportamento_pagamento"])

previsao = modelo_arvoredecisao.predict(novos_clientes)

display(novos_clientes)
display(previsao)
