print('='*50)
print('Calculo da folha de pagamento!')
print('='*50)

horas_trabalhadas = int(input('Digite o valor de horas trabalhadas no mês: '))
valor_hora = int(input('Digite o valor da hora trabalhada: '))
salario_bruto = horas_trabalhadas * valor_hora

print('='*50)
print('Seu salário bruto é de {}.'.format(salario_bruto))

if salario_bruto < 900:
     print('Seu salário é isento de todos os descontos do IR!')

elif salario_bruto >= 900 or salario_bruto <= 1500:
    desco_five = salario_bruto - (salario_bruto * 0.05)

    print('Seu salário liquido com todos os descontos é {}'.format(desco_five))
    print('Total de descontos: {}'.format((salario_bruto * 0.05)))
    print('Descontos de 5%')

if salario_bruto >= 1500 and salario_bruto <= 2500:
    desco_ten = salario_bruto - (salario_bruto * 0.1)

    print('Seu saláro liquido com todos os descontos é {}'.format(desco_ten))
    print('Total de descontos: {}'.format((salario_bruto * 0.1)))
    print('Descontos de 10%')

elif salario_bruto >= 2500:
    desco_vint = salario_bruto - (salario_bruto * 0.2)

    print('Seu salário liquido com todos os descontos é {}'.format(desco_vint))
    print('Total de descontos : {}'.format((salario_bruto * 0.2)))
    print('Descontos de 20%')

print('='*50)
