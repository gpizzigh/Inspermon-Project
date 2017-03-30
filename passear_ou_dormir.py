
while True:
 pergunta_inicial = input("Você quer passear ou dormir?:")
 if pergunta_inicial == "dormir":
   print("Até mais tarde")
   break
 elif pergunta_inicial == "passear":
   print("Vamos passear ")
   break
 else:
   print("Não existe essa função ")
   continue