peso = float(input("Informe o seu peso (em Kg): "))
altura = float(input("Informe a sua altura (em metros): "))


# Formula
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else: 
    classificacao = "Obesidade"

# Resultado
print(f"Seu imc é: {imc:.1f}. Classificação: {classificacao}.")
