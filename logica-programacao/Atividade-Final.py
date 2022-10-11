# Tecnologia em análise e desenvolvimento de sistemas - Turma 01 - EAD

from ast import If, Num
from errno import EILSEQ
from operator import index, indexOf, truediv
from os import listxattr
from pydoc import plain
import random
from re import T
#from winsound import PlaySound
from xmlrpc.client import FastParser

def pegarDadosVerde():
    return ("C", "P", "C", "T", "P", "C")
def pegarDadosAmarelo():
    return ("T", "P", "C", "T", "P", "C")
def pegarDadosVermelhos():
    return ("T", "P", "T", "C", "P", "T")

def tuboDados(tubo):
    for i in range(6):
        tubo.append(pegarDadosVerde())
    for amarelo in range(4):
        tubo.append(pegarDadosAmarelo())
    for vermlho in range(3):
        tubo.append(pegarDadosVermelhos()) 
    return tubo

def pegarDadosTubo(tubo):
    if (len(tubo) != 0):
        numDados = len(tubo) -1
        index = random.randint(0,numDados)
        dado = tubo[index]
        tubo.pop(index)
        return dado,tubo
    else:
        print("Tubo vazio")
        return -1,tubo

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

def mostrarDadoTubo(tubo):
    listDado = []
    for i in range(len(tubo)):
        if tubo[i] == ("C", "P", "C", "T", "P", "C"):
            listDado.append("Verde") 
        elif tubo[i] == ("T", "P", "C", "T", "P", "C"):
            listDado.append("Amarelo")
        else :
            listDado.append("Vermelho")
    return print(listDado)

def verificarScore(primeiro,segundo,terceiro):
    tiro = 0
    cerebro = 0
    passos = 0
    if primeiro == 'C':
        cerebro = cerebro + 1
    elif primeiro == 'T':
        tiro = tiro + 1
    else:
        passos = passos + 1
    if segundo == 'C':
        cerebro = cerebro + 1
    elif segundo == 'T':
        tiro = tiro + 1
    else:
        passos = passos + 1
    if terceiro == 'C':
        cerebro = cerebro + 1
    elif terceiro == 'T':
        tiro = tiro + 1
    else:
        passos = passos + 1
    return passos, cerebro, tiro

tubo = []
tubo = tuboDados(tubo)
listJogadores = []
jogo = True

numJogadores = int(input('Quantos zumbis na mesa? '))
if numJogadores < 2:
    print('é necessario 2 zumbis no minimo!! \n')
else:
    for i in range(numJogadores):
        nome = input('Informe seu nome morto-vivo ' + str(i) + ' ? ')
        cerebro = 0
        passos = 0
        tiro = 0
        jogador = [index,nome,cerebro,tiro]
        listJogadores.append(jogador)

print('Se preparem a invasão está começando... \n')

while(jogo):
    for i in  range(len(listJogadores)):
        codigo = jogador[0]
        nome = jogador[1]
        
        print("Turno de " + jogador[1] +' começou, role os dados \n')
        mostrarDadoTubo(tubo)
        turno = True
        blocoDado1 = True
        blocoDado2 = True
        blocoDado3 = True
        dado1 = True
        dado2 = True
        dado3 = True

        while(turno):
            continuarJogo = input('Você deseja continuar jogando os dados? (s = Sim / n = Não) \n')
            if continuarJogo == 's':
                continue
            else:
                turn = False
                jogar = False
                exit
            print('Role os dados \n')
            if blocoDado1:
                dado1,tubo = pegarDadosTubo(tubo)
            mostrarDadoTubo(dado1)
            
            if blocoDado2:
                dado2,tubo = pegarDadosTubo(tubo)
            mostrarDadoTubo(dado2)
            
            if blocoDado3:
                dado3,tubo = pegarDadosTubo(tubo)
            mostrarDadoTubo(dado3)

            print("Dados do Tubo: ")
            mostrarDadoTubo(tubo)

            um = ''
            dois = ''
            tres = ''

            if dado1 != -1:
                um  = faceDado(dado1)
            if dado2 != -1:
                dois  = faceDado(dado2)
            if dado3 != -1:
                tres  = faceDado(dado3)

        blocoDado1,blocoDado2,blocoDado3 = True

        cerebro,tiro,passos = verificarScore(um,dois,tres)

        if passos > 0 :
            if um  == 'P':
                blocoDado1 = False
            if dois == 'P':
                blocoDado2 = False
            if tres == "P":
                blocoDado3 = False
        
        listJogadores[codigo][2] = jogador[2] + cerebro
        listJogadores[codigo][3] =jogador[3]  + tiro

        print("Morto-vivo: " + listJogadores[codigo][1])
        print("Cerebro: " + str(listJogadores[codigo][2]))
        print("Tiro: " + str(listJogadores[codigo][3]))

        print(str(listJogadores[jogador[0][3]]))

        if listJogadores[jogador[0][3]] > 2:
            print('Você morreu!!\n')
            listJogadores[jogador[0][2]] = 0
            listJogadores[jogador[0][3]] = 0
            tuboRetorna = []
            tubo = tuboDados[tuboRetorna]
            mostrarDadoTubo(tubo)

            turno = False
        
        if listJogadores[jogador[0][2]] > 12:
            print('Parabens, Você Venceu !!!')
            jogar = False
            turno = False

        if turno:
            continuar = input('Deseja Continuar? (s = sim | n = não)')
            if continuar == 's':
                continue
            else:
                listJogadores[jogador[0][3]] = 0
                tuboRetorna = []
                tubo = tuboDados(tuboRetorna)
                mostrarDadoTubo(tubo)
                turno = False












