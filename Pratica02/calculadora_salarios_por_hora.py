# Calculadora de Salário por Horas Trabalhadas

numero = int(input("Digite o número do funcionário: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))
valor = float(input("Digite o valor por hora: "))

salario = horas * valor

print("Número do funcionário:", numero)
print("Salário:", salario)