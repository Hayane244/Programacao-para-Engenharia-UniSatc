# Escreva um script em linguagem Python que peça o raio de um círculo e, em seguida, exiba o perímetro e a área do círculo. Para saber o valor do pi, faça:
# import math
# print(math.pi)

import math

raio = float(input("Digite o raio do círculo: "))

perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print("\n--- Resultado ---")
print(f"Raio: {raio}")
print(f"Perímetro do círculo: {perimetro:.2f}")
print(f"Área do círculo: {area:.2f}")