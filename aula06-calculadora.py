# Tipos Primitivos e Saída de Dados
# int = números inteiros positivos, negativos ou nulo ex. 7 -4 0
# float (ou Números reais) = numeros que possuem (PONTO) 4.5 0.456 -15.555
# bool = VALOR LOGICO TRUE OU FALSE
# str = STRING 'OLÁ' '7.5' '' (VAZIA)

n1 = int(input('Digite um valor: ')) # O int contatena função de somar
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print('A soma vale', s)
print (f'A soma entre {n1} e {n2} vale {s}')