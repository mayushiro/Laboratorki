import random
print('Размерность матрицы?')
N = int(input())
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
r = 0
resultat = []
c = []
print('Ввести 1 для ручного ввода и 2 для рандомного заполнения матрицы')
c1 = int(input())
if c1 == 1:
	R = N
	C = N
	matrix1 = []
	print('Введи элементы первой матрицы')
	for a in range(R):
		b = []
		for c in range(C):
			b.append(int(input()))
		matrix1.append(b)
	for a in range(R):
		for c in range(C):
			print(matrix1[a][c], end=" ")
		print()
	R = N
	C = N
	matrix2 = []
	print('Введи элементы второй матрицы')
	for a in range(R):
		d = []
		for c in range(C):
			d.append(int(input()))
		matrix2.append(d)
	for a in range(R):
		for c in range(C):
			print(matrix2[a][c], end=" ")
		print()
if c1 == 2:
	R = N
	C = N
	matrix1 = []
	print('Введи элементы первой матрицы')
	for a in range(R):
		b = []
		for c in range(C):
			b.append(random.randint(0, 100))
		matrix1.append(b)
	for a in range(R):
		for c in range(C):
			print(matrix1[a][c], end=" ")
		print()
	R = N
	C = N
	matrix2 = []
	print('Введи элементы второй матрицы')
	for a in range(R):
		d = []
		for c in range(C):
			d.append(random.randint(0, 100))
		matrix2.append(d)
	for a in range(R):
		for c in range(C):
			print(matrix2[a][c], end=" ")
		print()
print('Выполнить умножение(*) вычитание(-) или сложение(+)?')
f=input()
if (f=="+"):
		for a in range(len(matrix1)):
			for c in range(len(matrix1[0])):
				print(matrix1[a][c] + matrix2[a][c], end=" ")
			print ('\n')
if (f=="-"):
		for a in range(len(matrix1)):
			for c in range(len(matrix1[0])):
				print(matrix1[a] [c] - matrix2[a][c], end=" ")
			print ('\n')
if (f=="*"):
		for a in range(len(matrix1)):
			for c in range(len(matrix1[0])):
				print(matrix1[a][c] * matrix2[a][c], end=" ")
			print ('\n')

