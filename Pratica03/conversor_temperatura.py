# Conversor de Temperatura

temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ")
destino = input("Digite a unidade de destino (C, F, K): ")

if origem == "C" and destino == "F":
    resultado = (temp * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temp + 273.15
elif origem == "F" and destino == "C":
    resultado = (temp - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temp - 273.15
elif origem == "K" and destino == "F":
    resultado = (temp - 273.15) * 9/5 + 32
else:
    resultado = temp

print("Temperatura convertida:", resultado)