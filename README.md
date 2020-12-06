# ISAG-Perceptron
Assignment - Programming

# About
Este repositório foi criado no âmbito da unidade curricular de Programming do curso da Pós Gradução de Data Science e Business Intelligence do ISAG. 

O objectivo deste projecto é a implementação de um algoritmo baseado em redes neuronais chamado de Perceptron. O código desenvolvido encontra-se na liguagem de programação Python.

# Intro to Perceptron 
O modelo Perceptron surgiu entre 1950 e 1960 e apesar de hoje em dia não ser comum o seu uso no mundo real pois é considerado um modelo básico, o Perceptron permite uma compreensão simples sobre a forma como uma rede neuronal funciona. 

O Perceptron é um classificador binário e linear, ou seja este modelo é usado para lidar com problemas de classificação cujo o dataset permita uma separação linear dos dados. 

#### AQUI

Fonte da Imagem: http://www.statistics4u.com/fundstat_eng/cc_classif_calib.html

Apesar de ser um algoritmo simples, o Perceptron não é um algoritmo "fraco" pois quando combinado com outros algoritmos ou mesmo quando usado num contexto de separação linear dos dados, este é pode apresentar altos graus de precisão. 

# How it works?

O Perceptron é um modelo matemático que recebe vários inputs (x1, x2, x3 ...) e tem como resultado um único output binário (0 ou 1). 

A regra para calcular o resultado final pressupõe o conhecimento de dois parâmetros do neurónio: 
* Pesos associados aos vários inputs (w1, w2, w3 ...)
* Valor constante de threshold (bias)

#### AQUI
O cálculo consiste numa soma ponderada de um produto escalar entre os inputs (x1, x2, x3 ...) e os respectivos pesos (w1, w2, w3 ...). Por sua vez, o resultado deste cálculo (x1*w1 + x2*w2 + x3*w3 ...) é usado para classificar cada observação como 0 ou 1 em comparação com um valor limiar (threshold/bias). 

Se x1*w1 + x2*w2 + x3*w3 ... >= bias então classificamos como classe = 1, se esta condição não se verificar ou seja x1*w1 + x2*w2 + x3*w3 ... < bias então classificamos como classe = 0. 

Após o algoritmo prever a sua classificação, os pesos iniciais devem ser ajustados consoante a classe seja igual ou não à original. 

# Our Implementation


# How to install? 
> $ git clone https://github.com/anamarg83/ISAG-Perceptron.git
> $ cd ISAG-Perceptron

# Main Functions 
Para a implementação deste algoritmo foram criadas as seguintes funções auxiliares:
| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |


