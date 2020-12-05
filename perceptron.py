# Importação das Libraries necessárias
from random import choices, choice
import random 
import numpy as np 
import matplotlib.pyplot as plt

# Criação da população 
def createDataset(nrows, nvariables): 
    return [[n/10 for n in choices(range(1,nrows),k=nvariables)] for _ in range(nrows)]

# Criação dos valores das classificação
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
    print("QUAL O NÚMERO DE ITERAÇÕES?")
    nr_interactions = int(input())
    
    print("QUAL A MÍNIMA ALTERAÇÃO DO ERRO?")
    error_value = float(input())

    print("QUAL A PROBABILIDADE PARA DEFINIR CLASSES?")
    prob_classe = float(input())
    
    return [nr_interactions, error_value, prob_classe]

# Criação da função que compara o nosso valor de observação com 0 
# Retorna 1 se essse valor for maior que 0
# Retorna 0 se esse valor for menor que 0
def classificationFunction(sum_per_observation): 
    if(sum_per_observation >= 0): 
        return 1 
    else: 
        return 0

## Criação do nosso logatitmo base
# A partir daqui realiza-se o cálculo de novos pesos
# Realizam-se tantas iterações quantas selecionadas acima
# Ao fim dessas iterações iremos ter os nossos pesos finais
def perceptron(population, classes, weights, iterations, p_classe, learning_rate, minimal_error):
    
    # Mostrar estado inicial
    createGraph(0)
    
    predictions = [None] * len(population)

    # Percorrer o número de iterações definidas pelo utilizador
    for index in range(iterations):

        # Validar se o erro é inferior ao erro mínimo definido pelo utilizador
        if errors[-1] > minimal_error:

          for i in range(len(population)):
            value_per_observation = 0

            # Cálculo dos pesos x valor das variávis
            for index_weight in range(len(weights)): 
              value_per_observation += population[i][index_weight]*weights[index_weight] + p_classe
          
            # Guardar o valor da nossa previsão
            predictions[i] = classificationFunction(value_per_observation)

            # Diferença entre a previsão e as classes originais
            diff_between_prediction_original = classes[i] - predictions[i]

            # Ajuste de pesos se a classe prevista não for igual à original 
            # Chegamos à conclusão que ajustar os pesos apenas quando a nossa previsão é diferente da original, 
            # o algoritmo é mais eficaz do que quando ajustamos sempre os pesos
            if classes[i] != predictions[i] :  
              for ii in range(len(weights)): 
                weights[ii] = weights[ii] + (learning_rate * diff_between_prediction_original * population[i][ii])
          
          # Cálculo dos erros
          total_error = float(learning_rate) * float(errorFunction(classes, predictions))
          errors.append(total_error) 
        else: 
          # Termina o algoritmo se atingiu o erro mínimo 
          return predictions

    return predictions

# Criação da função que calcula o erro do nosso algoritmo
def errorFunction(original, predictions): 
    acc = [p - o for o, p in zip(original,predictions)].count(0)/len(original)
    return 1 - acc

# Criação da função que calcula a taxa de precisão do nosso algoritmo
# Compara o nosso valor original com a previsão
def perceptronAccurancy(original, predictions): 
    print(original)
    print(predictions)
    acc = [o - p for o, p in zip(original,predictions)].count(0)/len(original)
    return f"____________________________________________________\n\nA taxa de precisão do algoritmo Perceptron é: {acc}\n____________________________________________________\n"

# Criação da função que reproduz o nosso gráfico
def createGraph(iteration):

    data = np.array(population)
    X, Y = data.T

    X0 = [X[index] for index, c in enumerate(classes) if c == 0] # valores da primeira variavel da população com a classe = 0
    Y0 = [Y[index] for index, c in enumerate(classes) if c == 0] # valores da segunda variavel da população com a classe = 0
    X1 = [X[index] for index, c in enumerate(classes) if c == 1] # valores da primeira variavel da população com a classe = 1
    Y1 = [Y[index] for index, c in enumerate(classes) if c == 1] # valores da segunda variavel da população com a classe = 1
    
    # Criação do gráfico com os pontos
    plt.scatter(X0, Y0, color='red', marker='o', label='Classe 0')
    plt.scatter(X1, Y1, color='blue', marker='x', label='Classe 1')
    
    plt.title('Iteração nº ' + str(iteration))
    plt.xlabel('Primeira Variável')
    plt.ylabel('Segunda Variável')
    plt.legend(loc='upper left')
    
    # Calcular os valores do eixo X
    xx=np.linspace(-0.5,0.5,num=5)

    # Calcular os valores do eixo Y com os pesos
    yy = -(weights[0] * xx) / weights[1]

    plt.plot(xx, yy, 'k-')
    plt.grid()
    plt.show()


# Criação da função que reproduz o nosso gráfico de erros ao longo das várias iterações
def errorsGraph(errors, iterations): 
  print(errors)   
  plt.plot(errors)
  plt.title('Erro ao longo das iterações')
  plt.xlabel('Epoch')
  plt.ylabel('Total Loss')
  plt.grid()

# Criação da função geral que chama todas as nossas funções criadas
def geral(): 
    # Inputs do utilizador
    inputs = userInteractions() 
    iterations = inputs[0]
    minimal_error = inputs[1]
    prob_classe = inputs[2]

    # Dataset creation
    population = createDataset(10,2)
    classes = createClasses(10)
    weights = createWeights(2)
    
    learning_rate = 0.05

    # Algoritmo Perceptron
    predictions = perceptron(population, classes, weights, iterations, prob_classe, learning_rate, minimal_error)
    
    createGraph(iterations) 

    # Valor de precisão do nosso algoritmo
    #acc = perceptronAccurancy(classes, predictions)
    #print(acc)

    # Gráfico dos erros
    errorsGraph(errors, iterations)