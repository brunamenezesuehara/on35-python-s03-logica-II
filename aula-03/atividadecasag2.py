print('Exercício Grupo 2')

def operacao_matematica(opcao, num1, num2):
    if opcao == 1:
        return num1 + num2
    elif opcao == 2:
        return num1 - num2
    elif opcao == 3:
        return num1 * num2
    elif opcao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Opção inválida"
print("Escolha uma operação matemática:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite o número da operação desejada: "))
if opcao in [1, 2, 3, 4]:
     num1 = float(input("Digite o primeiro valor: "))
     num2 = float(input("Digite o segundo valor: "))
     resultado = operacao_matematica(opcao, num1, num2)
     print(f"O resultado da operação é: {resultado}")
else:
     print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

def verifica_divisibilidade(numero):
    if (numero % 3 == 0) and (numero % 5 == 0):
        return "O número é divisível por 3 e 5 simultaneamente."
    elif (numero % 3 == 0):
        return "O número é divisível por 3."
    elif (numero % 5 == 0):
        return "O número é divisível por 5."
    else:
        return "O número não é divisível nem por 3 nem por 5."
numero = int(input("Digite um número inteiro: "))
resultado = verifica_divisibilidade(numero)
print(resultado)
def verifica_aposentadoria(idade, tempo_servico):
    if idade >= 65:
        return "Pode se aposentar."
    elif tempo_servico >= 30:
        return "Pode se aposentar."
    elif idade >= 60 and tempo_servico >= 25:
        return "Pode se aposentar."
    else:
        return "Não pode se aposentar."
idade = int(input("Digite a idade do trabalhador: "))
tempo_servico = int(input("Digite o tempo de serviço do trabalhador (em anos): "))
resultado = verifica_aposentadoria(idade, tempo_servico)
print(resultado)

