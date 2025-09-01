while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha == "sair":
        break

    if len(senha) >= 8:
        tem_numero = False
        for letra in senha:
            if letra.isdigit():
                tem_numero = True
                break

        if tem_numero:
            print("Senha forte cadastrada!")
            break
        else:
            print("Senha precisa ter pelo menos um número e um carácter: @, #, %, $, &.")
    else:
        print("Senha muito curta (mínimo 8 caracteres).")