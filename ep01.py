def main():
	print()
	print("modo: ", end = "")
	modo = int(input())

	if (modo == 1):
		
		print("n1: ", end = "")
		n1 = int(input())
		
		print("n2: ", end = "")
		n2 = int(input())
		
		print("n3: ", end = "")
		n3 = int(input())
		
		print("n4: ", end = "")
		n4 = int(input())
		
		print("n: ", end = "")
		n = int(input())

		somaQuadrados = n1*n1 + n2*n2 + n3*n3 + n4*n4

		if (somaQuadrados == n):
			print("verdadeiro")
		else:
			print("falso")

	elif (modo == 2):
		print("n: ", end = "")
		n = int(input())

		primo1 = 1
		primo2 = 2
		primo3 = 3
		primo4 = 5
		achouQuadrados = False
		somaQuadrados = primo1 * primo1 + primo2 * primo2 + primo3 * primo3 + primo4 * primo4

		while (somaQuadrados <= n and not achouQuadrados):
			
			if ( somaQuadrados == n):
				print("%d %d %d %d" % (primo1, primo2, primo3, primo4))
				achouQuadrados = True

			else:
				primo1 = primo2
				primo2 = primo3
				primo3 = primo4

				achouPrimo = False
				while (not achouPrimo):
					primo4 += 1
					contador = 0
					divisor = primo4
					while (divisor >= 1):
						if (primo4 % divisor == 0):
							contador += 1
						divisor -= 1
					if (contador == 2):
						achouPrimo = True

			somaQuadrados = primo1 * primo1 + primo2 * primo2 + primo3 * primo3 + primo4 * primo4

		if (not achouQuadrados):
			print("falso")
main()