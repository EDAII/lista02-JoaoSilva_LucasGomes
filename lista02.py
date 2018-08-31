import random
import os
from sys import exit

def action():
    os.system('clear')
    while True:  # Validação do tipo de ordenação
        typeSort = int(input(("\n0 - Sair do programa"
                              "\n1 - Selection sort"
                              "\n2 - Insertion sort"
                              "\n3 - Bubble sort"
                              "\nEscolha um tipo de ordenação: ")))
        try:
            if (typeSort < 0 or typeSort > 3):
                raise ValueError(typeSort)
        except ValueError as e:
            print("Valor inválido: ", e)
            os.system('clear')
        else:
            break
    return typeSort

def selectionSort(vector):

    for i in range(len(vector)-1):
        smallerNum = i
        for j in range(i+1,len(vector)):
            if(vector[j] < vector[smallerNum]):
                smallerNum = j
        if(smallerNum is not i):
            print("O {} trocou de lugar com o {}".format(vector[smallerNum],vector[i]))
            vector[i], vector[smallerNum] = vector[smallerNum], vector[i]
            print(vector)
    input("\nPressione ENTER para continuar...")

def insertionSort(vector):

    for i in range(len(vector)-1):
        print("Posição {}".format(i))
        for j in range(i+1,0,-1):
            if(vector[j] < vector[j-1]):
                vector[j],vector[j-1] = vector[j-1],vector[j]
                print(vector)

    input("\nPressione ENTER para continuar...")

def bubbleSort(vector):
    swap = True
    n = 0
    while(swap):
        swap = False
        print("{}º passada".format(n+1))
        for i in range(0,len(vector) - 1 ):
            if(vector[i] > vector[i+1]):
                vector[i],vector[i+1] = vector[i+1],vector[i]
                print(vector)
                swap = True
        n += 1

    input("\nPressione ENTER para continuar...")

def main():
    num = int(input("Digite o maior numero possível que pode estar presente na lista: "))

    while True: #Validação do tamanho do vetor
        try:
            size = int(input("Digite o tamanho do vetor, sendo ele menor ou igual ao limite superior da lista("+str(num)+"): "))
            if (size > num):
                raise ValueError(size)
        except ValueError as e:
            print("Valor inválido:",e)
        else:
            break

    typeSort = action()

    while typeSort is not 0:
        vector = random.sample(range(num),size) #Comando para gerar um vetor não ordenado de tamanho size de 0 ate num randomicamente
        os.system('clear')
        print("Vetor desordenado: \n{}".format(vector))

        if(typeSort is 1):
            selectionSort(vector)
        elif(typeSort is 2):
            insertionSort(vector)
        elif(typeSort is 3):
            bubbleSort(vector)

        typeSort = action()

main()