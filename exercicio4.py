# EXERCÍCIO 4

notas = [7.5, 8.0, 6.0, 9.5, 5.5, 8.5, 7.0, 9.0, 6.5, 8.0]
nomes = ['Carlos', 'Ana', 'Bruno', 'Ana', 'Diego', 'Ana', 'Bruno']

# ↓ 4.1 Calcule a média das notas usando sum() e len(). Imprima o resultado formatado com 2 casas decimais.
media = sum(notas)/len(notas)
print(f'Média: {media:.2f}')

# ↓ 4.2 Encontre a maior e menor nota usando as funções adequadas e mostre quantos alunos estão acima da média.
maior_nota = max(notas)
menor_nota = min(notas)
print(f'Maior nota: {maior_nota}')
print(f'Menor nota: {menor_nota}')
print(f'Alunos acima da média: {len([x for x in notas if x > media])}')


# ↓ 4.3 Conte quantas vezes 'Ana' aparece na lista nomes.
print(f"Ana aparece {nomes.count('Ana')} vezes.")


# ↓ 4.4 Encontre o índice da primeira ocorrência de 'Bruno' em nomes.
print(f"Bruno aparece pela primeira vez no índice {nomes.index('Bruno')}.")


# ↓ 4.5 Crie uma lista com nomes sem repetição (sem usar set), mantendo a ordem de primeira aparição.
nomes_sem_repeticao = []
for nome in nomes:
    if nome not in nomes_sem_repeticao:
        nomes_sem_repeticao.append(nome)
print(f'Nomes sem repetição: {nomes_sem_repeticao}')