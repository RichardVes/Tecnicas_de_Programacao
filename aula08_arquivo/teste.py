import ast

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