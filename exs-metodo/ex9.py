# 9
# Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido
# pela média aritmética das notas. Os conceitos são:
# - entre 0.0 e 4.0 (inclusive): conceito "D"
# - entre 4.0 (não incluído) e 7.0 (inclusive): conceito "C"
# - entre 7.0 (não incluído) e 9.0 (inclusive): conceito "B"
# - entre 9.0 (não incluído) e 10.0 (inclusive): conceito "A"
# Caso alguma das notas digitadas seja negativa, retorne o texto "ERRO".

def media(a,b,c):

    if a < 0 or b < 0 or c < 0:
        return "ERRO, nenhuma das notar pode ser negativa"
    elif a > 10 or b > 10 or c > 10:
        return "ERRO, as notas só vão ate 10"
    else:
        mediaArit = (a+b+c)/3
        if mediaArit <= 4:
            return "D"
        elif mediaArit <= 7:
            return "C"
        elif mediaArit <= 9:
            return "B"
        else:
            return "A"

a = float(input("Nota A: "))
b = float(input("Nota B: "))
c = float(input("Nota C: "))

print(media(a,b,c))