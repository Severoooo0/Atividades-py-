# Atividade 2 - Ler notas.txt, calcular médias e separar em
# aprovados.txt, exame.txt e reprovados.txt
# Formato de saída: nome;media;situacao
import os

nome_arquivo = "notas.txt"

if not os.path.exists(nome_arquivo):
    print(f"O arquivo '{nome_arquivo}' não existe. Execute a atividade 1 primeiro.")
else:
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    with open("aprovados.txt", "w") as aprovados, \
         open("exame.txt", "w") as exame, \
         open("reprovados.txt", "w") as reprovados:

        for linha in linhas:
            linha = linha.strip()
            if linha == "":
                continue

            nome, n1, n2, n3 = linha.split(";")
            media = (float(n1) + float(n2) + float(n3)) / 3

            if media >= 7:
                aprovados.write(f"{nome};{media:.2f};Aprovado\n")
                situacao = "Aprovado"
            elif media >= 5:
                exame.write(f"{nome};{media:.2f};Exame\n")
                situacao = "Exame"
            else:
                reprovados.write(f"{nome};{media:.2f};Reprovado\n")
                situacao = "Reprovado"

            print(f"{nome} - Média: {media:.2f} - {situacao}")

    print("\nArquivos aprovados.txt, exame.txt e reprovados.txt gerados.")
