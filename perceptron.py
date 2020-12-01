# função criar dataset + criar os valores para as classes + criar weights 
# função para interagir com o utilizador (numero de iterações + erro + valor da probabilidade de escolher a classes)
# função do algoritmo 
    # função calculo dos pesos 
    # função calculo do erro 
    # função calculo da previsão 
# função de criação do gráfico 

# population = [[0.3,0.7,0.1],[-0.6,0.3,0.2],[-0.1,-0.8,0.3],[0.1,-0.45,0.4]]
# classes = [1,0,0,1]
# weights = [0.8,-0.5,-0.1]

# fazer comentários no código
# erro 
# gráfico
# input nao funciona no visual code studio

# Import Libraries
from random import choices, choice
import random 

# Criação da população 
def createDataset(nrows, nvariables): 
    return [[n/10 for n in choices(range(1,nrows),k=nvariables)] for _ in range(nrows)]

# Criação dos valores das classificação
def createClasses(nrows): 
    return [random.choice([0,1]) for x in range(nrows)]

# Criação dos valores dos pesos
def createWeights(nvariables): 
    return [n/10 for n in choices(range(1,5),k=nvariables)]

def userInteractions(): 
    print("Qual o número de iterações?")
    nr_interactions = int(input())
    
    print("Qual a mínima alteração do erro?")
    error_value = float(input())

    print("Qual a probabilidade para definir classes?")
    prob_classe = float(input())
    
    return [nr_interactions, error_value, prob_classe]
    
def lossFunction(sum_per_observation, prob_classe): 
    if(sum_per_observation > prob_classe): 
        return 1 
    else: 
        return 0

def basic_perceptron(nr_iterations, p_classe):
    predictions = [None] * len(population)
    for index in range(nr_iterations): 

        i = (index % len(population))
        soma_por_individuo = 0
        for index_weight in range(2): 
            soma_por_individuo += population[i][index_weight]*weights[index_weight]
        
        classe = lossFunction(soma_por_individuo, p_classe)

        predictions[i] = classe

        loss = classes[i] - classe
        if(classes[i] != classe):
            for ii in range(len(weights)): 
                weights[ii] = weights[ii] + (p_classe * loss * population[i][ii])
                
        #print(weights)
    return predictions

def perceptronAccurancy(original, predictions): 
    acc = str(1-sum([o - p for o, p in zip(original,predictions)])/len(original))
    return f"A taxa de precisão do nosso algoritmo Perceptron é: {acc}"

def createGraph()
    print("1")

def geral(): 
    #user inputs
    inputs = userInteractions() 
    nr_iterations = inputs[0]
    error_value = inputs[1]
    prob_classe = inputs[2]

    #dataset creation
    population = createDataset(10,2)
    classes = createClasses(10)
    weights = createWeights(2)

    #print(population)
    #print(classes)
    #print(weights)

    #perceptron
    predictions = basic_perceptron(nr_iterations,prob_classe)
    print(predictions)

    #print(predictions)
    acc = perceptronAccurancy(classes, predictions)
    print(acc)