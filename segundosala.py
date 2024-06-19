print('Segundo:')
print('Em que cidade o cantor Lenine nasceu?')
print('a) Rio de Janeiro')
print('b) Recife')
print('c) Salvador')
resposta = input("Vamos lá!! Espero que você acerte :) ").strip()
resposta = resposta.lower()
if resposta.lower() == 'b':
    print('Parabéns! Você acertou! O cantor Lenine nasceu na cidade do Recife')
else:
    print('ops, você errou! O cantor Lenine nasceu na cidade do recife.')
    
