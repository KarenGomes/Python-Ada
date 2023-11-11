#função inicial 

def saudacao():
    print('seja bem-vindo(a)')
    print('Olá, é um prazer ter você fazendo parte desse curso')

saudacao()

#funcao com parâmetros e parâmetro com default

def saudacao(nome, curso='Python'):
    print(f'seja bem-vindo(a) {nome}')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('Karen')

saudacao('Karen', 'C++')

#função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print(f'O resultado da soma é {resultado}')

#exemplo:

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    else:
        return num1 - num2
    
print(calculadora(10, 20))

