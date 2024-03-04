ano = int(input('Digite o ano: '))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

print(f'O ano {ano} é bissexto?  {bissexto and "Sim" or "Não"}.   ')



#Calcula o delta 
def calcula_raizes (a, b, c):
    delta = b**2 - 4*a*c

    
    return delta

#Pergunta ao usuario os parâmetros da equação
a = float(input('Digite o "a" da equação: '))
b = float(input('Digite o "b" da equação: '))
c = float(input('Digite o "c" da equação: '))

# Atribui a funçao calcula_raizes a uma variavel
delta = calcula_raizes

#Calcula as raizes da equação
x1 = (- b + delta(a, b, c)**0.5 ) / (2*a)
x2 = (- b - delta(a, b, c)**0.5 ) / (2*a)

#Mostra ao usuario as raizes da equação
print('A primeira raiz é: ', x1)
print('A segunda raiz é: ', x2)

