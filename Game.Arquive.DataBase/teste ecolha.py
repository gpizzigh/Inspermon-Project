
list_player = [{"nome":"Dragoss","poder":15,"vida":20,"defesa":15,"XP":0},{"nome":"Odeaxus","poder":140,"vida":140,"defesa":60,"XP":150}]



def escolha():
    print("Escolha um dos segunites Inspermons de seu time para Batalhar: ")
    x = 0
    while x < len(list_player):
        print("{0} - {1}".format(x,list_player[x]["nome"]))
        x += 1
    escolhido = int(input("Digite o numero de seu Inspermon escolhido: "))
    for g in range(len(list_player)):
        if escolhido == g:
            print("Inspermon escolhido: {0} ".format(list_player[g]["nome"]))

    '''if escolhido == 1:
        print("Inspermon escolhido: {0} ".format(list_player[1]["nome"]))
    if escolhido == 2:
        print("Inspermon escolhido: {0} ".format(list_player[2]["nome"]))
    if escolhido == 3:
        print("Inspermon escolhido: {0} ".format(list_player[3]["nome"]))
    if escolhido == 4:
        print("Inspermon escolhido: {0} ".format(list_player[4]["nome"]))
    if escolhido == 5:
        print("Inspermon escolhido: {0} ".format(list_player[5]["nome"]))'''


escolha()
