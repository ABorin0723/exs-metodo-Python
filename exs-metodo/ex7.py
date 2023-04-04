# 7
# Crie um método que recebe dois parâmetros, que serão um inteiro N e uma string S (nesta ordem).
# O método deve imprimir na tela N vezes a string S.

def repet(N,S):

    for i in range(N):
        print(S)

N = int(input("Qual a quantidade de repetições? "))
S = input("Qual a string? ")

repet(N,S)