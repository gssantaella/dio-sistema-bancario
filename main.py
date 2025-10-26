menu = """\n
================ MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[q]\tSair
=> """


def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(valor, saldo, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return


def encontra_usuario(lista, cpf):
    return [usuario for usuario in lista if usuario["cpf"] == cpf]

def cria_usuario(lista_usuarios):
    cpf = input("Digite CPF (somente numeros): ")
    
    existe_usuario = bool(encontra_usuario(lista_usuarios, cpf))

    if existe_usuario:
        print("\n>>> Existe usuario com CPF informado")
        return

    nome = input("nome completo: ")
    data_nascimento = input("data de nascimento (dd-mm-aaaa): ")
    endereco = input("endereco (logradouro, numero - bairro - cidade - estado): ")

    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}

    print("\n>>> Usuario inserido")

    return usuario


def cria_conta(agencia, numero_conta, lista_usuario):
    cpf = input("Digite CPF do usuario: ")
    usuario = encontra_usuario(lista_usuario, cpf)

    if usuario:
        print("\n>>> Conta criada")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario[0]}

    print("\n>>> Usuario nao existe")


def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Ag:\t{conta['agencia']}
            Cc:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    numero_conta = 1
    contas = []

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(
                valor=valor,
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "nu":
            usuario = cria_usuario(usuarios)
            if usuario:
                usuarios.append(usuario)

        elif opcao == "nc":
            conta = cria_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            lista_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    return


if __name__ == '__main__':
    main()