#identificando o nome de usuario e a senha

nome = input('Digite um nome de usuario: ').upper()
senha = input('Digite uma senha: ').upper()

while nome != senha:
    print('Usuario registrado!')
    break

while nome == senha:
    print('O nome de usuario nao pode ser igual a senha!! ')
    print('Tente novamente...')
    break
