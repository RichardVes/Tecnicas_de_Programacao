#>>PARTE 1
#open("caminho","tipo")
# arquivo=open("aula08_arquivo/teste.txt","w")
# arquivo.write("Olá mundo")
# arquivo.close()

# >>> Parte 2
# arquivo=open("aula08_arquivo/teste.txt","r")
# print(arquivo.readable())
# #print(arquivo.read())
# #print(arquivo.readline())
# lista=arquivo.readlines()
# print(lista[0])
# arquivo.close()

#>>Parte 3
# arquivo = open("aula08_arquivo/teste.txt","a")
# arquivo.write("\nTexto")
# arquivo.close()

#>>Parte 4 
import ast

# Abre o arquivo e lê o conteúdo
# with open("aula08_arquivo/teste.txt", "r") as arquivo:
#     conteudo = arquivo.read()

arquivo=open("aula08_arquivo/teste.txt", "r")
conteudo=arquivo.read()
jogador = ast.literal_eval(conteudo)

# Acessa as características do dicionário
nome = jogador["nome"]
hp = jogador["hp"]
mana = jogador["mana"]

# Exibe as características
print(f"Nome: {nome}")
print(f"HP: {hp}")
print(f"Mana: {mana}")
arquivo.close()