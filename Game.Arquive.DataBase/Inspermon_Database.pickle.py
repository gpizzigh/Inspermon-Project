import pickle
dados = {
"Liumon":{"poder":100,"vida":200,"defesa":150},
"Pizzimon":{"poder":150,"vida":200,"defesa":100},
"Ninjamon":{"poder":50,"vida":60,"defesa":80},
"Chinesmon":{"poder":70,"vida":50,"defesa":90},
"Peruibemon":{"poder":20,"vida":40,"defesa":30},
"Italimon":{"poder":10,"vida":60,"defesa":40}
}

with open ("Inspermon_Database.pickle","wb") as arquivo:
	pickle.dump(dados, arquivo)
