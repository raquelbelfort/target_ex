# EXERCISE 1 : FIBONACCI

limite = int(input("Informe o limite para o cálculo da sequência de Fibonacci: "))

fibonacci = [0, 1]
while fibonacci[-1] < limite:
    proximo_valor = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_valor)

print("Sequência de Fibonacci até o limite informado:")
print(fibonacci)

numero_verificar = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))

if numero_verificar in fibonacci:
    print(f"O número {numero_verificar} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_verificar} não pertence à sequência de Fibonacci.")



# EXERCISE 2 : INVOICING 

import json

with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len([f for f in faturamento_diario if f > 0])

dias_acima_da_media = len([f for f in faturamento_diario if f > media_mensal])

print("Menor valor de faturamento diário: R$", menor_faturamento)
print("Maior valor de faturamento diário: R$", maior_faturamento)
print(f"Número de dias com faturamento diário acima da média mensal (R$ {media_mensal:.2f}):", dias_acima_da_media)



# EXERCISE 3 : PERCENTAGE 

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valor_total = sum(faturamento_estados.values())

percentuais = {estado: (faturamento / valor_total) * 100 for estado, faturamento in faturamento_estados.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")



# EXERCISE 4 : STRING

string_original = "string"

string_invertida = []

for i in range(len(string_original)-1, -1, -1):
    string_invertida.append(string_original[i])

string_invertida = ''.join(string_invertida)

print(string_invertida)