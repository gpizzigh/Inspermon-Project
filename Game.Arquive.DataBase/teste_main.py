
import random
import json
import colorama
from colorama import Fore, Back, Style, init
colorama.init()
init(autoreset=True)
#Variaveis--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
list_player = []
#Funções----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def passear_ou_dormir(pergunta_inicial):
	while True:
		pergunta_inicial = input("Você quer passear ou dormir?:")
		if pergunta_inicial == "dormir":
			print(Fore.BLUE + "Ate a proxima!")
			return pergunta_inicial
		elif pergunta_inicial == "passear":
			print(Fore.RED+"Passeando...")
			print(Fore.RED+"Inspermon encontrado!\n")
			batalha(dados)
			return pergunta_inicial
		else:
			print(Back.MAGENTA+"Não existe esta função!")

def inspermon_inicial(dados):
	#list_player = []
	while True:
		#print("Escolha um dos seguintes Inspermons iniciais:")
		print("Primeira Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}\nXP:{4}".format(dados[6]['nome'],dados[6]['poder'],dados[6]['vida'],dados[6]['defesa'],dados[6]['XP']))
		print("Segunda Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}\nXP:{4}".format(dados[7]['nome'],dados[7]['poder'],dados[7]['vida'],dados[7]['defesa'],dados[7]['XP']))
		print("Terceira Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}\nXP:{4}".format(dados[11]['nome'],dados[11]['poder'],dados[11]['vida'],dados[11]['defesa'],dados[11]['XP']))
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
			print("Você escolheu o Inspermon: {0}".format(dados[11]['nome']) )
			list_player.append(dados[11])
			return (Fore.WHITE + "Inspermon Adicionado!")
		else:
			print(Style.DIM + "Erro! Escolha novamente(Porfavor copie exatamente como mostrado!)")
			continue
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
# Programa Principal----------------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)
#with open('texto de introduçao.txt','r',encoding='utf-8') as texto:
#	for linha in texto.readlines():
#		print(Fore.GREEN+linha)
print(inspermon_inicial(dados))
#list_player.append(inspermon_inicial(dados))
print("Inspermons membros o de seu time: {0}".format(list_player))

pergunta_inicial = passear_ou_dormir("")

#<<<<<<< HEAD
if pergunta_inicial == "passear":
	print(Fore.RED+"Passeando...")
	print(Fore.RED+"Inspermon encontrado!\n")
	f = True
	while f:
		resposta = input("Você deseja fugir ou lutar? ")
		if resposta == "fugir":
			print("Voce conseguiu fugir em segurança!")
			passear_ou_dormir(pergunta_inicial)
		elif resposta == "lutar":
			print("Prepara para a batalha!")
			batalha(dados)
			f = False
		else:
			print("Comando irreconhecivel, porfavor tentar novamente")
#=======
'''if pergunta_inicial == "passear":
#<<<<<<< Updated upstream
	print(Fore.RED+"Passeando...")
	print(Fore.RED+"Inspermon encontrado!\n {0}".format(Aparecimento_de_Mons(dados)))
else:
	print(Fore.BLUE + "Ate a proxima!")
#=======
	print("Vamos passear")
	print(inspermon_inicial(dados))

	print(Aparecimento_de_Mons(dados))'''
#else:
	#print("Até a proxima")
