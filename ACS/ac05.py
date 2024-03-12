import random

def main():
    # Atributos do aventureiro e do monstro
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)
    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    # Exibir atributos iniciais
    print("Aventureiro: vida {} - att {} - def {}".format(vida_aventureiro, ataque_aventureiro, defesa_aventureiro))
    print("Monstro: vida {} - att {}".format(vida_monstro, ataque_monstro))

    # Loop do combate
    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print("\nRodada {}".format(rodada))

        # Ataque do aventureiro
        dano_aventureiro = random.randint(1, ataque_aventureiro)
        vida_monstro -= dano_aventureiro
        print("Aventureiro: vida {} - att {} - def {}".format(vida_aventureiro, ataque_aventureiro, defesa_aventureiro))
        print("Monstro: vida {} - att {}".format(vida_monstro, ataque_monstro))

        # Ataque do monstro
        if vida_monstro > 0:
            dano_monstro = random.randint(1, ataque_monstro) - defesa_aventureiro
            vida_aventureiro -= dano_monstro
            print("Aventureiro: vida {} - att {} - def {}".format(vida_aventureiro, ataque_aventureiro, defesa_aventureiro))
            print("Monstro: vida {} - att {}".format(vida_monstro, ataque_monstro))

        rodada += 1

    # Exibir resultado do combate
    if vida_aventureiro <= 0:
        print("\nO aventureiro morreu!")
    else:
        print("\nO monstro morreu!")

if __name__ == "__main__":
    main()