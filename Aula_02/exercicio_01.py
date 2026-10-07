# 1) A fórmula dos juros compostos é a seguinte:
# FV = PV.(1+I)^n
from xml.dom.expatbuilder import FilterVisibilityController

# Onde:
# FV - Valor final do investimento, ao término do tempo
# PV - Valor inicial que o cliente irá investir
# i - Rentabilidade mensal (em porcentagem)
# n - Quantidade de meses que o dinheiro do cliente vai ficar aplicado

# Elabore um Script em Python que solicite o valor do investimento (PV), o número de meses (n) que irá permanecer aplicado e  a rentabilidade (i). Ao final, o script deve mostrar o valor do montante total (FV).

PV = float (input ("Quanto você deseja investir? \n"))
n = int (input("Quantos meses seu dinheiro ficará aplicado? \n"))
i_porcentagem = float (input("Qual a rentabilidade do investimento aplicado? \n"))

#Converte a taxa percentual para valor decimal
i = i_porcentagem / 100

#Calcule o montante final (FV)
FV = PV * ((1+i) ** n)

print ("\n--RESUMO DO INVESTIMENTO--")
print (f"Valor Inicial: (PV): R$ {PV:.2F}")
print (f"Taxa Mensal (i): {i_porcentagem}%")
print (f"período (n): {n} meses")
print(f"O valor do montante final é de: {FV:.2f}")
