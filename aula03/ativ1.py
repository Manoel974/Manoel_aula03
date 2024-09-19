import os

#os.system('cls')

#valor = int(input('coloque um valor: '))

#if valor > 0:
 #   print(f'{valor} positivo')

#elif valor < 0:
 #   print(f'{valor} negtivo')

#else:
 #   print(f'{valor} Não digite zero')    

# n = int(input('Informe o número: '))

# if n != 0 :
#     if n > 0 :
#         print(f'{n} positvo')
#     else:
#         print(f'{n} negativo')
# else:
#     print('Não digite zero')

# p = float(input('Informe o peso: '))
# a = float(input('Informe a altura: '))

# imc = p / a**2

# if imc < 18.5:
#     print('Abaixo do peso')
# elif 24.9 > imc > 18.5:
#     print('Peso normal')
# elif 25.0 > imc > 24.9:
#       print('Sobrepeso')
# else:
#      print('Obesidade')


# profissao = input('Profissão').upper()
# Localidade = input('Localidade').upper()


resposta = input('Quer desconto Sim / Não? ')[0].upper()

if resposta =='S':
    print('Desconto!!!')
else:
    print('Não tem desconto')
    