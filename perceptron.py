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
    