# 6
# Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de string)
# e retorna a menor string da lista (com menos caracteres).

def menorList(listaLists):
    
    menor = None
    
    for i in listaLists:
        if menor is None or len(i) < len(menor):
            menor = i
    
    return menor

listaLists = []

listSize = int(input("qual o tamanho da lista? "))
for i in range(listSize):
    item = input("qual o item? ")
    listaLists.append(item)

print(menorList(listaLists))