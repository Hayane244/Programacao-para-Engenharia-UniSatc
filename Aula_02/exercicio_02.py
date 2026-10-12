#2) Ainda sobre juros compostos: Um cliente pediu que o sistema do banco tivesse a seguinte função:

#Informar o valor inicial que ele deve investir, para ao final de ‘n' meses ele tenha um valor ‘fv', supondo que este dinheiro esteja com uma rentabilidade 'i' mensal, em porcentagem.

#Desenvolva um script em Python que solicite o valor final, o número de meses que retende deixar seu dinheiro aplicado, bem como a rentabilidade. O script deve exibir o valor inicial que ele deve investir para atingir tal objetivo.

fv = float(input("Qual valor você deseja receber ao final do investimento? "))
n = int(input("Por quantos meses pretende investir? "))
i_porcentagem = float(input("Qual a rentabilidade mensal (%)? "))

# Transformando a porcentagem em valor decimal
i = i_porcentagem / 100

# Calculando o valor inicial
pv = fv / ((1 + i) ** n)

print(f"R$ {pv:.2f} deverá ser investido para atingir o objetivo final.")