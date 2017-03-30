def passear_ou_dormir(pergunta_inicial):
	while True:
		pergunta_inicial = input("Você quer passear ou dormir?:")
		if pergunta_inicial == "dormir":
			return "Até mais tarde"
			break
		elif pergunta_inicial == "passear":
			return "Vamos passear "
			break
		else:
			print("Não existe essa função ")
			continue
			

pergunta_inicial = passear_ou_dormir("")
print(pergunta_inicial)
