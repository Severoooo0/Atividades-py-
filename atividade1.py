# Atividade 1 - Coletar nome e 3 notas dos alunos e salvar em notas.txt
# Formato de cada linha: nome;nota1;nota2;nota3


def ler_nota(mensagem):
    while True:
        valor = input(mensagem).replace(",", ".")
        try:
            nota = float(valor)
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")


with open("notas.txt", "w") as arquivo:
    while True:
        nome = input("\nNome do aluno (ou ENTER para encerrar): ").strip()
        if nome == "":
            break

        nota1 = ler_nota("Nota 1: ")
        nota2 = ler_nota("Nota 2: ")
        nota3 = ler_nota("Nota 3: ")

        arquivo.write(f"{nome};{nota1};{nota2};{nota3}\n")
        print(f"Dados de {nome} salvos!")

print("\nArquivo notas.txt gerado com sucesso.")
