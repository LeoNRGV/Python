import random
def jogar():
  print("==========================================")
  print("==========================================")
  print("Bien venido a lo juego de las adivinaçones")
  print("==========================================")
  print("==========================================")


  pontos = 1000

  print("Qual és el nivel de dificuidade?")
  print("[1] Facil \n[2] Medio \n[3] Dificil")
  nivel = int(input(" Defina el nivel: "))

  while nivel < 1 or nivel > 3:
      nivel = int (input("  Debes escolhir entre 1 e 3!\n \
  Defina el nivel: "))

  if(nivel == 1):
    totaldetentativas = 12
    numero_secreto = random.randint(0,40)
    numero1 = 0
    numero2 = 40
  elif(nivel == 2):
    totaldetentativas = 9
    numero_secreto = random.randint(0,70)
    numero1 = 0
    numero2 = 70  
  else:
    totaldetentativas = 6
    numero_secreto = random.randint(0,100)
    numero1 = 0
    numero2 = 100

  for rodada in range(1, totaldetentativas +1):
          
    print("Tentativa {} de {}".format (rodada, totaldetentativas))

    chute_str = input ("Entra tu numero, (Dica: adentro di {} i {}): ".format (numero1, numero2))
    print ("Tu escribiste: ", chute_str)
    chute = int(chute_str)

    if chute < 0 or chute > 100:
      print("Tú debes escribir un numero entri {} e {}!".format (numero1, numero2))
      continue

    if(numero_secreto == chute):
      print("Tienes razón! Parabáins!")
      print("Tu acertastes e fizestes {} ponto!".format(pontos))
      break

    else:
        if chute > numero_secreto:
          print("Tú error, tu numero és superior a lo numero secreto.")

        elif chute < numero_secreto:
          print("Tú error, tu numero és inferior a lo numero secreto.")

    pontos_perdidos = (totaldetentativas * 5 * nivel)
    pontos = pontos - pontos_perdidos
  print("Fine")
if __name__=="__main__":
   jogar()