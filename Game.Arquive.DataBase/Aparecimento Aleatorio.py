import random 
import pickle
with open ("Inspermon_Database(Gamma).pickle","rb") as arquivo:
	Base_Dados = pickle.load(arquivo)
def Aparecimento_de_Mons(Base_Dados):
	lista_Mons=[]
	for e in Base_Dados:
		for x in e.keys():
			if x == "nome":
				lista_Mons.append(e[x])
	key = random.randint(0,len(lista_Mons)-1)
	#print(lista_Mons[key])
	return lista_Mons[key]
print(Aparecimento_de_Mons(Base_Dados))