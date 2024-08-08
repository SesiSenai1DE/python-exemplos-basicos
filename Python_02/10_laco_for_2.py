print("=====LOJAS=====")
print(" ")

# Array das lojas
lojas = ["Santo André", "São Bernardo", "São Caetano", "Diadema"]

# Exibindo Lojas
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")
    print(" ")

# Escolhendo uma loja para exibição
loja_selecionada = int(input("Selecione a loja desejada: "))

# Exibindo a loja selecionada (Caso exista)
# if 1 <= loja_selecionada <= len(lojas):
#     print(lojas[loja_selecionada -1])
# else:
#     print("Loja inválida!")

# Outra forma de exibir a loja selecionada (Caso exista)
for i, loja in enumerate(lojas, 1):
    if loja_selecionada == i:
        print(loja)
        break
else:
    print("Loja inválida!")