# 1 
# Crie um método que recebe dois valores val1 e val2 (assuma que serão inteiros). 
# O método deve retornar verdadeiro se val1 for divisível por val2 e falso caso contrário.

def divisaoExata(val1,val2):
    return val1 % val2 == 0

x = int(input("Primeiro valor "))
y = int(input("Segundo valor "))

print(divisaoExata(x,y))