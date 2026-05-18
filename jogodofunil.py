import random

numerosecreto = random.randint(1, 100)
minimo = 1
maximo = 100
acertou = False
print('--- O JOGO DO FUNIL ---')
print('A regra é o seguinte: Você tem que adivinhar o numero de 1 a 100')
print('De acordo com suas tentativas, o numero que você tentou adivinhar substitui o minimo ou máximo')
print('Por exemplo, a primeira pergunta vem "adivinhe um numero de 1 a 100", \no numero selecionado na rodada era 70 e o seu chute era 27')
print('Como não era 27, o funil aperta, a proxima rodada vem a pergunta de 28 a 100')
print('Se sobrar apenas 4 numeros possiveis para adivinhar, você perde.')
print('Por exemplo: o numero selecionado era 78, você chutou 76 e depois 80. \nSobrariam apenas 4 numeros possíveis para adivinhar, então você perde!')
print('Mas se caso você acertar o numero, você ganha!')
print('Boa sorte!!!!')
while not acertou:
    try:

     numero = int(input(f'Diga um numero de {minimo} a {maximo}: '))

     if numero < minimo or numero > maximo:
        print(f'Preste atenção, apenas numero entre {minimo} e {maximo} ')
     elif numero == numerosecreto:
        print('PARABÉNS! VOCÊ ACERTOU O NUMERO!!!')
        acertou = True
     elif numero < numerosecreto: 
        minimo = numero + 1
     else:
        maximo = numero - 1

     if  maximo - minimo <= 4:
         print(f'QUE PENA, O NUMERO ERA: {numerosecreto}.\nVOCÊ PERDEU!!!')
         acertou = True

    except: ValueError
    print('Digite apenas numeros!!')