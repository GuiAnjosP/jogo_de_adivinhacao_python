print('Seja bem-vindo a calculadora da empresa!')
faturamento = float(input('Digite o valor do faturamento da sua empresa:'))
custo = float(input('Digite o custo total da sua empresa:'))
imposto = 0.15 * faturamento
lucro = faturamento - custo - imposto
print(f'Você vai pagar R${imposto} de imposto.')
print(f'Seu lucro foi de R${lucro}')

mensagem = "O faturamento da loja foi de 2100" #string

teve_lucro = True #boolean

margem_lucro = lucro / faturamento
print(f'Sua margem de lucro foi de {margem_lucro}%')
# int = numeros inteiores
# float = numeros casa decimal
# strings = textos
# boolean = booleanos (True False)

# operadores especiais
# mod -> %
# resto da divisão de um número pelo outro
# 10 % 3 = resta 1, ou seja, é o mod da divisão

anos = int(310/12)
print(anos,'anos')
meses = 310 % 12
print(meses,'meses')
# floor division -> //
print(310 // 12
      )