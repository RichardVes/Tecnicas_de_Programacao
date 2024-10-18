ctrl + shift + vs

---

# ROTINAS

## função

def nome():
parametros

chamada;
nome()

##-parametros
def nome(parametro,parametro2):
ex
def linha(parametro,parametro2):
print('-='*parametro)
print(parametro2)
print('-='*parametro)

#-----DOCSTRINGS------
se usa comando help(função), para mostrar a documentação da função;
def nome():
"""
Texto de documentação da sua função
"""

para ler digite
help(nome)

#x--- aula de Discionario ---
##-Identificando e diferencioando-
tupla=()
lista=[]
discionario={}

##-Estrutura do dicionario-
nome={'indice':valor,'indice2':valor2}
ex
cpf={'nome':'Richard','numero':000}
print(cpf) ou print(cpf['nome'])

- keys(),Values() e items()-
  ex: print(cpf.values())
  print(cpf.keys())
  print(cpf.items())

-keys() = são as chaves dos nomes
ex: 'nome' e 'numero'
-values() = são os valores
ex: 'Richard' e 000
-items() = são as keys() e values() juntos
ex: 'nome':'Richard', 'numero':000

##-Tipos de saida do discionario -
ex: pessoa={'nome':'Ana','idade':22','peso':70}
print(pessoa)
print(f'{pessoa["nome"]}')
print(f'A {pessoa["nome"]} tem {pessoa["idade"]} e {pessoa["peso"]kg})

print(pessoa.values())
print(pessoa.keys())
print(pessoa.items())

for k,v in pessoa.items():
print(f'{k} = {v}')

##-Editar elemento
nome{'chave'} = novo valor

##-Adcionar indice
nome['indice3']=valor3
##-Apagar indice
del nome['indice']
nome.pop('indice')

-Verifica KEY no dicionario
if "chave" in dicionario:
print(f'Existe')
else:
print(f'Não existe')

-Verifica VALUES no dicionario
if "valor" in dicionario.values():
print(f'Existe')
else:
print(f'Não existe')

#-=--=--=-Cores-=--=--=--=-
\033[style;text;backgroud m
\033[0;33;44m
\033[m tira a formatação

style [ 0 - nenhum| 1 - negrito | 4 - underline | 7 negativo]
text [30 a 37] {branco,vermelhor,verde,amarelo,azul,roxo,ciano,cinza}
background [40 a 47] {branco,vermelhor,verde,amarelo,azul,roxo,ciano,cinza}
ex:
cores={'limpa':'\033[m',
'vermelho':'\033[31m',
'verde':'\033[32m',
'amarelo': '\033[33m',
'azul':'\033[34m',
'pretoebranco':'\033[7:30m'
}
nome ='Richard'
print(f"Meu nome é {cores['azul']}{nome}{cores['limpa']} !!!")

###+++++++++++++++++++++++++++++++++
#--- Dicionario{} dentro de uma lista[] ---
pessoas =[]
pessoa1={'nome':'Ana','idade':'20'}
pessoa2={'nome':'Joao','idade':30}
pessoas.append(pessoa1)
pessoas.append(pessoa2)
print(pessoas)
print(pessoas[0])
print(pessoas[1]['nome'])
