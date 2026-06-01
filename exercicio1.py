#EXERCÍCIO 1


frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
numeros = [10, 25, 3, 47, 8, 15, 30]


# ↓ 1.1 Imprima o primeiro e último item da lista sem usar índices negativos e depois usando índice negativo
primeiro_positivo = frutas[0]
print(primeiro_positivo)
ultimo_positivo = frutas[len(frutas)-1]
print(ultimo_positivo)

primeiro_negativo = frutas[-len(frutas)]
ultimo_negativo = frutas[-1]
print(primeiro_negativo)
print(ultimo_negativo)


# ↓ 1.2 Adicione 'morango' ao final de frutas e insira 'kiwi' na posição 2.
frutas.append('morango')
frutas.insert(2, 'kiwi')
print(frutas)


# ↓ 1.3 Remova 'banana' da lista frutas usando o método adequado.
frutas.pop(1)
print(frutas)


# ↓ 1.4 Percorra a lista numeros com um for e imprima apenas os números maiores que 15.
for i in numeros:
  if i > 15:
    print(i)


# ↓ 1.5 Imprima a lista numeros em ordem crescente e decrescente (sem modificar a lista original).
numeros_crescentes = sorted(numeros)
print(numeros_crescentes)
numeros_decrescentes = sorted(numeros, reverse=True)
print(numeros_decrescentes)
