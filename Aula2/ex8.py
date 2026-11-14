try:
    numero = int(input("Digite um número: "))
    print("Você digitou:", numero)
except ValueError:
    print("Valor inválido")