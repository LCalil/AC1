def ler_nome_usuario():
    nome = input('Informe o seu nome:')
    if nome == "":
        return print('Nome invalido.')
    else:
        return nome




def ler_notas():
    ap1 = float(input('Informe a nota da ap1: '))
    ap2 = float(input('Informe a nota da ap2: '))
    asub = float(input('Informe a nota da asub: '))
    ac = float(input('Informe a nota da AC: '))
    return ap1, ap2, asub, ac


def validar_notas(ap1, ap2, asub, ac):
    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return True
    else:
        return print('Nota invalida!')


def duas_maiores_notas(ap1, ap2, asub):
    if ap1 < asub:
        return asub, ap2
    if ap2 < asub:
        return asub, ap1

    return ap1, ap2


def calcular_media(n1, n2, ac):
    return(n1 + n2) * 0.4 + ac * 0.2


def informar_aprovacao(media):
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabéns, você foi aprovado!")
    else:
        print("Você foi reprovado...")

def le_nota():
    nota1 = float(input('Informe primeira nota: '))
    nota2 = float(input('Informe segunda nota: '))



def main():
    nome = ler_nome_usuario()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

main()
