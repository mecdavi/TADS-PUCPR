# David Eduard Machado de Camargo
# Tecnologia em análise e desenvolvimento de sistemas - Turma 01 - EAD

from ast import If
from errno import EILSEQ
from operator import indexOf
import random

def tuboDados(tubo):
    i = 1
    tubo = []
    for i in range(6):
        tubo.append('CPCTPC')
    for amarelo in range(4):
        tubo.append('TPCTPC')
    for vermlho in range(3):
        tubo.append('TPTCPT') 
    return tubo
    
    # zera pontuação
def zeraPontos(params):
    if(params == 's'):
        jogadorAtual = 0
        return jogadorAtual
    else:
        tiros = 0
        cerebros = 0
        passos = 0
        return tiros,passos,cerebros

def pegarDadosTubo(tubo):
    if (len(tubo) != 0):
        numDados = len(tubo) -1
        numSorteado = random.randint(0,numDados)
        dadoSorteado.append(tubo[numSorteado])
        tubo.pop(numSorteado)
        return dadoSorteado,tubo
    else:
        print("Tubo vazio")
        return 

def faceDado(dadoSorteado):
        numFace = random.randint(0,5)
        if dadoSorteado[numFace] == 'C':
            print('Cérebro - (Você comeu um cerebro)')
            return 'C'
        elif dadoSorteado[numFace] == 'P':
            print('Passos - (Uma vítima escapou)')
            return 'P'
        else:
            print('Tiro - (Você levou um tiro)')
            return 'T'

def situacaoTubo(tubo):
    corDado = []
    for dadoSorteado in range(len(tubo)):
        if tubo[dadoSorteado] == 'CPCTPC':
            corDado.append('Verde')
        elif tubo[dadoSorteado] == 'TPCTPC':
            corDado.append('Amarelo')
        elif tubo[dadoSorteado] == 'TPTCPT':
            corDado.append("Vermelho")
    return print(corDado)

def corDadoLancado(dado):
    if (dado == 'CPCTPC'):
        print('Verde')
    elif (dado == 'TPCTPC'):
        print('Amarelo')
    elif (dado == 'TPTCPT'):
        print("Vermelho")

def pontuacao(dadoROlado):
    cerebros = 0
    tiros = 0
    passos = 0
    for dadoROlado in dadosSorteados:
        numFace = random.randint(0,5)
        if dado[numFace] == 'C':
            print('Cérebro - (Você comeu um cerebro)')
            cerebros = cerebros + 1
        elif dadoSorteado == 'P':
            print('Passos - (Uma vítima escapou)')
            passos = passos + 1
        else:
            print('Tiro - (Você levou um tiro)')
            tiros = tiros + 1
        return cerebros,tiros,passos
    
print("Zombie dice")
print("Bem vindo novos jogadores")

numJogadores = 0
listaJogadores = []
jogadorAtual = 0

# dados 
tubo = []
tubo = tuboDados(tubo)
dadoSorteado = []

# dados no tubo
tudoJogador = []
# ações


#Pontuação
pontoCerebros = []
pontoTiros = []

# capturando informações dos jogadores (quantidade e nome) {
while (numJogadores <= 1):
    numJogadores = int(input('Informe o numero de jogadores: '))

    if numJogadores <= 1 :
        print('Retorne com seus amigos, o numero minímo de jogadores é 2')
    else:
        print("Bem vindo novos jogadores")

for i in range(numJogadores):
    jogador = input('Informe o nome do jogador ' + str(i+1) + ': ')
    listaJogadores.append(jogador)

print('Se preparem a invasão está começando... \n')

# }

# Rolagem de dados {
while jogadorAtual in range(len(listaJogadores)):
    tiro = 0
    passo = 0
    print("Turno de " + listaJogadores[jogadorAtual] +' começou, role os dados \n')
    situacaoTubo(tubo)
    print('\n')

    for i in range(3):
        pegarDadosTubo(tubo)
        corDadoLancado(dadoSorteado[i])
        faceDado(dadoSorteado[i])
        print('\n')
    pontuacao

    if(passosRodada == 3):
        print('A vitima fugiu, voce perdeu a vez')
        jogadorAtual = jogadorAtual + 1
        continue
# }

# Final ou novo lançamento de dados{
    continuarJogo = input('Você deseja continuar jogando os dados? (s = Sim / n = Não) \n')

    if continuarJogo == 'n':
        jogadorAtual = jogadorAtual +1
        dadosSorteados = []
        zeraPontos(continuarJogo)
        
        if jogadorAtual == len(listaJogadores):
            print('A invasão zumbi já está acabando')
            continue
    
    elif continuarJogo == 's':
        print('Iniciando mais uma rodada do turno atual ...')
        dadosSorteados = []
        if jogadorAtual == 0:
            zeraPontos(continuarJogo)
            #jogadorAtual = 0
        else:
            jogadorAtual = jogadorAtual - 1    
# }            
