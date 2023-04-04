# 3
# Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e
# retorna a soma de todos os valores entre 0 e o valor recebido. Caso o valor seja negativo, o
# método deve retornar -1.

# while
def soma(x):
    if x <= 0:
        return -1
    cont = 0
    soma = 0
    while cont < x:
        soma += cont
        cont += 1
    return soma

x = int(input("valor: "))

print(soma(x))

#for
def soma(y):
    if y <= 0:
        return -1
    soma = 0
    for i in range(0,y):
        soma += i
    return soma

y = int(input("valor: "))

print(soma(y))