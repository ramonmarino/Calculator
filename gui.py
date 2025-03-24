import tkinter as tk
from calculator import *  # Supondo que suas funções de calculadora estão nesse arquivo


# Função para manipular os cliques de operação
def calcular(operacao):
    try:
        num1 = float(entry_num1.get())  # Obtém o primeiro número da entrada
        num2 = float(
            entry_num2.get()) if operacao != 'Raiz' else None  # Segundo número (não precisa para operações como Raiz)

        if operacao == 'Somar':
            resultado = somar(num1, num2)
        elif operacao == 'Subtrair':
            resultado = subtrair(num1, num2)
        elif operacao == 'Multiplicar':
            resultado = multiplicar(num1, num2)
        elif operacao == 'Dividir':
            resultado = div(num1, num2)
        elif operacao == 'Raiz':
            resultado = raiz(num1)
        # Adicione mais operações conforme necessário

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro! Entrada inválida.")


# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Criando widgets (elementos da interface)
label_num1 = tk.Label(root, text="Primeiro número:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Segundo número (se necessário):")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Botões de operação
botao_somar = tk.Button(root, text="Somar", command=lambda: calcular('Somar'))
botao_somar.pack()

botao_subtrair = tk.Button(root, text="Subtrair", command=lambda: calcular('Subtrair'))
botao_subtrair.pack()

botao_multiplicar = tk.Button(root, text="Multiplicar", command=lambda: calcular('Multiplicar'))
botao_multiplicar.pack()

botao_dividir = tk.Button(root, text="Dividir", command=lambda: calcular('Dividir'))
botao_dividir.pack()

botao_raiz = tk.Button(root, text="Raiz Quadrada", command=lambda: calcular('Raiz'))
botao_raiz.pack()

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Resultado:")
label_resultado.pack()

# Inicia a interface
root.mainloop()
