print("********************************")
print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")
print("********************************")
#  definição número secreto
numerosecreto = 22
totaldetentativas = 3
rodada = 1

for rodada in range(1, totaldetentativas + 1):
    print("tentativa {} de {}".format(rodada, totaldetentativas))
#estrutura da entreda de dados
    chutejogador = input("Chute um numero de 0 a 50:")
    print("você digitou", chutejogador)
#convertendo chutejogador para inteiro e passando para variavel chute
    chute = int(chutejogador)
# se numerosecreto for igual a chute se não você errou
    if numerosecreto == chute:
        print("Você acertou")
   
    else:
        if chute > numerosecreto:
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif chute < numerosecreto:
            print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim do jogo")


