notas = []

while True:
    entrada = input("Digite a nota (ou 'fim' para encerrar): ")

    if entrada == "fim":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota fora do intervalo 0 a 10.")
    except:
        print("Entrada inválida. Digite um número.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("Média da turma:", media)
else:
    print("Nenhuma nota válida foi registrada.")