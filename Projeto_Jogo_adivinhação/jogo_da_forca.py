def jogar():
    print("**********************************")
    print("**********************************")
    print("***Bem vindo ao jogo da Forca!****")
    print("**********************************")
    print("**********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        chute = input("Digite uma letra.")
        chute = chute.strip()

        indice = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição{}".format(letra, indice))
            indice = indice + 1
        print("jogando...")
    print("Fim do jogo")


if __name__=="__main__":
    jogar()
