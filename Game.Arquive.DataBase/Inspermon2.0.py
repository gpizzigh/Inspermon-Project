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
			lvl_up(list_player) 
		elif pergunta_inicial == "Insperdex":
			print(Insperdex)
			print(funt_Insperdex(Insperdex))
			print(len(Insperdex))
		else:
			print(Back.MAGENTA+"Não existe esta função!")
			

def inspermon_inicial(dados):  #OK
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

def Aparecimento_de_Mons(dados):  #OK
	lista_Mons = []
	for e in dados:
		for x in e.keys():
			if x == "nome":
				lista_Mons.append(e[x])
	key = random.randint(0,len(lista_Mons)-1)
	#print(lista_Mons[key])
	return lista_Mons[key]
#print (Aparecimento_de_Mons(dados))


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
	
	f = True
	while f:
		fugir_ou_lutar = input("Você deseja fugir ou lutar?:")
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
			
			for g in range(len(list_player)):
				escolhido = int(input("Digite o numero de seu Inspermon escolhido: "))
				if escolhido == g:
					print("Inspermon escolhido: {0} ".format(list_player[g]["nome"]))
					vida_jogador = list_player[g]["vida"]
					print(list_player[g]["vida"])
					


					while list_player[g]["vida"]>0 and dados_oponente["vida"]>0:
						z = random.randint(0,10)
						if list_player[g]["poder"] >= dados_oponente["defesa"]:
							if z == 9:
								dados_oponente["vida"] = dados_oponente["vida"] - (list_player[g]["poder"]*100 - dados_oponente["defesa"])
								print("Ataque critico feito pelo Inspermon do jogador") 
							else:
								dados_oponente["vida"] = dados_oponente["vida"] - (list_player[g]["poder"] - dados_oponente["defesa"])

						elif list_player[g]["poder"] <= dados_oponente["defesa"]:
							if z == 9:
								dados_oponente["vida"] = dados_oponente["vida"] - (list_player[g]["poder"]*100 - dados_oponente["defesa"])
								print("Ataque critico do Inspermon do jogador") 
							else:
								dados_oponente["vida"] = dados_oponente["vida"]


						if dados_oponente["vida"] <= 0:
							list_player[g]["XP"] = list_player[g]["XP"] + 10
							list_player[g]["vida"] = vida_jogador  
							print(Fore.GREEN+Style.BRIGHT+'Vitoria! o Inspermon {0} foi derrotado com sucesso!'.format(dados_oponente["nome"]))
							print('A experiência de seu Inspermon é agora de {0}\nA vida do seu Inspermon agora é de {1}'.format(list_player[g]["XP"],list_player[g]["vida"]))

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
							if z == 5:
								list_player[g]["vida"] = list_player[g]["vida"] - (dados_oponente["poder"]*100 - list_player[g]["defesa"])
								print("Ataque critico do oponente")
							else:
								list_player[g]["vida"] = list_player[g]["vida"] - (dados_oponente["poder"] - list_player[g]["defesa"])

						elif dados_oponente["poder"] <= list_player[g]["defesa"]:
							if z == 5:
								list_player[g]["vida"] = list_player[g]["vida"] - (dados_oponente["poder"]*100 - list_player[g]["defesa"])
								print("Ataque critico do oponente")
							else:
								list_player[g]["vida"] = list_player[g]["vida"]

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
						
				else:
					print("Digite novamente!")  # Dando erro estranho
					continue

		else:
		    print(Fore.RED + "Porfavor digite novamente")  # Arrumei o erro !
		    continue


def lvl_up(list_player):  # OK
	for x in range(len(list_player)):
		if list_player[x]["XP"] == 50:
			list_player[x]["XP"]  = 55
			list_player[x]["poder"] = list_player[x]["poder"] * 1.5
			list_player[x]["vida"] = list_player[x]["vida"] * 1.7
			list_player[x]["defesa"] = list_player[x]["defesa"] * 1.5
			print("O seu Inspermon,{0} evoluiu.\nInspermon status:\npoder:{1}\ndefesa:{2}\nvida:{3}".format(list_player[x]["nome"],list_player[x]["poder"],list_player[x]["defesa"],list_player[x]["vida"]))
			return list_player[x]
		elif list_player[x]["XP"] == 155:
			list_player[x]["XP"] == 160
			list_player[x]["poder"] = list_player[x]["poder"] *1.6
			list_player[x]["vida"] = list_player[x]["vida"] * 1.7
			list_player[x]["defesa"] = list_player[x]["defesa"] * 1.6
			print("O Inspermon,{0}, evoluiu.\nInspermon status:\npoder:{1}\ndefesa:{2}\nvida:{3}".format(list_player[x]["nome"],list_player[x]["poder"],list_player[x]["defesa"],list_player[x]["vida"]))
			return list_player[x]


def funt_Insperdex(Insperdex):  # Dando erro
	
	for y in range(len(Insperdex)):
		if Insperdex[y] not in Insper2:
			Insper2.append(Insperdex[y])
			return Insper2

def escolha(dados):  
	print("Escolha um dos seguintes Inspermons de seu time para Batalhar:")
	x = 0
	while x < len(list_player):
		print("{0} - {1}".format(x,list_player[x]["nome"]))
		x += 1
	for g in range(len(list_player)):
		escolhido = int(input("Digite o numero de seu Inspermon escolhido: "))
		if escolhido == g:
			print("Inspermon escolhido: {0} ".format(list_player[g]["nome"]))
			vida_jogador = list_player[g]["vida"]
		else:
			print("Digite novamente")
			continue

# Programa Principal----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------- Texto -------------------------------------------------------------

Insper2 = []


with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)

with open('texto de introduçao.txt','r',encoding='Latin-1') as texto:
	for linha in texto.readlines():
		print(Fore.GREEN+Style.BRIGHT+linha)


print("------"*20)
#-------------- Escolha do Inspermon inicial ---------------------------------------
inspermon_inicial(dados)
Insperdex.append(dados[6])
Insperdex.append(dados[7])
Insperdex.append(dados[11])
print("Inspermons membros o de seu time: {0}".format(list_player))
print("------"*20)
# ------------- Funçao Passear ou dormir -------------------------------------------



passear_ou_dormir()
