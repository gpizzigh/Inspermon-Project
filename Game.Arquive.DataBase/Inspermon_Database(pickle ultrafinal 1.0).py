import pickle
dados =[ 
{"nome": "Liumon","poder":100,"vida":200,"defesa":150},
{"nome": "Pizzimon","poder":150,"vida":200,"defesa":100},
{"nome": "Ninjamon","poder":50,"vida":60,"defesa":80},
{"nome": "Chinesmon","poder":70,"vida":50,"defesa":90},
{"nome": "Peruibemon","poder":20,"vida":40,"defesa":30},
{"nome":"Italimon","poder":10,"vida":60,"defesa":40},
{'Player': {"nome": "Boludosmon","poder":15,"vida":50,"defesa":50}
}
]


with open ("Inspermon_Database(Gamma).pickle","wb") as arquivo:
	pickle.dump(dados, arquivo)
