def verificar_intervalo(numero):
    if 10 <= numero <= 99:
        return True
    else:
        return False

def main():
    numero = int(input("Digite um número: "))

    if verificar_intervalo(numero):
        print("O número está entre 10 e 99.")
    else:
        print("O número não está entre 10 e 99.")

if __name__ == "__main__":
    main()
