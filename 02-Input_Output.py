a = 'bom dia'
x = input (a  +' Qual é o seu nome? ') 
print ('Olá,', x)
y = input ('Qual é a sua idade? ')
print (x, 'você tem', y, 'anos')


print('Olá ', input('Qual é o seu nome? '), ', seja bem-vindo!', sep='')

# a função input recebe um argumento que é a mensagem que vai ser mostrada ao utilizador
# a função print recebe um ou mais argumentos e os imprime
# no input sóa recebe um parametro, no print pode receber vários parâmetros, separados por vírgula
# no input o resultado sempre é uma string, e se quiser apreensentar 2 args preciso concatemar com o operador +