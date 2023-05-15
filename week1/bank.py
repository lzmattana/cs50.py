"""
Run your program with python bank.py. Type Hello and press Enter. Your program should output:
$0
Run your program with python bank.py. Type Hello, Newman and press Enter. Your program should output:
$0
Run your program with python bank.py. Type How you doing? and press Enter. Your program should output
$20
Run your program with python bank.py. Type What's happening? and press Enter. Your program should output
$100
"""

#A função strip() é usada para remover qualquer espaço em branco no início e no final da entrada do usuário.
#A função lower() é usada para converter a entrada do usuário em letras minúsculas.
greeting = input("Digite uma saudação: ").strip().lower()

#usamos esse método para verificar se a saudação do usuário começa com a letra h
#ignorando espaços em branco e diferenças de maiúsculas e minúsculas.
if greeting == "hello":
    print("$0")
elif greeting.startswith("hello"): # Removido espaço após "hello" para tratar de casos como "hello there"
    print("$0")
elif greeting.startswith("h"):
    if greeting.startswith("hello,"): # Adicionado tratamento para "Hello, Newman"
        print("$0")
    else:
        print("$20")
else:
    print("$100")