import random
import json
import colorama
from colorama import Fore, Back, Style, init
colorama.init()
init(autoreset=True)
#Variaveis--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
list_player = []
Insperdex = []
#Funções----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def passear_ou_dormir():
    #pergunta_inicial = input("Você quer passear ou dormir?:")
	f = True
	while f:
		pergunta_inicial = input("Você deseja passear, dormir ou acessar o Insperdex?: ")
		if pergunta_inicial == "dormir":
			print(Fore.BLUE + "Até a proxima!")
			f = False
			break
		elif pergunta_inicial == "passear":
			print(Fore.BLACK + "------"*20)
			print(Fore.RED+"Passeando...")
			print(Fore.RED+"Inspermon encontrado!\n")
			print(Fore.BLACK + "------"*20)
			batalha_2(dados)
			#lvl_up(dados)
		elif pergunta_inicial == "Insperdex":
			print(Insperdex)
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

'''def batalha(dados):
	n=0
	list_0 = []
	list_0.append(Aparecimento_de_Mons(dados))
	#print(list_0[g]) #No Error
	while n < 46:
		if list_0[0] == dados[n]["nome"]:
			dados_oponente = dados[n]
		n=n+1
	Insperdex.append(dados_oponente["nome"])
	print(Fore.YELLOW + dados_oponente["nome"]) # No Error
	vida_oponente = dados_oponente["vida"]
	vida_jogador = list_player[g]["vida"]  # Dando problema . Problema apos perder algum Hp sem Morrer e apos isso ele morrre o hp Inspermon nao e restaurado 100%
	fugir_ou_lutar = input("Você quer fugir ou lutar?:")
	f = True
	while f:
		if fugir_ou_lutar == "fugir":
			print("Você fugiu da batalha")
			f = False
		elif fugir_ou_lutar == "lutar":
			print(Fore.RED + "Prepare-se para a batalha!")
#--------------------------------------Teste---------------------------------------------------------------
			print("Escolha um dos seguintes Inspermons de seu time para Batalhar: ")
			x = 0
			while x < len(list_player):
				print("{0} - {1}".format(x,list_player[x]["nome"]))
				x += 1
			escolhido = int(input("Digite o numero de seu Inspermon escolhido: "))
			for g in range(len(list_player)):
				if escolhido == g:
					print("Inspermon escolhido: {0} ".format(list_player[g]["nome"]))
					vida_jogador = list_player[g]["vida"]
					print(list_player[g]["vida"])
#-----------------------------------------Teste------------------------------------------------------------
			batalha_2(dados)'''
def batalha_2(dados):
#----------------------------------------Teste-----------------------------------------
	n=0
	list_0 = []
	list_0.append(Aparecimento_de_Mons(dados))
	#print(list_0[g]) #No Error
	while n < 46:
		if list_0[0] == dados[n]["nome"]:
			dados_oponente = dados[n]
		n=n+1
	Insperdex.append(dados_oponente["nome"])
	print(Fore.YELLOW + dados_oponente["nome"]) # No Error
	vida_oponente = dados_oponente["vida"]
	'''vida_jogador = list_player[g]["vida"]'''  # Dando problema . Problema apos perder algum Hp sem Morrer e apos isso ele morrre o hp Inspermon nao e restaurado 100%
	fugir_ou_lutar = input("Você deseja fugir ou lutar?:")
	f = True
	while f:
		if fugir_ou_lutar == "fugir":
			print("Você fugiu da batalha")
			f = False
		elif fugir_ou_lutar == "lutar":
			print(Fore.RED + "Prepare-se para a batalha!")
#----------------------------------------Teste----------------------------------------
			print("Escolha um dos seguintes Inspermons de seu time para Batalhar: ")
			x = 0
			while x < len(list_player):
				print("{0} - {1}".format(x,list_player[x]["nome"]))
				x += 1
			escolhido = int(input("Digite o numero de seu Inspermon escolhido: "))
			for g in range(len(list_player)):
				if escolhido == g:
					print("Inspermon escolhido: {0} ".format(list_player[g]["nome"]))
					vida_jogador = list_player[g]["vida"]
					#print(list_player[g]["vida"]) # Sem Erro!
