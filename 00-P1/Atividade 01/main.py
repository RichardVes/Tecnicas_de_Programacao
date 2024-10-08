import os
from random import randint
os.system("clear")
nivel=1
exp=0
pv=3
moedas=0
nome=input("DIgite um nome: ")
os.system("clear")
print("-="*20)
print(f"Ficha do personagem")
print(f"Nome do personagem: {nome}")
print(f"Pontos de vida: {pv}")
print(f"Nivel: {nivel}, com exp:{exp}")
print(f"Moedas de ouro: {moedas}")
print("-="*20)
cont=input("Aperte Enter para continuar")
os.system("clear")
entrar =input("Entrar na masmorra s/n: ")
os.system("clear")
#Enigma
while True:
  if entrar=="s" or entrar=="S":
    codigo=randint(1,18)
    print(f"Codigo secreto: {codigo}")
    for jogada in range(1,4):
      dado=randint(1,6)
      print(f"Tentativa:{jogada}, {codigo}")
      if dado==codigo:
        print("Acertou")
      else:
        print("Errou")
        break

  elif entrar=="n" or entrar=="N":
    break
  entrar =input("Entrar na masmorra s/n")

os.system("clear")
print("-="*20)
print(f"Ficha do personagem")
print(f"Nome do personagem: {nome}")
print(f"Pontos de vida: {pv}")
print(f"Nivel: {nivel}, com exp:{exp}")
print(f"Moedas de ouro: {moedas}")
print("-="*20)