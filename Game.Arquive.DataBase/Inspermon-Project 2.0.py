import pickle
with open ("Inspermon_Database.pickle","rb") as arquivo:
	Base_Dados = pickle.load(arquivo)
	print(Base_Dados["Pizzimon"])