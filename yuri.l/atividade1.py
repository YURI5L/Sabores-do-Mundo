def verificar_maioridade(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} não é maior de idade."

def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    resultado = verificar_maioridade(nome, idade)
    print(resultado)

if __name__ == "__main__":
    main()
