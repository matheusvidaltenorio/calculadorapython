
from cal_functions import *

def main():
    while True:
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        choice = input("Digite a opção (1/2/3/4/5): ")

        if choice == '5':
            print("Saindo...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print("Resultado:", add(num1, num2))
        elif choice == '2':
            print("Resultado:", subtract(num1, num2))
        elif choice == '3':
            print("Resultado:", multiply(num1, num2))
        elif choice == '4':
            print("Resultado:", divide(num1, num2))
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
