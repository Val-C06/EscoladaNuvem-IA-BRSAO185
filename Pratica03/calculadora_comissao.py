# Calculadora de Comissão

nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o total de vendas: "))

comissao = vendas * 0.15
total = salario_fixo + comissao

print("Nome do vendedor:", nome)
print("Total a receber:", round(total, 2))