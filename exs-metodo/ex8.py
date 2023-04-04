# 8
# Crie um método que recebe um inteiro X por parâmetro e imprime os valores de 1 até X (inclusive).

def seq(x):
    
    repet = 1

    while repet <= x:
        print(repet)
        repet += 1

x = int(input("Qual o número? "))
seq(x)