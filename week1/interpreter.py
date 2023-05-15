"""
Run your program with python interpreter.py. Type 1 + 1 and press Enter. Your program should output:
2.0
Run your program with python interpreter.py. Type 2 - 3 and press Enter. Your program should output:
-1.0
Run your program with python interpreter.py. Type 2 * 2 and press Enter. Your program should output
4.0
Run your program with python interpreter.py. Type 50 / 5 and press Enter. Your program should output
10.0
"""


entrada = input("Digite uma expressão aritmética (exemplo: 1 + 1): ")
x, y, z = entrada.split()

if y == '+':
    resultado = float(x) + float(z)
elif y == '-':
    resultado = float(x) - float(z)
elif y == '*':
    resultado = float(x) * float(z)
elif y == '/':
    resultado = float(x) / float(z)

# usaremos a função print() para exibir o resultado como um número de ponto
# flutuante com uma casa decimal usando o método format().
print("{:.1f}".format(resultado))
