# função criar dataset + criar os valores para as classes + criar weights 
# função para interagir com o utilizador (numero de iterações + erro + valor da probabilidade de escolher a classes)
# função do algoritmo 
    # função calculo dos pesos 
    # função calculo do erro 
    # função calculo da previsão 
# função de criação do gráfico 

# TODO
# confirmar que a função de accurancy está correcta
# erro entre iterações 
# gráfico (falta tornar dinâmico a forma como vai buscar os dados)
# input nao funciona no visual code studio

# Importação das Libraries necessárias
from random import choices, choice
import random 
import numpy as np 
import matplotlib.pyplot as plt

# Criação da população 
def createDataset(nrows, nvariables): 
    return [[n/10 for n in choices(range(1,nrows),k=nvariables)] for _ in range(nrows)]

# Criação dos valores das classes 
def createClasses(nrows): 
    return [random.choice([0,1]) for x in range(nrows)]

# Criação dos valores dos pesos
def createWeights(nvariables): 
    return [n/10 for n in choices(range(1,5),k=nvariables)]

## Criação da função de interação com o utilizador
# Selecionar o número de iterações pretendidos,
# a mínima alteração do erro e a nossa probabilidade
# para definir a classe que será usada nos cálculos seguintes
def userInteractions(): 
    print("Qual o número de iterações?")
    nr_interactions = int(input())
    
    print("Qual a mínima alteração do erro?")
    error_value = float(input())

    print("Qual a probabilidade para definir classes?")
    prob_classe = float(input())
    
    return [nr_interactions, error_value, prob_classe]
    
# Criação da função que compara o nosso valor de observação com 0 
# Retorna 1 se essse valor for maior que 0
# Retorna 0 se esse valor for menor que 0
def lossFunction(sum_per_observation): 
    if(sum_per_observation >= 0): 
        return 1 
    else: 
        return 0

## Criação do nosso logatitmo base
# A partir daqui realiza-se o cálculo de novos pesos
# Realizam-se tantas iterações quantas selecionadas acima
# Ao fim dessas iterações iremos ter os nossos pesos finais
def perceptron(population, classes, weights, nr_iterations, p_classe):
    
    # Gráfico inicial 
    createGraph(0)
    
    predictions = [None] * len(population)
    
    # Loop pelo número de iterações que queremos executar
    for index in range(nr_iterations): 

        i = (index % len(population))
        soma_por_individuo = 0

        # Cálculo dos pesos x valor das variávis
        for index_weight in range(2): 
            soma_por_individuo += population[i][index_weight]*weights[index_weight]
        
        # Escolher a classe através da função de perda
        classe = lossFunction(soma_por_individuo)

        # Acrescentar à nossa lista de previsões
        predictions[i] = classe

        # Diferença entre a nova previsão e a classe original
        loss = classes[i] - classe

        # Se a classe prevista não for igual à original, é necessário ajustar os pesos
        if(classes[i] != classe):
            for ii in range(len(weights)): 
                weights[ii] = weights[ii] + (p_classe * loss * population[i][ii])

        # Visualização do Perceptron a cada iteração       
        createGraph(index + 1) 
        #print(weights)
    return predictions

# Criação da função que calcula a taxa de precisão do nosso algoritmo
# Compara o nosso valor original com a previsão
def perceptronAccurancy(original, predictions): 
    acc = str(1-sum([o - p for o, p in zip(original,predictions)])/len(original))
    return f"A taxa de precisão do nosso algoritmo Perceptron é: {acc}"

# Criação da função que reproduz o nosso gráfico
def createGraph(iteration):

    print("")
    print("****************************************************")
    print("****************************************************")
    print("                    ITERAÇÃO "+str(iteration))
    print("****************************************************")
    print("****************************************************")
    print("")

    data = np.array(population)
    X, Y = data.T

    # TODO
    # Isto está martelado é preciso alterar para ficar dinâmico
    X0=np.append(X[:1], X[3:4])
    Y0=np.append(Y[:1], Y[3:4])
    X1=np.append(X[1:2], X[2:3])
    Y1=np.append(Y[1:2], Y[2:3])
    
    # Acrescentar os pontos da população ao gráfico
    plt.scatter(X0, Y0, color='red', marker='o', label='Classe 0')
    plt.scatter(X1, Y1, color='blue', marker='x', label='Classe 1')
    
    # Acrescentar labels e legenda ao gráfico
    plt.xlabel('First Variable')
    plt.ylabel('Second Variable')
    plt.legend(loc='upper left')
    
    # Calcular o eixo dos x
    xx=np.linspace(-0.5,0.5,num=5)
    #print(xx)

    # Calcular o eixo dos y com a função da recta baseada nos pesos ajustados
    yy = -(weights[0] * xx) / weights[1]
    #print(yy)

    # Desenhar a recta no gráfico
    plt.plot(xx, yy, 'k-')
    
    #plt.savefig('images/02_06.png', dpi=300)
    # Mostrar o gráfico
    plt.show()

# Criação da função geral que chama todas as nossas funções criadas
def main(): 
    #user inputs
    inputs = userInteractions() 
    nr_iterations = inputs[0]
    error_value = inputs[1]
    prob_classe = inputs[2]

    #dataset creation
    #population = createDataset(10,2)
    #classes = createClasses(10)
    #weights = createWeights(2)

    population = [[0.3,0.7],[-0.6,0.3],[-0.1,-0.8],[0.1,-0.45]]
    classes = [1,0,0,1]
    weights = [0.8,-0.5]

    #print(population)
    #print(classes)
    #print(weights)
    
    #perceptron
    predictions = perceptron(population,classes,weights,nr_iterations,prob_classe)
    print(predictions)

    #print(predictions)
    acc = perceptronAccurancy(classes, predictions)
    print(acc)