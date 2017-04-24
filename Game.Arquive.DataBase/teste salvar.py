#Salvar dois dados -----> list_player and insperdex
import json


with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)

list_player = [{"nome":"Gladium","poder":35,"vida":35,"defesa":15,"XP":0},{"nome":"Dragoss","poder":15,"vida":20,"defesa":15,"XP":0}]
insperdex = [dados[6]["nome"],dados[11]["nome"]]

def Save_game():
    list_player_save = list_player
    insperdex_player = insperdex
    with open ('Savegame_player.json','wb') as fp:
        json.dump(list_player_save, fp, indent = 1)
    with open ('Savegame_insperdex.json','wb') as fp:
        json.dump(insperdex_player, fp, indent = 1)
        print("Jogo salvo com sucesso!")

Save_game()
