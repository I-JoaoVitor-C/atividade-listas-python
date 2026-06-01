# EXERCÍCIO 2

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# ↓ 2.1 Extraia os 4 primeiros elementos da lista.
for i in letras[:4]:
  print(i)
print(letras[:4])

# ↓ 2.2 Extraia do 3º ao 7º elemento (inclusive).
print(letras[2:7])

# ↓ 2.3 Extraia os 3 últimos elementos usando slicing.
print(letras[-3:])

# ↓ 2.4 Crie uma cópia invertida da lista completa usando slicing.
letras_invertidas = letras[::-1]
print(letras_invertidas)

# ↓ 2.5 Extraia apenas os elementos de índice par (0, 2, 4, ...) usando o passo no slicing.
print(letras[::2])