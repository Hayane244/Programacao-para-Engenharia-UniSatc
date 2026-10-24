# 8) Agora faça o contrário. Você fornece a temperatura em graus Fahrenheit, seu script converte para Celsius e exibe na tela.

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Temperatura em Fahrenheit:", fahrenheit, "°F")
print("Temperatura em Celsius:", celsius, "°C")