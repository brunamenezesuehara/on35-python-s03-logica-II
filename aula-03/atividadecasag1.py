print('Exercício Grupo 1')

def encontrar_maior_e_diferenca(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2

    diferenca = abs(num1 - num2)

    return maior, diferenca
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
maior, diferenca = encontrar_maior_e_diferenca(num1, num2)
print(f"O maior número é: {maior}")
print(f"A diferença entre os dois números é: {diferenca}")

def encontrar_maior_ou_igual(num1, num2):
    if num1 > num2:
        return f"O maior número é: {num1}"
    elif num2 > num1:
        return f"O maior número é: {num2}"
    else:
        return "Números iguais"
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = encontrar_maior_ou_igual(num1, num2)
print('resultado')

def dia_da_semana(numero):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    
    return dias.get(numero, "Número inválido. Por favor, digite um número entre 1 e 7.")
numero = int(input("Digite um número inteiro entre 1 e 7: "))
resultado = dia_da_semana(numero)
print(resultado)

