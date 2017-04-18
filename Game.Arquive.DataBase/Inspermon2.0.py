import random
import json
import colorama
from colorama import Fore, Back, Style, init
colorama.init()
init(autoreset=True)
#Variaveis--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
list_player = []
#Funções----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def passear_ou_dormir():
    #pergunta_inicial = input("Você quer passear ou dormir?:")
	f = True
	while f:
		pergunta_inicial = input("Você quer passear ou dormir?:")
		if pergunta_inicial == "dormir":
			print(Fore.BLUE + "Até a proxima!")
			f = False
			break
		elif pergunta_inicial == "passear":
			print(Fore.BLACK + "------"*20)
			print(Fore.RED+"Passeando...")
			print(Fore.RED+"Inspermon encontrado!\n")
			print(Fore.BLACK + "------"*20)
			batalha(dados)
		else:
			print(Back.MAGENTA+"Não existe esta função!")
			#return pergunta_inicial # !!Funçao OK!!

def inspermon_inicial(dados):
	#list_player = []
	while True:
		print("Escolha um dos seguintes Inspermons iniciais:")
		print(Fore.BLUE + "Primeira Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}".format(dados[6]['nome'],dados[6]['poder'],dados[6]['vida'],dados[6]['defesa']))
		print(Fore.RED + "Segunda Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}".format(dados[7]['nome'],dados[7]['poder'],dados[7]['vida'],dados[7]['defesa']))
		print(Fore.GREEN + "Terceira Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}".format(dados[11]['nome'],dados[11]['poder'],dados[11]['vida'],dados[11]['defesa']))
		escolha = input("Escolha entre os Inspermons {0}, {1} ou {2}:".format(dados[6]["nome"],dados[7]["nome"],dados[11]["nome"]))
		if escolha == dados[6]['nome']:
			colection = dados[6]
			list_player.append(dados[6])
			print("Você escolheu o Inspermon: {0}".format(dados[6]['nome'])) # so mostra o nome do Insper
			return (Fore.WHITE + "Inspermon Adicionado!")
			break
		elif escolha == dados[7]['nome']:
			colection = dados[7]
			print("Você escolheu o Inspermon: {0}".format(dados[7]['nome']))
			list_player.append(dados[7])
			return (Fore.WHITE + "Inspermon Adicionado!")
			break
		elif escolha == dados[11]['nome']:
			colection = dados[11]
			print("Você escolheu o Inspermon: {0}".format(dados[11]['nome']))
			list_player.append(dados[11])
			return (Fore.WHITE + "Inspermon Adicionado!")
			break
		else:
			print(Style.DIM + Fore.RED +"Erro! Escolha novamente(Porfavor copie exatamente como mostrado!)")
			continue #funçao no estado OK
def Aparecimento_de_Mons(dados):
	lista_Mons = []
	for e in dados:
		for x in e.keys():
			if x == "nome":
				lista_Mons.append(e[x])
	key = random.randint(0,len(lista_Mons)-1)
	#print(lista_Mons[key])
	return lista_Mons[key]
#print (Aparecimento_de_Mons(dados))



def batalha(dados):
	n=0
	list_0 = []
	list_0.append(Aparecimento_de_Mons(dados))
	#print(list_0[0]) #No Error
	while n < 20:
		if list_0[0] == dados[n]["nome"]:
			dados_oponente = dados[n]
		n=n+1
	print(Fore.YELLOW + dados_oponente["nome"]) # No Error
	vida_oponente = dados_oponente["vida"]
	vida_jogador = list_player[0]["vida"]
	while list_player[0]["vida"]>0 and dados_oponente["vida"]>0:
		if list_player[0]["poder"] > dados_oponente["defesa"]:
			dados_oponente["vida"] = dados_oponente["vida"] - (list_player[0]["poder"] - dados_oponente["defesa"])
		if dados_oponente["vida"] <= 0:
			list_player[0]["XP"] = list_player[0]["XP"] + 10
			print(Fore.GREEN+Style.BRIGHT+'Vitoria! o Inspermon {0} foi derrotado com sucesso!'.format(dados_oponente["nome"]))
			print('A experiência de seu Inspermon é agora de {0}'.format(list_player[0]["XP"]))

			while True:
				d = input("Voce deseja adiciona-lo ao seu time?(Sim ou Nao): ")
				if d == "Sim":
					dados_oponente["vida"]=vida_oponente
					list_player.append(dados_oponente)
					print("Inspermon adicionado com sucesso!")
					print("Inspermons membros de seu time: {0}".format(list_player))
					return
				elif d == "Nao":
					print("O Inspermon {0} olha para você com uma cara de assustado e corre en direçao ao horizonte... ".format(dados_oponente["nome"]))
					return
				else:
					print("Por favor Tente novamente (utilize maiusculas!)")
		elif dados_oponente["poder"] > list_player[0]["defesa"]:
			list_player[0]["vida"] = list_player[0]["vida"] - (dados_oponente["poder"] - list_player[0]["defesa"])
			if list_player[0]["vida"] <= 0:
				print(Fore.RED + Style.BRIGHT +"Você corre em desespero, nervoso e assustado, com seu inspermon em seu colo, enquanto ele libera seu ultimo folego de vida...")
				while True:
					novo_futuro = input('VOCÊ MORREU!!!... Digite Sim para Renascer:')
					if novo_futuro == "Sim":
						list_player[0]["vida"] = vida_jogador
						print("Voce Correu para o hospital salvando seu Inspermon...")
						return
					else:
						print("Nao reconheço este comando, porfavor tente novamente...: ")
		elif list_player[0]["poder"] >= dados_oponente["defesa"]:
			dados_oponente["vida"] = dados_oponente["vida"]

		else:
			dados_oponente["poder"] >= list_player[0]["defesa"]

# Programa Principal----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------- Texto -------------------------------------------------------------
with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)

with open('texto de introduçao.txt','r',encoding='Latin-1') as texto:
	for linha in texto.readlines():
		print(Fore.GREEN+Style.BRIGHT+linha)
print("------"*20)
#-------------- Escolha do Inspermon inicial ---------------------------------------
inspermon_inicial(dados)
print("Inspermons membros o de seu time: {0}".format(list_player))
print("------"*20)
# ------------- Funçao Passear ou dormir -------------------------------------------

passear_ou_dormir()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#deletar------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#pergunta_inicial = passear_ou_dormir("")



#print(inspermon_inicial(dados))
#list_player.append(inspermon_inicial(dados))

#=======
