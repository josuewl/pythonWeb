# Exibe o título do programa "Sabor Express" com uma linha em branco abaixo
print('Sabor Express\n')

# Exibe o menu de opções disponíveis para o usuário
print('1. Cadastrar restaurante')  # Opção para cadastrar um novo restaurante
print('2. Listar restaurante')     # Opção para listar os restaurantes cadastrados
print('3. Ativar restaurante')     # Opção para ativar um restaurante cadastrado
print('4. Sair\n')                 # Opção para sair do programa, com uma linha em branco abaixo

# Solicita ao usuário que escolha uma das opções exibidas no menu
opcao_escolhida = input('Escolha uma opção: ')

# Exibe a opção escolhida pelo usuário, interpolando o valor dentro da string
print(f'Você escolheu a opção {opcao_escolhida}')
