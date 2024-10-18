import os
from random import randint
os.system("clear")
nivel=1
exp=0
exptotal=0
pv=3
moedas=0
soma=0

nome=input("Digite um nome: ")
os.system("clear")
print("------------------------------")
print(f"Ficha do personagem")
print(f"Nome do personagem: {nome}")
print(f"Pontos de vida: {pv}")
print(f"Nivel: {nivel}, com exp:{exptotal}")
print(f"Moedas de ouro: {moedas}")
print("------------------------------")
cont=input("-Aperte ENTER para continuar-")
os.system("clear")
entrar =input("Entrar na masmorra s/n: ")
os.system("clear")
#Enigma
while True:
  if entrar=="s" or entrar=="S":
    codigo=randint(1,18)
    #codigo=6 #forçar ganhar
    #print(f"Codigo secreto: {codigo}") #mostra o codigo
    for jogada in range(1,4):
      dado=randint(1,6)
      #dado=2 #forçar ganhar
      print(f"Tentativa:{jogada}, dado:{dado}")
      soma=soma+dado
    print(f"Soma do dado:{soma} :: Codigo:{codigo}")
    print("------------------------------")
    if soma==codigo:
      print("Você Acertou \nGanhou 10 moedas de ouro e 2 exp")
      moedas=moedas+10
      exp=exp+2
      exptotal=exptotal+2
      if exp==4:
        pv=pv+1
        nivel=nivel+1
        exp=0
        print(f"Você subiu de nivel\n Ganhou mais 1 vida")
      dado=0
      soma=0
      print("------------------------------")
      cont=input("-Aperte ENTER para continuar-")
    else:#Errou
      print("Errou")
      pv=pv-1
      print(f"Perdeu 1 ponto de vida")
      cont=input("-Aperte ENTER para continuar-")
      dado=0
      soma=0
      if pv<=0:
        os.system("clear")
        print(f"Você morreu")
        cont=input("-Aperte ENTER para continuar-")
        break
  elif entrar=="n" or entrar=="N":
    break
  else:#Tecla errada
    os.system("clear")
    print(f"Você digitou uma tecla invalida")
    print("------------------------------")
    cont=input("-Aperte ENTER para continuar-")

  os.system("clear")
  print("------------------------")
  print(f"Status atual do Personagem")
  print("------------------------")
  print(f"{nome}, Pv:{pv}")
  print(f"Nivel: {nivel}, com exp:{exptotal}")
  print(f"Moedas de ouro: {moedas}")
  print("------------------------------")
  cont=input("-Aperte ENTER para continuar-")
  os.system("clear")
  entrar =input("Entrar na masmorra s/n: ")
  os.system("clear")

os.system("clear")
print("-------Saida-------------")
print(f"Ficha do personagem")
print(f"{nome}, Pv:{pv}")
print(f"Nivel: {nivel}, com exp:{exptotal}")
print(f"Moedas de ouro: {moedas}")
print("------------------------------")