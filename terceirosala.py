print('terceiro:')
nome = input("Por favor, insira um nome: ")
gosta_do_nome = input(f"Você gosta do nome {nome}? (Sim/Não): ")
if gosta_do_nome.lower() == 'sim':
        print("Que ótimo! Fico feliz que você goste do nome.")
elif gosta_do_nome.lower() == 'não':
         print("Ah, entendo. Nem todos nomes agradam a todos.")
else:
         print("Desculpe, não entendi sua resposta. Por favor, responda com 'Sim' ou 'Não'.")
         
    