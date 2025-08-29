# Calculadora da Média

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

media = (N1*2 + N2*3 + N3*4 + N4*1) / 10

print("Media:", round(media, 1))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input("Digite a nota do exame: "))
    print("Nota do exame:", exame)
    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:", round(media_final, 1))