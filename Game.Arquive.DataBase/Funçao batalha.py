import json
import random
with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)

list_player = [{"nome":"Oddibia","poder":95,"vida":35,"defesa":55}]
def Aparecimento_de_Mons(dados):
	lista_Mons = []
	for e in dados:
		for x in e.keys():
			if x == "nome":
				lista_Mons.append(e[x])
	key = random.randint(0,len(lista_Mons)-1)
	return lista_Mons[key]

Aparecimento_de_Mons(dados)



def batalha(dados):
	n=0
	list_0 = []
	list_0.append(Aparecimento_de_Mons(dados))
	print(list_0[0]) #No Error
	while n < 12:
		if list_0[0] == dados[n]["nome"]:
			dados_oponente = dados[n]
		n=n+1
	print(dados_oponente) # No Error
	list_player = [{"nome":"Oddibia","poder":95,"vida":35,"defesa":55}]




	f = True
	while f:
		if list_player[0]["vida"]>0 and dados_oponente["vida"]>0:
			dados_oponente["vida"] = dados_oponente["vida"] - (list_player[0]["poder"] - dados_oponente["defesa"])
		elif dados_oponente["vida"] <= 0:
			print('Vitoria! o Inspermon {0} foi derrotado com sucesso!'.format(dados_oponente["nome"]))
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
			novo_futuro = input('VOCÊ MORREU!!!... Digite Sim para Renacer:')
			if novo_futuro == "Sim":
				print("Voce Correu para o hospital salvando seu Inspermon...")
				break
			else:
				print("Nao reconheço este comando, porfavor tente novamente...: ")
				continue










batalha(dados)

#print(list_0[0])
#print(batalha(dados))
