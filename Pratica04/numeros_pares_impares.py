pares = 0
impares = 0

entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

while entrada != "fim":
    numero = int(entrada)

    if numero % 2 == 0:
        print(numero, "é par")
        pares = pares + 1
    else:
        print(numero, "é ímpar")
        impares = impares + 1

    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)