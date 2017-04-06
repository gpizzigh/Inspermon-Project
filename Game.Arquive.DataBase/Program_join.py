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
		if pergunta_inicial == "dormir" or pergunta_inicial == "passear":
			return pergunta_inicial
		else:
			print(Back.MAGENTA+"Não existe essa função!")

def inspermon_inicial(dados):
	#list_player = []
	while True:
		#print("Escolha um dos seguintes Inspermons iniciais:")
		print("Primeira Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}".format(dados[6]['nome'],dados[6]['poder'],dados[6]['vida'],dados[6]['defesa']))
		print("Segunda Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}".format(dados[7]['nome'],dados[7]['poder'],dados[7]['vida'],dados[7]['defesa']))
		print("Terceira Opção:\n{0}\nPoder:{1}\nVida:{2}\nDefesa:{3}".format(dados[11]['nome'],dados[11]['poder'],dados[11]['vida'],dados[11]['defesa']))
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

# Programa Principal----------------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)
with open('texto de introduçao.txt','r') as texto:
	for linha in texto.readlines():
		print(Fore.GREEN+linha)
print(inspermon_inicial(dados))
#list_player.append(inspermon_inicial(dados))
print("Inspermons membros o de seu time: {0}".format(list_player))

pergunta_inicial = passear_ou_dormir("")

if pergunta_inicial == "passear":
	print(Fore.RED+"Passeando...")
	print(Fore.RED+"Inspermon encontrado!\n {0}".format(Aparecimento_de_Mons(dados)))
else:
	print(Fore.BLUE + "Ate a proxima!")