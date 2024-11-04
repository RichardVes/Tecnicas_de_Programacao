# Aula 08

---

## Leitura e escrita de arquivos

> Para criar arquivos e abrí-los, utilizamos o **método open()**.
> Este método irá abrir o arquivo que passarmos como parâmetro com um determinado modo de uso (**que também será passado como parâmetro**)
>
> **open(nome_do_arquivo, modo_de_funcionamento).**
>
> ## Há diversos modos de uso, como podemos ver abaixo:
>
> > **'r': modo de leitura,** o arquivo deve existir previamente
> >
> > **'w': modo de escrita,** se o arquivo não existir, ele será criado
> >
> > **'a': modo de anexar,** adiciona informações ao final do arquivo
> >
> > **'x': modo exclusivo,** cria um novo arquivo somente se ele não existir
> >
> > **'r+' : modo de leitura e escrita**
> >
> > > Outros exemplos:
> > >
> > > **'b': modo binário,** usado para arquivos binários, como imagens ou vídeos
> > >
> > > **'t': modo de texto,** usado para arquivos de texto

## Observações inicias

> Toda vez que abrir um arquivo, feche;
>
> ```
> arquivo = open("caminho","r")
>
> ```
>
> ### verifica se é possivel ler o >arquivo
>
> ```
> arquivo.readable()
> ```
>
> ```
> arquivo.close()
>
> ```

o método **read()**, retorna todo o conteúdo do arquivo como uma string.

Veja o exemplo abaixo:

```
arquivo = open('texto.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
ou
print(arquivo.read())
```

É possível ler o arquivo linha por linha utilizando o método **readline()**.

Este método retorna uma única linha do arquivo por vez. Veja um exemplo:

```
arquivo = open('texto.txt', 'r')
linha = arquivo.readline()
print(linha)
ou
print(arquivo.readline())
ou
lista=arquivo.readlines() # cria uma lista com cada linha do arquivo
print(lista)
```

---

## Escrevendo em um arquivo em Python

### "a" --> append

> Além de ler arquivos, também é possível escrever informações em um arquivo usando Python.
>
> Para isso, utilizamos o método **write()**.
>
> Vejamos um exemplo:
>
> ```
> arquivo = open('novo_texto.txt', 'a')
> arquivo.write('Olá, Mundo!')
> arquivo.close()
> ```
>
> Neste exemplo, criamos um novo arquivo chamado “novo_texto.txt” e escrevemos a string “Olá, Mundo!” no arquivo.
>
> Em seguida, fechamos o arquivo utilizando o método close().
>
> É importante fechar o arquivo depois de terminar de escrever para liberar os recursos do sistema operacional.

### "w" --> write

> O modo write cria um arquivo com o texto passado ou apaga o arquivo e escreve somente o que for passado
>
> Vejamos um exemplo:
>
> ```
> arquivo = open('novo_texto.txt', 'w')
> arquivo.write('Olá, Mundo!')
> arquivo.close()
> ```
>
> O comando apaga tudo e escreve o texto "Olá, Mundo!" no arquivo.

### "r+" --> append

> ## Permite ler e escrever ao mesmo tempo o arquivo, com umas resalvas

## Manipulando arquivos com o statement with

> Além de abrir e fechar arquivos manualmente, Python também oferece uma sintaxe mais conveniente para manipulação de arquivos.
>
> O statement with é usado para abrir um arquivo e garantir que ele seja fechado corretamente, mesmo em caso de erro.
>
> Vejamos um exemplo:
>
> ```
> with open('texto.txt', 'r') as arquivo:
> conteudo = arquivo.read()
> print(conteudo)
> ```
>
> Neste exemplo, o arquivo é aberto dentro do bloco with e o conteúdo é lido e armazenado na variável conteudo.
>
> Ao final do bloco with, o arquivo é automaticamente fechado, mesmo que ocorra uma exceção durante a leitura.
>
> O statement with é especialmente útil quando manipulamos arquivos grandes ou quando há várias operações a serem realizadas no arquivo.
>
> Ele garante que os recursos do sistema operacional sejam liberados de forma eficiente.
