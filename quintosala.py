print('Quinta Atividade')

opcao1 = 'Cerveja'
opcao2 = 'Drink Específico'
opcao3 = 'Água'

print('Escolha uma bebida:')
print(f'1. {opcao1}')
print(f'2. {opcao2}')
print(f'3. {opcao3}')

escolha = input("Digite o número da bebida que você escolheu (1, 2, ou 3): ").strip()
if escolha == "1":
    print(f"Você escolheu {opcao1}.")
elif escolha == "2":
    print(f"Você escolheu {opcao2}.")
elif escolha == "3":
    print(f"Você escolheu {opcao3}.")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


