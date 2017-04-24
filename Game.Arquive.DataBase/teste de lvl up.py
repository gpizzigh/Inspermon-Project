
import json

with open("Data_Inspermons.json") as arquivo:
	dados = json.load(arquivo)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def lvl_up(dados):  # Dando erro. Lista out of range
    x = 0
    while x <= len(list_player): # certo
        if list_player[x]["XP"] == 50:
            if list_player[x]["nome"] =="Gladium":
                print("Seu Inspermou esta evoluindo!")
                print("..."*5)
                print("Parabens! Seu inspermom evoluiu de Gladium para Warirum!")
                list_player[x] = dados[19]
#------------------- Utilizar este formato de codigo para repetiçao! -------------
            if list_player[x]["nome"] == "Oddibia":
                print("Seu Inspermou esta evoluindo!")
                print("..."*5)
                print("Parabens! Seu inspermom evoluiu de Oddibia para Orgatos!")
                list_player[x] = dados[21]
#----------------------------------------------------------------------------------
            elif list_player[x]["nome"] == "Moltander":
                print("Seu Inspermou esta evoluindo!")
                print("..."*5)
                print("Parabens! Seu inspermom evoluiu de Moltander para Termeon!")
                list_player[x] = dados[23]
        x += 1







#--------------------------------------------------------------------------------------------------------------------------------------------------------------
list_player = [{"nome":"Oddibia","poder":35,"vida":35,"defesa":25,"XP":0},{"nome":"Silveramel","poder":37,"vida":25,"defesa":15,"XP":0}]
f = True
while f:
    adicionador_de_xp = input("Aperte 'z' para adicionar 10 de Xp: ")
    if adicionador_de_xp == "z":
        New = list_player[0]["XP"] + 10
        list_player[0]["XP"] = New
        print(list_player[0]["nome"])
        print(list_player[0]["XP"])
    else:
        lvl_up(dados)
        f = False
print(lvl_up(dados))
