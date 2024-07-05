def adicionar_funcionario(nome, salario, profissao):
    funcionario = {
        'nome': nome,
        'salario': salario,
        'profissao': profissao
    }
    funcionario.append(funcionario)
    print(f"Funcionário {nome} adicionado com sucesso.")

def listar_funcionarios():
    """Lista todos os funcionários."""
    if not funcionario:
        print("Nenhum funcionário cadastrado.")
    else:
        print("Lista de Funcionários:")
        for funcionario in funcionario:
            print(f"Nome: {funcionario['nome']}, Salário: {funcionario['salario']}, Profissão: {funcionario['profissao']}")
