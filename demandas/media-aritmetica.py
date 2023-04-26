nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1+nota2+nota3)/3
print("A sua média é {}".format(media))

if media >= 7:
    print("Aprovado!")
elif media <= 6 and media >= 4:
    print("Recuperação!")
elif media <= 3:
    print("Reprovado!")