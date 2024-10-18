def cadastro_notas(qtdalunos,alunos):
  nome=str(input('Qual o nome do aluno? '))
  nota=float(input('Qual a nota do aluno? '))
  alunos[nome]=nota
  return alunos
  
  
qtdalunos=int(input('Quantos alunos quer cadastrar? '))
alunos={}
for i in range(0,qtdalunos):
  cadastro_notas(qtdalunos,alunos)
print(f'Dic alunos {alunos}')