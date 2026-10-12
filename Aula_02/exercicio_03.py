#3) Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem  um desconto de 35%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para X cópias?

#Solicite o valor de X. Crie um Script em linguagem Python para solicitar os dados necessários e exibir o custo total da compra.

x = int(input("Deseja fazer quantas cópias? "))

desconto = 35 / 100
preco = 24.95
#1 reprersenta 100% do preço original;
#"desconto" representa 35%, ou 0.35;
#"1 -n desconto" significa 1 - 0 = 0.35 = 0.65, ou seja, 65% do preço preço original
preco_desconto = preco * (1 - desconto)

prim_exam = 3
rest_exam = (x - 1) * 0.75

custo = (preco_desconto * x) + prim_exam + rest_exam

print(f"O custo total das {x} cópias é de R$ {custo:.2f}")