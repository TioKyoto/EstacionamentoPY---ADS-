def menu():
    """
    Mostra o menu de opções.
    
    Returns:
        str: Opção que o usuário escolheu.
    """
    print("\n----- Menu -----")
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def estacionar_veiculo(estacionamento, default_proprietario):
    """
    Estaciona um veículo no estacionamento.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
        default_proprietario (str): O nome do proprietário padrão.
    """
    placa = input("Digite a placa do veículo: ")
    if placa in estacionamento:
        print("Veículo já está estacionado.")
        return
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    proprietario = input(f"Digite o nome do proprietário (ou pressione Enter para usar '{default_proprietario}'): ")
    if not proprietario:
        proprietario = default_proprietario
    estacionamento[placa] = {
        'marca': marca,
        'modelo': modelo,
        'cor': cor,
        'proprietario': proprietario
    }
    print("Veículo estacionado.")

def retirar_veiculo(estacionamento):
    """
    Retira um veículo do estacionamento.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
    """
    placa = input("Digite a placa do veículo: ")
    if placa in estacionamento:
        del estacionamento[placa]
        print("Veículo retirado.")
    else:
        print("Veículo não encontrado.")

def listar_veiculos(estacionamento):
    """
    Lista todos os veículos estacionados.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
    """
    if not estacionamento:
        print("Nenhum veículo estacionado.")
    else:
        for placa, dados in estacionamento.items():
            print(f"Placa: {placa}, Marca: {dados['marca']}, Modelo: {dados['modelo']}, Cor: {dados['cor']}, Proprietário: {dados['proprietario']}")

def verificar_veiculo(estacionamento):
    """
    Verifica se um veículo está estacionado.

    Args:
        estacionamento (dict): O dicionário que armazena os veículos estacionados.
    """
    placa = input("Digite a placa do veículo: ")
    if placa in estacionamento:
        dados = estacionamento[placa]
        print(f"O veículo está estacionado. Marca: {dados['marca']}, Modelo: {dados['modelo']}, Cor: {dados['cor']}, Proprietário: {dados['proprietario']}")
    else:
        print("Veículo não encontrado.")

def main():
    """
    Função que gerencia o loop do menu e chama as funções.
    """
    estacionamento = {}
    default_proprietario = "Seu Nome"
    while True:
        opcao = menu()
        if opcao == '1':
            estacionar_veiculo(estacionamento, default_proprietario)
        elif opcao == '2':
            retirar_veiculo(estacionamento)
        elif opcao == '3':
            listar_veiculos(estacionamento)
        elif opcao == '4':
            verificar_veiculo(estacionamento)
        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
