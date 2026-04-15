email = "EMAIL_FALSO@gmail.com"

email = email.lower() # colocar em letra minúscula
email = email.strip() # ajustar espaços vazios
print(email)

# tamanho
print(len(email))

# posição (começa a contar do zero) se tiver 2 ou mais letras ele apenas pegará a primeira
posicao = email.find("@")
print(posicao)

# pegar pedaços do texto  o : significa até ou seja, da posição 11 até a posição 13
servidor = (email[posicao+1:])
print(servidor)


# troocar um pedaço do texto
novo_email = (email.replace("@gmail.com", "@yahoo.com.br"))
print(novo_email)

nome = "guilherme anjos"
nome = nome.capitalize() # coloca apenas a primeira letra maiúscula.
print(nome)
nome = nome.title() #colocar os nomes e sobrenomes com a primeira letra maiuscula.
print(nome)
nome = nome.upper() #coloca todas as letras maiúsculas
print(nome)


#formatação numerica
faturamento  = 1_000_000
custo = 50000
lucro = faturamento - custo
margem = lucro / faturamento
texto = f"O lucro foi de  R${lucro:,.2f} e o faturamento de R${faturamento:,.2f} e margem foi de {margem:.0%}"
print(texto)

# exercicios
nome = "guilherme dos anjos pinto"
email = "emailfalsodogui@gmail.com"

# descubra o servidor do email
posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)
# descubra o 1º nome do usuario
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()
print(primeiro_nome)
# criar uma mensagem personalizada "Usuario {primeiro nome} foi cadastrado com sucesso no emal {email}"
mensagem = f"Usuário {primeiro_nome} foi cadastrado com sucesso no email {email}"
print(mensagem)