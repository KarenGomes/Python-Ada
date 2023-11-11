# DICIONÁRIOS

#criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Karen', 'idade': 19, 'altura': 1.53 }

print(dicionario['idade'])

#adicionando elementos 

dicionario['programador'] = True

print(dicionario)

#se o conteúdo já existir, irá sobrescrever 

#iterando 

for chave in dicionario:
    print(chave, dicionario[chave])

#testando a existência de uma chave 

print('peso' in dicionario)
print('altura' in dicionario)