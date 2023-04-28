import random

print("SORTEANDO ENTRE 3 PESSOAS")

nome1 = input("1° Digite seu nome: ")
nome2 = input("2° Digite seu nome: ")
nome3 = input("3° Digite seu nome: ")

lista = [nome1, nome2, nome3]
sorteio = random.choice(lista)

print("A pessoa sorteada foi: {}".format(sorteio))
