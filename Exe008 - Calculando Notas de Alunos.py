#Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre sua média

n1 = float(input('Digite a primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = (n1 + n2) / 2  #coloquei entre parenteses n1 e n2 por causa da ordem de precedencias: 1º(), 2º**, 3º* / // %, 4º+ -

print('A média entre {} e {}, é igual a {:.1f} '.format(n1, n2, m))
