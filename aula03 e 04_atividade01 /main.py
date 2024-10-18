import os
from random import randint

def limpar_tela():
    os.system("clear")

def ficha(personagem):
    limpar_tela()
    print("------------------------------")
    print(f"Ficha do personagem")
    print("------------------------------")
    print(f"{personagem['nome']}, Pv: {personagem['pv']}")
    print(f"Nivel: {personagem['nivel']}, com exp: {personagem['exptotal']}")
    print(f"Moedas de ouro: {personagem['moedas']}")
    print("------------------------------")
    input("-Aperte ENTER para continuar-")
    limpar_tela()

def rolar_dados():
    soma = 0
    for jogada in range(1, 4):
        dado = randint(1, 6)
        print(f"Tentativa: {jogada}, dado: {dado}")
        soma += dado
    return soma

def masmorra(personagem):
    while True:
        limpar_tela()
        codigo = randint(1, 18)
        soma_dados = rolar_dados()
        print(f"Soma do dado: {soma_dados} :: Codigo: {codigo}")
        print("------------------------------")
        
        if soma_dados == codigo:
            print("Você Acertou \nGanhou 10 moedas de ouro e 2 exp")
            personagem['moedas'] += 10
            personagem['exp'] += 2
            personagem['exptotal'] += 2
            if personagem['exp'] >= 4:
                personagem['pv'] += 1
                personagem['nivel'] += 1
                personagem['exp'] = 0
                print(f"Você subiu de nível\n Ganhou mais 1 vida")
        else:
            print("Errou")
            personagem['pv'] -= 1
            print(f"Perdeu 1 ponto de vida")
            if personagem['pv'] <= 0:
                limpar_tela()
                print(f"Você morreu")
                input("-Aperte ENTER para continuar-")
                break
        limpar_tela()
        input("-Aperte ENTER para continuar-")
        ficha(personagem)
        
        entrar = input("Entrar na masmorra s/n: ").strip().lower()
        if entrar != 's':
            break

def main():
    limpar_tela()
    nome = input("Digite um nome: ").strip()
    
    personagem = {
        'nome': nome,
        'nivel': 1,
        'exp': 0,
        'exptotal': 0,
        'pv': 3,
        'moedas': 0
    }

    limpar_tela()
    ficha(personagem)
    limpar_tela()
    
    entrar = input("Entrar na masmorra s/n: ").strip().lower()
    limpar_tela()
    
    if entrar == 's':
        masmorra(personagem)

    limpar_tela()
    print("-------Saída-------------")
    ficha(personagem)

if __name__ == "__main__":
    main()
