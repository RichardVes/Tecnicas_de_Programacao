produtos={}
while True:
  print("""[1] Cadastro de Profutos
[0] Sair e Mostrar a Lista
      """)
  menu=int(input("O que você quer fazer?"))
  if menu==0:
    print(produtos)
    break
  elif menu==1:
    nome=input("Qual o nome do profuto?")
    valor=int(input("Qual o valor do produto"))
    produtos[nome]=valor