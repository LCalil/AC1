"""
Exercício 1: Revisite a Ac1
"""

#Equaçao do segundo grau
def eq_seg_grau():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c
    
    if delta < 0:
        return None
    
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    
    return raiz1, raiz2


raizes = eq_seg_grau()
if raizes is not None:
    print("As raízes da equação são:", raizes)
else:
    print("A equação não possui raízes reais.")




#Ano bissexto
    
def bissexto():
    ano = int(input('Digite um ano: '))
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
if bissexto():
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

