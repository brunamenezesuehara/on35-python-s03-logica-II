print('Exercicío sala')
print('Lógica II')
print('Primeiro:')

idade_str = input("Por favor, insira sua idade: ")

if idade_str.strip() != "":
    idade = int(idade_str)
    if idade >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade.")
else:
     print("Você não inseriu uma idade válida.")
