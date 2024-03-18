"""
Exercício 01: triângulo
"""
def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return"Não é um triângulo"
    if a == b == c:
        return'Equilátero'
    elif a == b or b == c or a == c:
        return'Isósceles'
    else:
            return'Escaleno'

def testa_triangulo():
    (determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
    
def main():
    testa_triangulo()

main()


"""
Exercício 02:  dia da semana
"""

def dia_semana(numero):
    if numero == 1:
         return'Domingo' 
    elif numero == 2:
         return'Segunda' 
    elif numero == 3:
         return'Terça'
    elif numero == 4:
         return'Quarta'
    elif numero == 5:
         return'Quinta'
    elif numero == 6:
        return'Sexta'
    elif numero == 7:
         return'Sabado' 
    else:
         return""

def testa_dia_semana():
     numero = int(input('Digite o número correspondente ao dia da semana (1 a 7):'))
     print(dia_semana(numero))

testa_dia_semana()


"""
Exercício 3: calculadora simples

"""


def soma(a, b):
     return a + b
def subtracao(a, b):
     return a - b
def multiplicacao(a, b):
     return a * b
def divisao(a, b):
    if b == 0:
        return'Operação inválida' 
    
def elabora_interface():
    print("Informe um número: ", end="")
    a = float(input())
    print("Informe outro número: ", end="")
    b = float(input())
    print("Informe a operação: ", end="")
    operacao = input().lower()
    if operacao == "soma":
        resultado = soma(a, b)
    elif operacao == "subtração":
        resultado = subtracao(a, b)
    elif operacao == "multiplicação":
        resultado = multiplicacao(a, b)
    elif operacao == "divisão":
        resultado = divisao(a, b)
    else:
        resultado = "operação inválida"
    print("Resultado: ", resultado)

elabora_interface()
