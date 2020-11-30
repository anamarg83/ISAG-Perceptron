# função criar dataset + criar os valores para as classes + criar weights 
# função para interagir com o utilizador (numero de iterações + erro + valor da probabilidade de escolher a classes)
# função do algoritmo 
    # função calculo dos pesos 
    # função calculo do erro 
    # função calculo da previsão 
# função de criação do gráfico 

# Import Libraries
from random import choices

# Criação da população 
def createDataset(nrows, nvariables): 
    return [choices(range(1,nrows),k=nrows) for _ in range(nvariables)]

#final_values = [1,0,1,0,1]
#weights = [9,5]
#population = createDataset(5,2)

def interaccaoUtilizador(): 
    print("número de iterações?")
    ite = input()
    
    print("erro?")
    ite = input()

def basic_perceptron():
    populacao = [[0.3,0.7,0.1],[-0.6,0.3,0.2],[-0.1,-0.8,0.3],[0.1,-0.45,0.4]]
    final_values = [1,0,0,1]
    weights = [0.8,-0.5,-0.1]
    b = 0.5
    for index in range(len(populacao)): 
        print('index: '+ str(index))
        
        #print("STEP 1- peso atual: "+ str(weights[0]) + " - "+ str(weights[1]))
        soma_por_individuo = 0


        for index_pesos in range(2): 
            soma_por_individuo += populacao[index][index_pesos]*weights[index_pesos]
        #print(soma_por_individuo)
        
        classe = 0
        
        if(soma_por_individuo > b): 
            classe = 1 
        else: 
            classe = 0
        #print(classe)

        previsao = final_values[index] - classe
        #print(previsao)
        
        if(final_values[index] != classe):
            for index_pesos in range(len(weights)): 
                #print("STEP 2- peso atual: "+ str(weights[index_pesos])+ " b: " +str(b) + " previsao: "+ str(previsao) + " pop: " + str(populacao[index][index_pesos]))
                weights[index_pesos] = weights[index_pesos] + (b * previsao * populacao[index][index_pesos])
                
        print(weights)
    