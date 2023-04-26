# Valor da passagem:
# Até 200km = 1.50
# Mais que 200km = 1.25

distancia = float(input("Digite uma distancia em KM: "))

if distancia <= 200.0:
    km = float(1.50)
    total = distancia*km
    print("Preço da passagem: R${:.2f}".format(total))

else:
    km = float(1.25)
    total = distancia*km
    print("Preço da passagem: R${:.2f}".format(total))
