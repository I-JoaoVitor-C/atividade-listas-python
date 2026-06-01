# EXERCÍCIO 3

# Exemplo de list comprehension:
# quadrados = [x**2 for x in range(10)]
 
palavras = ['python', 'lista', 'programação', 'código', 'loop', 'função']
numeros = list(range(1, 21))  # 1 até 20

# ↓ 3.1 Use list comprehension para criar uma lista com os quadrados de 1 a 10.
quadrados = [x**2 for x in range(1, 11)]
print(quadrados)

# ↓ 3.2 Use list comprehension para filtrar apenas os números pares da lista numeros.
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# ↓ 3.3 Crie uma lista com o comprimento (len) de cada palavra em palavras.
comprimento = [len(p) for p in palavras]
print(comprimento)

# ↓ 3.4 Crie uma lista com as palavras de palavras que tenham mais de 5 letras, em maiúsculas.
maior_que_5l = [p.upper() for p in palavras if len(p) > 5]
print(maior_que_5l)

# ↓ 3.5 Crie uma lista de tuplas (número, quadrado) para números de 1 a 5.
num_quad = [(x, x**2) for x in range(1, 6)]
print(num_quad)