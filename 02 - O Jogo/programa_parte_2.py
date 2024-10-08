#Autor: Richard
from random import randint
from os import system
from time import sleep
import math
system("clear")

#DEFININDO A LISTA GENERICA
#nome=vidaMaxima,VidaAtual,Atque,defesa, exp , nivel (jogador) ,
#nome= NOME 0, HPMAX 1 , HP 2, ATK 3, DEF 4, EXP 5 , LVL 6 , loot
monstroF=['Goblin',5,5,1,0,1]
monstroM=['Ork',10,8,3,1,3]
monstroD=['Gigante',15,15,6,2,10]
monstroBoss=['Dragão Vermelho',50,50,10,5,100]
nome=str(input("Digite o nome do Aventureiro: "))
jogador=[nome,5,5,3,1,0,1]
system("clear")
sair=1
while sair!=0:
  #Ficha inicial
  print(f"-=-=-=-=-=-=-=Aventureiro=-=-=-=-=-=-=-")
  print(f"""{jogador[0]}, Level:{jogador[6]}, exp:{jogador[5]}
  Vida:{jogador[2]}, Ataque:{jogador[3]}, Defesa:{jogador[4]},""")
  print("-="*20)
  sleep(2)
  explorar=str(input("Você quer explorar a Caverna? s/n: ")).lower()
  system("clear")
  if explorar == 'n':
      break
  elif explorar == 's':
      encontro=randint(0,100)

      if   encontro<=54: #Monstro Facil
          print("-=" * 20)
          print(f"Você encontrou um {monstroF[0]}")
          print(f"Vida:{monstroF[2]}, Ataque:{monstroF[3]}, Defesa:{monstroF[4]}")
          print("-=" * 20)
          sleep(2)
          while jogador[2]>0 or monstroF[2]>0:
            dano=jogador[3]-monstroF[4]
            if dano>0:
              print(f"Voce causou {dano} de dano ao {monstroF[0]}!")
              monstroF[2]-=dano
              sleep(1.5)
              if monstroF[2]<0:
                monstroF[2]=0
                print(f"{monstroF[0]}, {monstroF[2]} vida restante")
            else:
              print(f"O {monstroF[0]} esquivou!")
              sleep(1.5)
            if monstroF[2]==0:
              print(f"O {monstroF[0]} foi derrotado!")
              jogador[5]+=monstroF[5]
              monstroF[2]=monstroF[1] #reseta o hp 
              sleep(1.5)
              break
            else:
              sleep(1.5)
              dano=monstroF[3]-jogador[4]
              if dano>0:
                print(f"O {monstroF[0]} causou {dano} de dano em você!")
                jogador[2]-=dano
                sleep(1.5)
                if jogador[2]<0:
                  jogador[2]=0
                  print(f"{jogador[0]}, sua vida atual é {jogador[2]}")
                  sleep(1.5)
                if jogador[2] == 0:
                  print(f"{jogador[0]}, você morreu!!!")
                  sleep(1.5)
                  sair=0
                  break
              else:
                print(f"Você se esquivou do ataque do {monstroF[0]}!")
                sleep(1.5)
          sleep(1) 
          var=input("\nAperte a Tecla ENTER para continuar...")
            
      elif encontro>=55 and encontro<74: #Monstro Medio
          print("-=" * 20)
          print(f"Você encontrou um {monstroM[0]}")
          print(f"Vida:{monstroM[2]}, Ataque:{monstroM[3]}, Defesa:{monstroM[4]}")
          print("-=" * 20)
          sleep(2)
          while jogador[2]>0 or monstroM[2]>0:
            dano=jogador[3]-monstroM[4]
            if dano>0:
              print(f"Voce causou {dano} de dano ao {monstroM[0]}!")
              monstroM[2]-=dano
              sleep(1.5)
              if monstroM[2]<0:
                monstroM[2]=0
                print(f"{monstroM[0]}, {monstroM[2]} vida restante")
            else:
              print(f"O {monstroM[0]} esquivou!")
              sleep(1.5)
            if monstroM[2]==0:
              print(f"O {monstroM[0]} foi derrotado!")
              jogador[5]+=monstroM[5]
              monstroM[2]=monstroM[1] #reseta o hp 
              sleep(1.5)
              break
            else:
              sleep(1.5)
              dano=monstroM[3]-jogador[4]
              if dano>0:
                print(f"O {monstroM[0]} causou {dano} de dano em você!")
                jogador[2]-=dano
                sleep(1.5)
                if jogador[2]<0:
                  jogador[2]=0
                  print(f"{jogador[0]}, sua vida atual é {jogador[2]}")
                  sleep(1.5)
                if jogador[2] == 0:
                  print(f"{jogador[0]}, você morreu!!!")
                  sleep(1.5)
                  sair=0
                  break
              else:
                print(f"Você se esquivou do ataque do {monstroM[0]}!")
                sleep(1.5)
          sleep(1) 
          var=input("\nAperte a Tecla ENTER para continuar...")
            
      elif encontro>=75 and encontro<94: #Monstro Dificil
          print("-=" * 20)
          print(f"Você encontrou um {monstroD[0]}")
          print(f"Vida:{monstroD[2]}, Ataque:{monstroD[3]}, Defesa:{monstroD[4]}")
          print("-=" * 20)
          sleep(2)
          while jogador[2]>0 or monstroD[2]>0:
            dano=jogador[3]-monstroD[4]
            if dano>0:
              print(f"Voce causou {dano} de dano ao {monstroD[0]}!")
              monstroD[2]-=dano
              sleep(1.5)
              if monstroD[2]<0:
                monstroD[2]=0
                print(f"{monstroD[0]}, {monstroD[2]} vida restante")
            else:
              print(f"O {monstroD[0]} esquivou!")
              sleep(1.5)
            if monstroD[2]==0:
              print(f"O {monstroD[0]} foi derrotado!")
              jogador[5]+=monstroD[5]
              monstroD[2]=monstroD[1] #reseta o hp 
              sleep(1.5)
              break
            else:
              sleep(1.5)
              dano=monstroD[3]-jogador[4]
              if dano>0:
                print(f"O {monstroD[0]} causou {dano} de dano em você!")
                jogador[2]-=dano
                sleep(1.5)
                if jogador[2]<0:
                  jogador[2]=0
                  print(f"{jogador[0]}, sua vida atual é {jogador[2]}")
                  sleep(1.5)
                if jogador[2] == 0:
                  print(f"{jogador[0]}, você morreu!!!")
                  sleep(1.5)
                  sair=0
                  break
              else:
                print(f"Você se esquivou do ataque do {monstroD[0]}!")
                sleep(1.5)
          sleep(1) 
          var=input("\nAperte a Tecla ENTER para continuar...")
          
      else: # encontro>=90 and encontro<100: #Monstro Boss
          print("-=" * 20)
          print(f"Você encontrou um {monstroBoss[0]}")
          print(f"Vida:{monstroBoss[2]}, Ataque:{monstroBoss[3]}, Defesa:{monstroBoss[4]}")
          print("-=" * 20)
          sleep(2)
          while jogador[2]>0 or monstroBoss[2]>0:
            dano=jogador[3]-monstroBoss[4]
            if dano>0:
              print(f"Voce causou {dano} de dano ao {monstroBoss[0]}!")
              monstroBoss[2]-=dano
              sleep(1.5)
              if monstroBoss[2]<0:
                monstroBoss[2]=0
                print(f"{monstroBoss[0]}, {monstroBoss[2]} vida restante")
            else:
              print(f"O {monstroBoss[0]} esquivou!")
              sleep(1.5)
            if monstroBoss[2]==0:
              print(f"O {monstroBoss[0]} foi derrotado!")
              jogador[5]+=monstroBoss[5]
              monstroBoss[2]=monstroBoss[1] #reseta o hp 
              sleep(1.5)
              break
            else:
              sleep(1.5)
              dano=monstroBoss[3]-jogador[4]
              if dano>0:
                print(f"O {monstroBoss[0]} causou {dano} de dano em você!")
                jogador[2]-=dano
                sleep(1.5)
                if jogador[2]<0:
                  jogador[2]=0
                  print(f"{jogador[0]}, sua vida atual é {jogador[2]}")
                  sleep(1.5)
                if jogador[2] == 0:
                  print(f"{jogador[0]}, você morreu!!!")
                  sleep(1.5)
                  sair=0
                  break
              else:
                print(f"Você se esquivou do ataque do {monstroBoss[0]}!")
                sleep(1.5)
          sleep(1) 
          var=input("\nAperte a Tecla ENTER para continuar...")
          

  else:
    print("Você digitou um valor invalido")  # else caverna

  # nome= NOME 0, HPMAX 1 , HP 2, ATK 3, DEF 4, EXP 5 , LVL 6 , loot
  expTotal=math.ceil((jogador[6]+1)*1.1)
  #print(f"exp total {expTotal}")
  #print(f"exp atual {jogador[5]}")
  system("clear")

  if jogador[5] >= expTotal:
    jogador[5] =0
    jogador[6]+=1
    print(f'Nivel {jogador[6]}')
    jogador[1]+=5
    jogador[2]=jogador[1]
  #  print(f"{jogador[0]}, vida max{jogador[1]}, vida atual{jogador[2]}")
    if jogador[6]%2==0:
      pass
    else:
      jogador[3]+=1
      jogador[4]+=1
      print(f"{jogador[0]}, subiu dano{jogador[3]} e defesa{jogador[4]}")

    

system("clear")
if jogador[2] >0:
  print(f"{jogador[0]}, você saiu da Caverna com vida!")
  print(f"-=-=-=-=-=-=-=Aventureiro=-=-=-=-=-=-=-")
else:
  print(f"O corpo do aventureiro {jogador[0]}, foi tirado da caverna em pedaços!")
  print(f"-=-=-=-=-=-=-=OBTUARIO=-=-=-=-=-=-=-")
#Ficha inicial
print(f"""{jogador[0]}, Level:{jogador[6]}, exp:{jogador[5]}
Vida:{jogador[2]}, Ataque:{jogador[3]}, Defesa:{jogador[4]},""")
print("-="*20)