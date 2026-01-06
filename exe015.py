#Aluguel de carros
dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (Km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')