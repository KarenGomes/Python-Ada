nota1= 7.9
nota2 = 9.7
nota3 = 8.2

notas = [nota1, nota2, nota2]

#criando listas 

lista = []
lista2 = list()
lista3 = [25, 'nome', False]
lista_de_listas = [10, [1,2,3]]

#índice

print(lista3[1])

#slice

lista = [10, 50, 30, 40, 25]
print(lista[0:3]) #de 0 até 3
print(lista[2:]) #2 até o final 


for elemento in lista:
    print(elemento)

#comprimento 

print('comprimento da lista ', len(lista))

for i in range(len(lista)):
    print(lista[i])

# > METODOS DE LISTA


lista = [1, 3, 12, 8, 2]

#append 

print('antes do append: ', lista)

lista.append(3)

print('depois do append', lista)

#insert 

lista.insert(2, 10)

print('depois do insert', lista)

#extend 

lista2 = [1,2,3]

lista.extend(lista2)

print('depois do extend', lista)

#pop

lista.pop()

print('Lista após o pop', lista)

lista.pop(0)

print('Lista após o pop indice 0', lista)

#remove 

lista.remove(3) #remove o elemento 

print('Depois de remove', lista)

#count 

print('quantidade de 2 na lista: ', lista.count(2))

#index

print('indice do elemento 12: ', lista.index(12))

#sort

lista.sort()

print('lista ordenada: ', lista)

lista.sort(reverse=True)

print('Lista reversa', lista)

# FUNÇÕES PARA LISTAS 

#len

print(len(lista))

#sum 

print(sum(lista)) #soma todos os elementos da lista

#max

print('maior elemento da lista', max(lista))

#min

print('menor elemento da lista', min(lista))



