import random
numero_secreto =  random.randint(1,10)
# Isso fará o algoritmo escolher um número de 1 a 10!
print('Número gerado!')
palpite = int(input('Tente adivinhar o número:'))

if palpite == numero_secreto:
    print('Você acertou!')
else:
    if palpite < numero_secreto:
        print('Tente um número MAIOR!')
    else:
        print('Tente um número MENOR!')
    while palpite != numero_secreto:
        palpite = int(input('Tente novamente:'))
        if palpite < numero_secreto:
            print('MAIOR!')
        elif palpite > numero_secreto:
            print('MENOR!')
            
print('Agora sim você acertou!')