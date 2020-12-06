# ISAG-Perceptron
Assignment - Programming

# About
Este repositório foi criado no âmbito da unidade curricular de Programming do curso da Pós Gradução de Data Science e Business Intelligence do ISAG. 

O objectivo deste projecto é a implementação de um algoritmo baseado em redes neuronais chamado de Perceptron. O código desenvolvido encontra-se na liguagem de programação Python.

# Intro to Perceptron 
O modelo Perceptron surgiu entre 1950 e 1960 e apesar de hoje em dia não ser comum o seu uso no mundo real pois é considerado um modelo básico, o Perceptron permite uma compreensão simples sobre a forma como uma rede neuronal funciona. 

O Perceptron é um classificador binário e linear, ou seja este modelo é usado para lidar com problemas de classificação cujo o dataset permita uma separação linear dos dados. 

![alt text](http://www.statistics4u.com/fundstat_eng/img/hl_classif_separation.png)

```Fonte da Imagem: http://www.statistics4u.com/fundstat_eng/cc_classif_calib.html```

Apesar de ser um algoritmo simples, o Perceptron não é um algoritmo "fraco" pois quando combinado com outros algoritmos ou mesmo quando usado num contexto de separação linear dos dados, este é pode apresentar altos graus de precisão. 

# How it works?

O Perceptron é um modelo matemático que recebe vários inputs (x1, x2, x3 ...) e tem como resultado um único output binário (0 ou 1). 

A regra para calcular o resultado final pressupõe o conhecimento de dois parâmetros do neurónio: 
* Pesos associados aos vários inputs (w1, w2, w3 ...)
* Valor constante de threshold (bias)

![alt text](https://miro.medium.com/max/645/0*LJBO8UbtzK_SKMog)

```Fonte da imagem: https://towardsdatascience.com/what-is-a-perceptron-210a50190c3b```


O cálculo consiste numa soma ponderada de um produto escalar entre os inputs (x1, x2, x3 ...) e os respectivos pesos (w1, w2, w3 ...). Por sua vez, o resultado deste cálculo (x1*w1 + x2*w2 + x3*w3 ...) é usado para classificar cada observação como 0 ou 1 em comparação com um valor limiar (threshold/bias). 

Se ```x1*w1 + x2*w2 + x3*w3 ... >= bias``` então classificamos como ```classe = 1```, se esta condição não se verificar ou seja ```x1*w1 + x2*w2 + x3*w3 ... < bias``` então classificamos como ```classe = 0```. 

Após o algoritmo prever a sua classificação, os pesos iniciais devem ser ajustados consoante a classe seja igual ou não à original. 

# Our Implementation - The Assumptions 
* A nossa implementação do algoritmo Perceptron contém a criação de um dataset gerado aleatoriamente cujo o utilizador não consegue alterar, o mesmo acontece para os valores dos pesos e classes finais. 
* A learning rate do Perceptron foi pré definida com o valor de 0.05.
* O modelo a cada iteração percorre todos os elementos do dataset e ajusta os pesos sempre que cada indivíduo é mal classificado pelo modelo. 
* O cálculo do erro é calculado no fim de cada iteração através do produto entre a learning rate e a diferença entre as classes previstas e originais. 
* A única limitação da nossa implementação é que apenas consegue representar o gráfico dos dados e da função linear nos casos de datasets com apenas 2 variáveis/inputs. 

# How to install? 
> $ git clone https://github.com/anamarg83/ISAG-Perceptron.git

> $ cd ISAG-Perceptron

# Main Functions 
Para a implementação deste algoritmo foram criadas as seguintes funções auxiliares:
| Function | Arguments & Return Values | Description |
| --- | --- | --- |
| createDataset | Número de indivíduos da população e número de inputs/variáveis a considerar. Devolve uma lista de listas. | Função que gera aleatoriamente valores decimais entre 0 e o número de indivíduos. |
| createClasses | Número de indivíduos da população. Devolve uma lista. | Função que gera as classes da população. Valores aleatórios entre 0 e 1. |
|  createWeights | Número de variáveis/pesos. Devolve uma lista. | Função que gera aleatoriamente valores entre 0 e 1 numa lista. |
| userInteractions | NA | Função que permite ao utilizador introduzir os valores relativos ao número de iterações do algoritmo, mínima alteração do erro entre iterações e o valor do parâmetro threshold/bias. | 
| classificationFunction | Valor float. Devolve a classe 0 ou 1. | Função que permite classificar uma observação com base no valor previamente calculado do x1*w1 + x2*w2 + x3*w3 + ... + bias  | 
| perceptron | Recebe vários argumentos para o algoritmo como o dataset, as classes originais, os pesos, o  bias, o número de iterações, learning rate e erro mínimo.a Devolve uma lista com as classificações previstas. | Função que contém a lógica principal do Perceptron, itera sobre o número de iterações pré definidas sobre toda a população, calcula os valores previstos e ajusta os pesos. | 
| errorFunction | Duas listas. Devolve o valor do erro. | Função que calcula o erro do algoritmo com base na comparação entre as classes originais e previstas | 
| perceptronAccurancy | Duas listas. Devolve um print com o valor da precisão. | Função que calcula a precisão do algoritmo com base na comparação entre as classes originais e previstas. | 
| createGraph | Número de iterações. Não devolve nada. | Função que imprime um gráfico com os data points do dataset/população e a equação da recta com base nos pesos ajustados pelo algoritmo. | 
| errorsGraph | Lista com valores dos erros e número de iterações. Não devolve nada. | Função que imprime o gráfico com a evolução do erro do algoritmo ao longo das iterações. | 
| geral | NA | Função main que integra todas as outras funções criadas. | 




