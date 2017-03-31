import random 
import json


def passear_ou_dormir(pergunta_inicial):
	while True:
		pergunta_inicial = input("Você quer passear ou dormir?:")
		if pergunta_inicial == "dormir" or pergunta_inicial == "passear":
			return pergunta_inicial
		else:
			print("Não existe essa função")
			

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

# Programa Principal
with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)


pergunta_inicial = passear_ou_dormir("")

if pergunta_inicial == "passear":
	print("Vamos passear")
	print(Aparecimento_de_Mons(dados))
else:
	print("Ate a proxima")