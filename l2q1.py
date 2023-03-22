#Faça um Programa que peça dois números e imprima o maior deles.

#entrada
print("Programa para comparar dois números")
numero_1 = int(input("Digite o 1 numero para comparar: "))
numero_2 = int(input("Digite o 2 numero para comparar: "))
numero_3 = int(input("digite o 3 numero para compara : "))
#processamento
if numero_1 > numero_2:
    print("O número {} é o maior".format(numero_1))
else:
    print('O número {} é o maior'.format(numero_2))
    