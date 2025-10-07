
name = input('Digite seu Nome: ')
age = int(input('Digite sua idade: '))


print("Olá,", name)

if age >= 60:
    print('Terceira idade')

elif age >= 18:
    print('Maior de idade')

else:
    print('Menor de idade')
    print('Ultima linha da minha estrutura')
print('Print fora da minha estrutura')