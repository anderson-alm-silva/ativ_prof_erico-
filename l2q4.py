#faça um programa que verifique se uma letra é vogal ou consoantes 

palavra = input('digite a letra: ').lower() 
vogais = ('a','e','i','o','u')
if palavra in vogais:
    print('A letra é vogal')
else:
    print('A letra é consoante')