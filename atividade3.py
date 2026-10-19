# Atividade 3 - Ler exame.txt, coletar a nota do exame,
# calcular a nova média e acrescentar o resultado em
# aprovados.txt ou reprovados.txt
import os

nome_arquivo = "exame.txt"

if not os.path.exists(nome_arquivo):
    print(f"O arquivo '{nome_arquivo}' não existe. Execute a atividade 2 primeiro.")
else:
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    if len(linhas) == 0:
        print("Nenhum aluno em exame.")

    for linha in linhas:
        linha = linha.strip()
        if linha == "":
            continue

        nome, media_anterior, _ = linha.split(";")
        media_anterior = float(media_anterior)

        while True:
            try:
                nota_exame = float(input(f"Nota do exame de {nome}: ").replace(",", "."))
                if 0 <= nota_exame <= 10:
                    break
                print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Digite um número válido.")

        media_final = (media_anterior + nota_exame) / 2

        if media_final >= 5:
            with open("aprovados.txt", "a") as aprovados:
                aprovados.write(f"{nome};{media_final:.2f};Aprovado após exame\n")
            print(f"{nome} - Média final: {media_final:.2f} - Aprovado após exame\n")
        else:
            with open("reprovados.txt", "a") as reprovados:
                reprovados.write(f"{nome};{media_final:.2f};Reprovado após exame\n")
            print(f"{nome} - Média final: {media_final:.2f} - Reprovado após exame\n")
