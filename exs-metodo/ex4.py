# 4
# Crie um método que recebe um valor por parâmetro (assuma que será uma string)
# e retorna a quantidade de letras ou outros caracteres que não sejam espaço que existem neste texto

def carac(x):
    size = len(x)
    spaces = x.count(" ")
    return size - spaces

x = input("String ")

print(carac(x))