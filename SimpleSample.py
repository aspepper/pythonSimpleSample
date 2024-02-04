# Concatenação de strings
name = "Alex"
surname = "Pimenta"
fullname = nome + " " + surname

# Impressão do resultado
print("Nome completo:", fullname)

# Substituição de texto
message = "Olá, {name}! Bem-vindo ao DevForge."
personalizedMessage = mensagem.format(name=name)

# Impressão da mensagem personalizada
print(personalizedMessage)

# Verificação de substrings
if "Pimenta" in fullname:
    print("Has a surname Pimenta.")

# Transformação para maiúsculas
fullnameUpper = fullname.upper()

# Impressão do nome em maiúsculas
print("Uppercase Name:", fullnameUpper)
