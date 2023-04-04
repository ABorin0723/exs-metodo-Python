# 5
# Crie um método que recebe uma lista por parâmetro e imprime os elementos da lista recebida.

def getList(lista):

    lista = []
    
    listSize = int(input("qual o tamanho da lista? "))

    for i in range(listSize):
        item = input("qual o item? ")
        lista.append(item)

    for i in lista:
        print(i)

lista = []

getList(lista)
