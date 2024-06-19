print('Atividade Quatro')

possui_irmaos = input("Você possui irmãos? (sim/não): ").strip().lower()
if possui_irmaos == "sim":
    quantos_irmaos = input("Quantos irmãos você tem? ").strip()
    print(f"Que legal! Você tem {quantos_irmaos} irmãos.")
elif possui_irmaos == "não":
 gostaria_ter_irmaos = input("Você gostaria de ter irmãos? (sim/não): ").strip().lower()
 if gostaria_ter_irmaos == "sim":
   print("Seria interessante ter irmãos!")
 else:
   print("Tudo bem, ser filho único também tem suas vantagens!")
else:
   print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
   


   

    