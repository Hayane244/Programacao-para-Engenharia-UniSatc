# 2) Construa um script em linguagem Python que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundos). Ao fim, o script deve calcular a velocidade média, em m/s, do objeto. Mostrar os dados fornecidos e o valor calculado.

deslocamento = int (input("Digite a variação do deslocamento (em metros): "))
tempo = int (input("Digite a variação do tempo (em segundos): "))

v_media = deslocamento / tempo

print("\n--- Resultado ---")
print(f"Deslocamento: {deslocamento} metros")
print(f"Tempo: {tempo} segundos")
print(f"Velocidade Média: {v_media} m/s")







