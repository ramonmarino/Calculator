from calculator import *  # chamando todas as funções.

# Dicionário de operações
operacoes = {
    1: somar,
    2: subtrair,
    3: multiplicar,
    4: div,
    5: raiz,
    6: potencia,
    7: modulo,
    8: fatorial,
    9: logaritmo,
    10: absoluto,
    11: arredondar,
    12: raiz_n
}

# Loop para continuar até o usuário digitar 0
while True:
    # Exibe o menu de opções
    print("\nMENU DE ESCOLHA")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Raiz Quadrada")
    print("6 - Potência")
    print("7 - Módulo")
    print("8 - Fatorial")
    print("9 - Logaritmo")
    print("10 - Valor Absoluto")
    print("11 - Arredondar")
    print("12 - Raiz N")
    print("0 - Sair\n")

    # Solicita a escolha do usuário do menu
    chosen_number = int(input("Escolha um número de 1 a 12 ou 0 para sair: "))

    if chosen_number in operacoes:
        number_one = float(input("Digite o primeiro número: "))

        # Algumas operações não necessitam de segundo número
        if chosen_number not in [5, 8, 10, 11]:
            number_two = float(input("Digite o segundo número: "))
            resultado = operacoes[chosen_number](number_one, number_two)
            operacao_str = f"{number_one} {chosen_number} {number_two} = {resultado}"
        else:
            resultado = operacoes[chosen_number](number_one)
            operacao_str = f"{chosen_number}({number_one}) = {resultado}"

        # Exibe o resultado da operação
        print(f"Resultado: {resultado}")

        # Salva no arquivo TXT
        with open("historico.txt", "a") as file:
            file.write(operacao_str + "\n")

# Caso o usuário escolha sair, o loop é quebrado
    if chosen_number == 0:
        print("Saindo...")
        break
