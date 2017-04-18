import colorama
from colorama import Fore, Back, Style, init
colorama.init()
init(autoreset=True)

def passear_ou_dormir():
    #pergunta_inicial = input("Você quer passear ou dormir?:")
    f = True
    while f:
        pergunta_inicial = input("Você quer passear ou dormir?:")
        if pergunta_inicial == "dormir":
            print(Fore.BLUE + "Ate a proxima!")
            g = False
            f = False
            break
        elif pergunta_inicial == "passear":
            print(Fore.RED+"Passeando...")
            print(Fore.RED+"Inspermon encontrado!\n")
            batalha(dados)
            passear_ou_dormir(pergunta_inicial)
        else:
            print(Back.MAGENTA+"Não existe esta função!")
            return pergunta_inicial
def batalha(dados):
      	n=0
      	list_0 = []
      	list_0.append(Aparecimento_de_Mons(dados))
      	#print(list_0[0]) #No Error
      	while n < 20:
      		if list_0[0] == dados[n]["nome"]:
      			dados_oponente = dados[n]
      		n=n+1
      	print(dados_oponente["nome"]) # No Error
      	f = True
      	while f:
      		if list_player[0]["vida"]>0 and dados_oponente["vida"]>0:
      			dados_oponente["vida"] = dados_oponente["vida"] - (list_player[0]["poder"] - dados_oponente["defesa"])
      		elif dados_oponente["vida"] <= 0:
      			list_player[0]["XP"] = list_player[0]["XP"] + 10
      			print('Vitoria! o Inspermon {0} foi derrotado com sucesso! \nA experiência de seu Inspermon é agora de {1}'.format(dados_oponente["nome"],list_player[0]["XP"]))
      			d = input("Voce deseja adiciona-lo ao seu time?(Sim ou Nao): ")
      			if d == "Sim":
      				list_player.append(dados_oponente)
      				print("Inspermon adicionado com sucesso!")
      				print("Inspermons membros de seu time: {0}".format(list_player))
      				break
      			if d == "Nao":
      				print("O Inspermon {0} olha para você com uma cara de assustado e corre en direçao ao horizonte... ".format(dados_oponente["nome"]))
      				break
      			else:
      				print("Por favor Tente novamente (utilize maiusculas!)")
      				continue
      		if list_player[0]["vida"]>0 and dados_oponente["vida"]>0:
      			list_player[0]["vida"]= list_player[0]["vida"] - (dados_oponente["poder"] - dados_oponente["defesa"])
      			#print(list_player[0]["vida"])
      		elif list_player[0]["vida"] <=0:
      			print("Você corre em desespero, nervoso e assustado, com seu inspermon em seu colo, enquanto ele libera seu ultimo folego de vida...")
      			novo_futuro = input('VOCÊ MORREU!!!... Digite Sim para Renascer:')
      			if novo_futuro == "Sim":
      				print("Voce Correu para o hospital salvando seu Inspermon...")
      				break
      			else:
      				print("Nao reconheço este comando, porfavor tente novamente...: ")

#Programa Principal

#g = True
#while g:
#pergunta_inicial = input("Você quer passear ou dormir?:")
passear_ou_dormir()
