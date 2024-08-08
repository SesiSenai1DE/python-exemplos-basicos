valor = int(input("Informe o valor: "))

# Uso do If ternário
teste = "Situação Normal!" if valor < 100 else "Situação: Pré-diabetes!" if valor in range (100,125) else "Diabetes"

# Exibição
print(teste)