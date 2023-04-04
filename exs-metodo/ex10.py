# 10
# Crie um método que recebe um inteiro por parâmetro e retorna verdadeiro caso
# seja um valor primo e falso caso contrário. Caso o parâmetro seja negativo o método deve
# retornar falso.

def isPrimo(x):

    if x <= 1:
        return False
    elif x == 2 or x == 3 or x == 5:
        return True
    else:
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
            return True
        else:
            return False
    

x = int(input("Qual o valor? "))
print(isPrimo(x))