import jogo_da_forca
import jogo_de_adivinhação

def escolher_jogo():
    print("**********************************")
    print("**********************************")
    print("******Escolha o seu jogo!*********")
    print("**********************************")
    print("**********************************")
    print("(1)Forca \n(2)Adivinhação")

    jogo = int(input("Qual jogo você quer jogar?\n"))

    if jogo == 1:
        print("jogando forca")
        jogo_da_forca.jogar()
    elif jogo == 2:
        print("jogando adivinhação")
        jogo_de_adivinhação.jogar()
    
if __name__=="__main__":
   escolher_jogo()
   