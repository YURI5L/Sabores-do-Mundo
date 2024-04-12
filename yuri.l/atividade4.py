
def verificar_maioridade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        return "Você já fez 18 anos neste ano."
    else:
        return "Você fará 18 anos neste ano."

def main():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    resultado = verificar_maioridade(ano_nascimento)
    print(resultado)

if __name__ == "__main__":
    main()
