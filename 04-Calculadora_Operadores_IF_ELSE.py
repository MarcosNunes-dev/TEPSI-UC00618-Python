mensagem = """1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão: \n"""
x = input('Digite o primeiro número: ')
y = input('Digite o segundo número: ')
z =input('Escolha a operação que deseja realizar:'  + mensagem)
if z == '1':
    print(' O resultado da soma dos números é: ', int(x) + int(y))
elif z == '2':
    print(' O resultado da subtração dos números é: ', int(x) - int(y))
elif z == '3':
    print(' O resultado da multiplicação dos números é: ', int(x) * int(y))
else :
    print(' O resultado da divisão dos números é: ', int(x) / int(y))
