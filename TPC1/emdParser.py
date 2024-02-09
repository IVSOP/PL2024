#!/usr/bin/env python3


modalidades = set({})

total_atletas = 0
aptos = 0
inaptos = 0

idades = []
for i in range(0, 20): # duvido que haja atletas com 100 anos
	idades.append(0)

with open("./emd.csv", "r") as file:
	lines = file.readlines()
	for line in lines[1:]:
		_id,index,dataEMD,nome_primeiro,nome_último,idade,género,morada,modalidade,clube,email,federado,resultado = line.rstrip().split(',')

		modalidades.add(modalidade)

		total_atletas += 1
		if (resultado == "true"):
			aptos += 1
		else:
			inaptos += 1

		idades[int(int(idade) / 5)] += 1


print("Modalidades:")
for mod in sorted(modalidades):
	print("    " + mod)

print("Atletas aptos:")
print("    " + str(100 * float(aptos) / float(total_atletas)) + "%")
print("Inaptos:")
print("    " + str(100 * float(inaptos) / float(total_atletas)) + "%")

print("Numero de atletas por escalao:")
for i in range(0, 20):
	num = idades[i]
	if (num > 0):
		print("    [" + str(i * 5) + "-" + str(((i + 1) * 5) - 1) + "]: " + str(num))
