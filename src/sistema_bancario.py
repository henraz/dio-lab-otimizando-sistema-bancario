mensagem_input = f"""\n{' Sistema Bancário ':-^60}
Opções disponíveis:

[C] - Criar usuário
[K] - Criar conta
[D] - Depósito
[S] - Saque
[E] - Extrato
[Q] - Sair

Qual operação deseja realizar? """

saldo = 0
quantidade_saque = 0
desc_extrato = ""
usuarios = []
contas = []


def deposito(saldo_conta, extrato_conta, /) -> tuple:

    print("\nOpção selecionada: [D] - Depósito.")
    valor_deposito = float(input("Digite a quantidade desejada para depósito: "))

    if valor_deposito > 0:
        saldo_conta += valor_deposito
        extrato_conta = extrato_conta + "\n" + "R$ +" + str(valor_deposito)
        msg = f"Depósito realizado com sucesso: R$ {valor_deposito:.2f}"
        print(f"\n{msg:^60}")
    else:
        print(f"\n{'Deve-se depositar um valor maior que zero.':^60}")

    return saldo_conta, extrato_conta


def saque(*, saldo_conta, num_saque, extrato_conta) -> tuple:

    print("\nOpção selecionada: [S] - Saque.")
    
    if num_saque == 3:
        print(f"\n{'Não é possível realzar o saque. Limite de saques diários: 3':^60}")
    else:    
        valor_saque = float(input("Digite a quantidade desejada para saque: "))

        if valor_saque > 500:
            print(f"\n{'Não é possível realizar o saque.':^60}")
            print(f"\n{'Valor máximo diário permitido: R$ 500,00.':^60}")

        elif valor_saque > saldo_conta:
            msg = f"Não há saldo o suficiente. Saldo atual: R$ {saldo_conta:.2f}."
            print(f"\n{msg:^60}")

        elif valor_saque < 0:
            print(f"\n{'Deve-se digitar um valor maior que zero.':^60}")
        else:
            saldo_conta -= valor_saque
            num_saque += 1
            extrato_conta = extrato_conta + "\n" + "R$ -" + str(valor_saque)
            msg = f"Saque realizado com sucesso: R$ {valor_saque:.2f}"
            print(f"\n{msg:^60}")

    return saldo_conta, num_saque, extrato_conta


def extrato(saldo_conta, /, *, extrato_conta) -> None:

    print("\nOpção selecionada: [E] - Extrato.")
    print(f"\n{' Extrato Bancário ':#^60}") 
    if extrato_conta == "":
        print(f"\n{'Não foram realizadas movimentações.':^60}")
    else:
        print(extrato_conta)
        print(f"Saldo atual da conta: R$ {saldo_conta:.2f}")
    print("")
    print(60*"#")

    return extrato_conta


def verifica_cpf_usuario(lista_usuarios, cpf) -> int:

    for usuario in lista_usuarios:
        if cpf == usuario['cpf']:
            return usuario
    return 0


def criar_usuario(lista_usuarios):

    print("\nOpção selecionada: [C] - Criar Usuário.")
    nome = input("Digite o nome do usuário: ")
    data_nascimento  = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF (Apenas números): ")
    endereco = input("""Digite o endereço 
(logradouro, numero - bairro - cidade/sigla estado): """)

    if verifica_cpf_usuario(lista_usuarios, cpf) != 0:
        msg = f"CPF: {cpf} já está cadastrado."
        print(f"\n{msg:^60}")
    else:
        lista_usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':endereco})
        print(f"\n{'Usuário cadastrado com sucesso.':^60}")
    return lista_usuarios


def criar_conta(lista_contas):

    print("\nOpção selecionada: [K] - Criar Conta.")
    cpf = input("Digite o CPF: ")
    if len(lista_contas) == 0:
        numero_conta = 1
    else:
        numero_conta = len(lista_contas) + 1

    usuario = verifica_cpf_usuario(lista_usuarios, cpf)
    if usuario == 0:
        print(f"\n{'Usuário não existe. Não será possível criar a conta.':^60}")
    else:
        lista_contas.append({'agencia':'0001', 'conta':numero_conta, 'usuario':usuario})
        msg = f"Conta criada com sucesso! Agência: 0001, Número da conta {numero_conta}"
        print(f"\n{msg:^60}")

    return lista_contas


while True:

    operacao = input(mensagem_input).upper()

    if operacao not in 'CKDSEQ':
        print(f"\n{'Operação inválida!':^60}")

    if operacao == 'C':

        lista_usuarios = criar_usuario(usuarios)

    if operacao == 'K':
        
        lista_contas = criar_conta(contas)

    if operacao == 'D':

        saldo, desc_extrato = deposito(saldo, desc_extrato)

    if operacao == 'S':

        saldo, quantidade_saque, desc_extrato = saque(saldo_conta=saldo, num_saque=quantidade_saque, 
                                                      extrato_conta=desc_extrato)
    if operacao == 'E':

        desc_extrato = extrato(saldo, extrato_conta=desc_extrato)

    if operacao == 'Q':

        print("\nOpção selecionada: [Q] - Sair.")
        print("Saindo ...")
        break

    print(60*"-")