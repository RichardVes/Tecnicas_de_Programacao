#------------------------------------------------------------#
# Ex 1
def ex1():
  def cadastrar_aluno(alunos):
      nome = input("Digite o nome do aluno: ")
      nota = float(input(f"Digite a nota do(a) {nome}: "))
      alunos[nome] = nota
      return alunos

  alunos = {}
  for i in range(3):  
      alunos = cadastrar_aluno(alunos)
  print(alunos)
#------------------------------------------------------------#
#Ex2
def ex2():
  def atualizar_precos(produtos, aumento_percentual):
      for produto in produtos:
          produtos[produto] = produtos[produto] * (1 + aumento_percentual / 100)
      return produtos

  produtos = {"arroz": 10.0, "feijão": 8.0, "macarrão": 6.5}
  percentual = 10  # Aumento de 10%
  print(atualizar_precos(produtos, percentual))
#------------------------------------------------------------#
#ex3
def ex3():
  def calcular_media_alunos(dicionario_notas):
      dicionario_medias = {}
      for aluno, notas in dicionario_notas.items():
          media = sum(notas) / len(notas)
          dicionario_medias[aluno] = media
      return dicionario_medias

  notas_alunos = {
      "Ana": [8.5, 9.0, 7.5],
      "Pedro": [6.0, 5.5, 7.0],
      "Maria": [9.0, 9.5, 10.0]
  }
  print(calcular_media_alunos(notas_alunos))
#------------------------------------------------------------#
#Menu
escolha=int(input('Qual exercicio mostrar ?'))
if escolha ==1:
  ex1()
elif escolha==2:
   ex2()
else:
   ex3()