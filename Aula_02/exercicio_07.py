# 7) Você está no Brasil, e para temperatura usamos o grau Celsius. Porém, quando você for contratado para trabalhar como programador Python no exterior, deverá usar graus Fahrenheit.
# Ou seja, você fornece a temperatura em graus Celsius, e seu script faz a conversão para graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperatura em Celsius:", celsius, "°C")
print("Temperatura em Fahrenheit:", fahrenheit, "°F")