#----------------------------------------Teste----------------------------------------
					while list_player[g]["vida"]>0 and dados_oponente["vida"]>0:
						if list_player[g]["poder"] >= dados_oponente["defesa"]:
							dados_oponente["vida"] = dados_oponente["vida"] - (list_player[g]["poder"] - dados_oponente["defesa"])
						if dados_oponente["vida"] <= 0:
							list_player[g]["XP"] = list_player[g]["XP"] + 10
							list_player[g]["vida"] = vida_jogador  # Coloquei somente para tentar resolver problema do HP da linha 85.
							print(Fore.GREEN+Style.BRIGHT+'Vitoria! o Inspermon {0} foi derrotado com sucesso!'.format(dados_oponente["nome"]))
							print('A experiência de seu Inspermon é agora de {0}\nA vida do seu Inspermon agora é de {1}'.format(list_player[g]["XP"],list_player[g]["vida"]))
							#lvl_up(dados)
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
									print("Por favor Tente novamente (UTILIZE MAIUSCULAS!)")
						if dados_oponente["poder"] > list_player[g]["defesa"]:
							list_player[g]["vida"] = list_player[g]["vida"] - (dados_oponente["poder"] - list_player[g]["defesa"])
						if list_player[g]["vida"] <= 0:
							print(Fore.RED + Style.BRIGHT +"Você corre em desespero, nervoso e assustado, com seu inspermon em seu colo, enquanto ele libera seu ultimo folego de vida...")
							while True:
								novo_futuro = input('VOCÊ MORREU!!!... Digite Sim para Renascer:')
								if novo_futuro == "Sim":
									list_player[g]["vida"] = vida_jogador
									print("Voce Correu para o hospital salvando seu Inspermon...")
									print("A vida do Inspermon {0} foi restaurada.\nVida Inspermon:{1}".format(list_player[g]["nome"],list_player[g]["vida"]))
									print(list_player)
									return
								else:
									print("Nao reconheço este comando, porfavor tente novamente...:")
								if list_player[g]["poder"] >= dados_oponente["defesa"]:
									dados_oponente["vida"] = dados_oponente["vida"]
								else:
									dados_oponente["poder"] >= list_player[g]["defesa"]
		else:
			print(Fore.RED + "Porfavor digite novamente")  # Ainda esta dand erro aqui! ele nao esta retornando para o inicio do while porfavor resolver!
			break



def lvl_up(dados):  # Dando erro. Lista out of range
    x = 0
    while x <= len(list_player): # certo
        if list_player[x]["XP"] == 50:
            if list_player[x]["nome"] =="Gladium":
                print("Seu Inspermou esta evoluindo!")
                print("..."*5)
                print("Parabens! Seu inspermom evoluiu de Gladium para Warirum!")
                list_player[x] = dados[19]
 #------------------- Utilizar este formato de codigo para repetiçao! -------------
            if list_player[x]["nome"] == "Oddibia":
                print("Seu Inspermou esta evoluindo!")
                print("..."*5)
                print("Parabens! Seu inspermom evoluiu de Oddibia para Orgatos!")
                list_player[x] = dados[21]
 #----------------------------------------------------------------------------------
            elif list_player[x]["nome"] == "Moltander":
                print("Seu Inspermou esta evoluindo!")
                print("..."*5)
                print("Parabens! Seu inspermom evoluiu de Moltander para Termeon!")
                list_player[x] = dados[23]
        x += 1
def escolha(dados):
	print("Escolha um dos seguintes Inspermons de seu time para Batalhar: ")
	x = 0
	while x < len(list_player):
		print("{0} - {1}".format(x,list_player[x]["nome"]))
		x += 1
	escolhido = int(input("Digite o numero de seu Inspermon escolhido: "))
	for g in range(len(list_player)):
		if escolhido == g:
			print("Inspermon escolhido: {0} ".format(list_player[g]["nome"]))
			vida_jogador = list_player[g]["vida"]


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
Insperdex.append(dados[6]['nome'])
Insperdex.append(dados[7]['nome'])
Insperdex.append(dados[11]['nome'])
print("Inspermons membros o de seu time: {0}".format(list_player))
print("------"*20)
# ------------- Funçao Passear ou dormir -------------------------------------------



passear_ou_dormir()
