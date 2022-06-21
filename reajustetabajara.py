print('Calculando seu reajuste salárial na Tabajra')
print('-' * 20)

salarioAt = int(input('Digite seu salário atual em R$: '))

if salarioAt <= 280:
    print("""Salario antes do reajuste: {}
          O percentual de aumento aplicado: {}
          O valor aumentado: {}
          O novo salário: {}""".format(salarioAt, '20%', (salarioAt * 0.2), (salarioAt * 0.2) + salarioAt))

elif salarioAt <= 280 or salarioAt <= 700:
    print("""Salario antes do reajuste: {}
        o percentual  de aumento aplicado: {}
        O valor aumentado: {}
        O novo salário: {}""".format(salarioAt, '15%', (salarioAt * 0.15), (salarioAt * 0.15) + salarioAt))

if salarioAt <= 700 or salarioAt <= 1500:
    print("""Salario antes do reajuste: {}
          o percentual  de aumento aplicado: {}
          O valor aumentado: {}
          O novo salário: {}""".format(salarioAt, '10%', (salarioAt * 0.1), (salarioAt * 0.1) + salarioAt))

if salarioAt > 1500 :
    print("""Salario antes do reajuste: {}
            o percentual  de aumento aplicado: {}
            O valor aumentado: {}
            O novo salário: {}""".format(salarioAt, '5%', (salarioAt * 0.05), (salarioAt * 0.05) + salarioAt))

