def repetir ():
	x= True
	while x==True:
		edad = int(input("ingrese edad"))
		print(edad)
		if edad>=18:
			x=False
		else:
			print("es menor de edad")
repetir() 
