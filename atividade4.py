# Atividade 4 - Ler aprovados.txt e reprovados.txt e
# imprimir a lista de alunos com sua situação/legenda
import os

for nome_arquivo in ["aprovados.txt", "reprovados.txt"]:
    titulo = nome_arquivo.replace(".txt", "").upper()
    print(f"\n===== {titulo} =====")

    if not os.path.exists(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' não existe.")
        continue

    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    if len(linhas) == 0:
        print("Nenhum aluno.")

    for linha in linhas:
        linha = linha.strip()
        if linha == "":
            continue
        nome, media, situacao = linha.split(";")
        print(f"{nome:<20} Média: {media:>5}   {situacao}")
