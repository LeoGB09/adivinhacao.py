import random

print("---------------------------------------------------------------------------")

print("Bem vindo ao jogo de Adivinhação")

numero_secreto = random.randrange(1, 101)
rodadas = 0

print("Escolha o nivel de dificuldade")
print("---------------------------------------------------------------------------")
print("|(1) Facíl: 10 tentativas|(2) Médio: 6 tentativas|(3) Dificil: 4 tentativas|")
print("---------------------------------------------------------------------------")
nivel = int(input("Qual o nivel de dificuldade?:"))

if(nivel == 1):
    rodadas = 10
elif(nivel == 2):
    rodadas = 6
else:
    rodadas = 4

for tentativas in range(1, rodadas + 1):
    
    numero_chute = int(input("Digite um número entre 1 e 100:"))

    if(numero_chute < 1 or numero_chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue

    acertou = numero_chute == numero_secreto
    maior = numero_chute > numero_secreto
    menor = numero_chute < numero_secreto
    print("------------------------")
    print(f"TENTATIVA {tentativas} DE {rodadas}")
    print("------------------------")
    print("Você digitou:", numero_chute)
    
    if (acertou):
        print("Parabens, você acertou")
        break
    else:
        if(maior):
            print("Você errou, o numero secreto é menor")
            if(tentativas == rodadas):
                print(f"O numero secreto era {numero_secreto}")
        elif(menor):
            print("Você errou, o numero secreto é maior")
            if(tentativas == rodadas):
                print(f"O numero secreto era {numero_secreto}")

print("---------------------")
print("-----Fim de Jogo-----")
print("---------------------")

print("------------------------------------------------------------------")