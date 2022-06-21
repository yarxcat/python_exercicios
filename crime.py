print('=' * 30)
print('Entrevistando um suspeito')
print('=' * 30)
print('Responda "S" para SIM e "N" para NÂO.')
print('-' * 30)

classifica = 0

q1 = input('Telefonou para a vitima? ').upper()
q2 = input('Esteve no local do crime? ').upper()
q3 = input('Morava perto da vitima? ').upper()
q4 = input('Devia para a vitima? ').upper()
q5 = input('Já trabalhou para a vitima? ').upper()

if q1 == 'S':
    classifica += 1

if q2 == 'S':
    classifica += 1

if q3 == 'S':
    classifica += 1

if q4 == ' S':
    classifica += 1

if q5 == 'S':
    classifica += 1

if classifica < 2:
    print('Inocente')
elif classifica == 2:
    print('Suspeito')

if classifica >= 3 and classifica <= 4:
    print('Cumplice')
elif classifica == 5:
    print('Assassino')
