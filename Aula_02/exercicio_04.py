#1) Escreva um script em linguagem Python que receba 2 valores de x e y. Em seguida, calcule e imprima o valor de z:
#  z: (x²+y²) / x-y

x = int (input("Digite o valor de x: "))
y = int (input("Digite o valor de y: "))

z = (x **2 + y **2) / (x - y)

print("Calculo: (x²+y²) / x-y z")
print(f"Resultado: {z}")
