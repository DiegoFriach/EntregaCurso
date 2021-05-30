numero1 = input()
operacao = input()
numero2 = input()
operacao2 = input()
numero3 = input()

if operacao == "+" and operacao2 == "+":
	resultado = int(numero1) + int(numero2) + int(numero3)
elif operacao == "-" and operacao2 == "-":
	resultado = int(numero1) - int(numero2) - int(numero3)
elif operacao == "*" and operacao2 == "*":
	resultado = int(numero1) * int(numero2) * int(numero3)
elif operacao == "//" and operacao2 == "//":
	if int(numero2) == 0 or int(numero3) == 0:
		print ("ERRO")
	if int(numero2) != 0 and int(numero3) != 0:
		resultado = int(numero1) // int(numero2) // int(numero3)
elif operacao == "+" and operacao2 == "-":
	resultado = int(numero1) + int(numero2) - int(numero3)
elif operacao == "-" and operacao2 == "+":
	resultado = int(numero1) - int(numero2) + int(numero3)
elif operacao == "*" and operacao2 == "+":
	resultado = int(numero1) * int(numero2) + int(numero3)
elif operacao == "+" and operacao2 == "*":
	resultado = int(numero1) + int(numero2) * int(numero3)
elif operacao == "//" and operacao2 == "+":
	if int(numero2) == 0:
		print ("ERRO")
	if int(numero2) != 0:
		resultado = int(numero1) // int(numero2) + int(numero3)
elif operacao == "+" and operacao2 == "//":
	if int(numero3) == 0:
		print ("ERRO")
	if int(numero3) != 0:
		resultado = int(numero1) + int(numero2) // int(numero3)
elif operacao == "-" and operacao2 == "*":
	resultado = int(numero1) - int(numero2) * int(numero3)
elif operacao == "*" and operacao2 == "-":
	resultado = int(numero1) * int(numero2) - int(numero3)
elif operacao == "-" and operacao2 == "//":
	if int(numero3) == 0:
		print ("ERRO")
	if int(numero3) != 0:
		resultado = int(numero1) - int(numero2) // int(numero3)
elif operacao == "//" and operacao2 == "-":
	if int(numero2) == 0:
		print ("ERRO")
	if int(numero2) != 0:
		resultado = int(numero1) // int(numero2) - int(numero3)
elif operacao == "*" and operacao2 == "//":
	if int(numero3) == 0:
		print ("ERRO")
	if int(numero3) != 0:
		resultado = int(numero1) * int(numero2) // int(numero3)
elif operacao == "//" and operacao2 == "*":
	if int(numero2) == 0:
		print ("ERRO")
	if int(numero2) != 0:
		resultado = int(numero1) // int(numero2) * int(numero3)
		
print(str(resultado), end = "")
