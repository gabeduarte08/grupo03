def adicionar_funcionario(funcionarios, id, nome, cargo, salario):
    funcionarios[id] = {
        'nome': nome,
        'cargo': cargo,
        'salario': salario
    }
    print(f"Funcionário '{nome}' adicionado com sucesso.")

def atualizar_funcionario(funcionarios, id, nome=None, cargo=None, salario=None):
    if id in funcionarios:
        if nome:
            funcionarios[id]['nome'] = nome
        if cargo:
            funcionarios[id]['cargo'] = cargo
        if salario:
            funcionarios[id]['salario'] = salario
        print(f"Funcionário '{id}' atualizado com sucesso.")
    else:
        print(f"Funcionário com ID '{id}' não encontrado.")

def remover_funcionario(funcionarios, id):
    if id in funcionarios:
        del funcionarios[id]
        print(f"Funcionário '{id}' removido com sucesso.")
    else:
        print(f"Funcionário com ID '{id}' não encontrado.")

def detalhes_funcionario(funcionarios, id):
    if id in funcionarios:
        funcionario = funcionarios[id]
        print(f"ID: {id}")
        print(f"Nome: {funcionario['nome']}")
        print(f"Cargo: {funcionario['cargo']}")
        print(f"Salário: {funcionario['salario']}")
    else:
        print(f"Funcionário com ID '{id}' não encontrado.")

def menu():
    funcionarios = {}
    while True:
        print("1 - Adicionar Funcionário")
        print("2 - Atualizar Funcionário")
        print("3 - Remover Funcionário")
        print("4 - Detalhes de um Funcionário")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            id = input("Digite o ID do funcionário: ")
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            adicionar_funcionario(funcionarios, id, nome, cargo, salario)

        elif opcao == '2':
            id = input("Digite o ID do funcionário que deseja atualizar: ")
            nome = input("Digite o novo nome (ou deixe em branco para manter o mesmo): ")
            cargo = input("Digite o novo cargo (ou deixe em branco para manter o mesmo): ")
            salario = input("Digite o novo salário (ou deixe em branco para manter o mesmo): ")
            if salario:
                salario = float(salario)
            else:
                salario = None
            atualizar_funcionario(funcionarios, id, nome, cargo, salario)

        elif opcao == '3':
            id = input("Digite o ID do funcionário que deseja remover: ")
            remover_funcionario(funcionarios, id)

        elif opcao == '4':
            id = input("Digite o ID do funcionário que deseja visualizar os detalhes: ")
            detalhes_funcionario(funcionarios, id)

        elif opcao == '5':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()