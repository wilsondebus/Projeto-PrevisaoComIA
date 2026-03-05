## 🧠 Previsão de Score de Crédito com Machine Learning

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de prever o score de crédito de clientes com base em características financeiras e comportamentais.

O modelo classifica os clientes em três categorias de risco:

Boa

OK

Ruim

A solução foi desenvolvida em Python, utilizando bibliotecas amplamente usadas em ciência de dados, como Pandas e Scikit-learn.

## 🚀 Tecnologias Utilizadas

Python

Pandas

Scikit-learn

Jupyter Notebook

## 📊 Etapas do Projeto

O desenvolvimento do modelo seguiu as seguintes etapas:

1️⃣ Importação e análise da base de dados

A base de clientes é carregada e analisada para identificar as variáveis relevantes para a previsão do score de crédito.

2️⃣ Tratamento e preparação dos dados

Algumas colunas possuem valores categóricos (texto).
Esses valores são transformados em números utilizando Label Encoding, permitindo que os algoritmos de Machine Learning consigam processá-los.

Exemplos de variáveis tratadas:

Profissão

Mix de crédito

Comportamento de pagamento

3️⃣ Separação de dados de treino e teste

Os dados são divididos em:

70% para treinamento

30% para teste

Isso permite avaliar o desempenho do modelo em dados que ele nunca viu.

4️⃣ Treinamento de modelos de Machine Learning

Foram testados dois algoritmos:

Random Forest (Árvore de decisão em conjunto)

K-Nearest Neighbors (KNN)

Após os testes, o modelo Random Forest apresentou melhor desempenho.

5️⃣ Previsão para novos clientes

Após o treinamento, o modelo é utilizado para prever o score de crédito de novos clientes, importados de um arquivo separado.

Antes da previsão, os dados passam pelo mesmo processo de transformação utilizado no treinamento do modelo.

## 📈 Resultado

O modelo treinado consegue analisar características financeiras e prever automaticamente o perfil de crédito de novos clientes, auxiliando em processos de análise de risco e tomada de decisão.

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

Prática de Machine Learning

Manipulação de dados com Pandas

Uso de modelos da biblioteca Scikit-learn

Construção de um pipeline completo de análise e previsão de dados

## 👨‍💻 Autor

Wilson Dias Debus
Estudante de Ciência da Computação
Universidade Franciscana – Santa Maria/RS
