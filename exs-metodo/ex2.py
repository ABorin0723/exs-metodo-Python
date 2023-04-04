# 2
# Crie um método chamado maiorValor que recebe 3 valores por parâmetro (assuma = inteiros) e retorna o maior dos três

def maiorValor(val1,val2,val3):
    if val1 > val2 and val2 > val3:
        return val1
    elif val2 > val1 and val1 > val3:
        return val2
    else:
        return val3
    
x = int(input("Valor 1: "))
y = int(input("Valor 2: "))
z = int(input("Valor 3: "))

print(maiorValor(x,y,z))