 # EXERCÍCIO 5

# Tabela de notas: cada sublista = [nome, nota1, nota2, nota3]
turma = [
    ['Alice',   8.0, 7.5, 9.0],
    ['Bruno',   6.5, 7.0, 8.0],
    ['Carla',   9.5, 9.0, 9.5],
    ['Diego',   5.0, 6.0, 5.5],
    ['Elena',   7.0, 8.5, 7.5],
]

# 5.1 Imprima o nome e a média de cada aluno, calculando a média das 3 notas.
for linha in turma:
  nome = linha[0]
  notas = linha[1:]
  media = sum(notas)/len(notas)
  print(f'O (A) aluno (a) {nome}, tem a média: {media:.2f}')

# 5.2 Encontre e imprima o nome do aluno com maior média.
melhor_aluno = ""
maior_media = -1

for aluno in turma:
    nome = aluno[0]
    media = sum(aluno[1:]) / 3
   
    # Verifica se esta é a maior média até agora
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome

print(f"O aluno com a maior média é {melhor_aluno} (Média: {maior_media:.2f})")

# 5.3 Imprima a lista de alunos aprovados (média >= 6.0) e reprovados.
aprovados = []
reprovados = []

for aluno in turma:
    nome = aluno[0]
    media = sum(aluno[1:]) / 3
    info_aluno = f"{nome} (Média: {media:.2f})"
    if media >= 6.0:
        aprovados.append(info_aluno)
    else:
        reprovados.append(info_aluno)

print("———ALUNOS—APROVADOS———")
for aluno in aprovados:
    print(f" {aluno}")

print("\n———ALUNOS—REPROVADOS———")
for aluno in reprovados:
    print(f" {aluno}")

# 5.4 Calcule a média geral da turma (média de todas as médias individuais).
soma_medias = 0
for aluno in turma:
    nome = aluno[0]
    media = sum(aluno[1:]) / 3
    soma_medias += media

soma_media_geral = soma_medias/(len(turma))
print(f'Essa é a média geral da turma: {soma_media_geral:.2f}')

# 5.5 Adicione um novo aluno 'Felipe' com notas 8.0, 7.5, 8.5 e re-imprima o ranking da turma em ordem decrescente de média
turma.append(['Felipe', 8.0, 7.5, 8.5])

ranking = []
for aluno in turma:
    nome = aluno[0]
    media = sum(aluno[1:]) / 3
    ranking.append([nome, media])

ranking.sort(key=lambda x: x[1], reverse=True)

print("———RANKING—DA—TURMA——")
for posicao, aluno in enumerate(ranking, start=1):
    print(f"{posicao}º {aluno[0]} - Média: {aluno[1]:.2f}")