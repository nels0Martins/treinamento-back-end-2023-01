'''1. Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
a. se ele ainda vai se alistar ao serviço militar
b. se é a hora de se alistar.
c. se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta que passou do prazo'''

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
idade = int(2023 - ano_nascimento)
print(f'Você tem {idade} anos!')

if idade < 18:
    print("Você deve se alistar apenas com 18 anos!")
elif idade == 18:
    print("Já está na hora de se alistar!")
elif idade > 18:
    print("Você já passou da hora de se alistar!")
