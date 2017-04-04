def inspermon_inicial(dados):
	while True:
		escolha = input("Escolha entre os inspermons Boludosmon , Turtwig ou Pixu:")
		if escolha == "Boludosmon":
			colection = dados[6] 
			return "Você escolheu o Inspermon:Boludosmon"  # so mostra o nome do Insper
			break
		elif escolha == "Turtwig":
			colection = dados[7]
			return "Você escolheu o Inspermon:Turtwig" 
			break
		elif escolha == "Pixu":
			colection = dados[8]
			return "Você escolheu o Inspermon:Pixu" 
			break
		else:
			print("Erro!Escolha novamente")
			continue

		 
	
	

