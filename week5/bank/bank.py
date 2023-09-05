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
def main():
    greet = (input("Greeting: ")).lower().strip()
    print(f"${value(greet)}")


#usamos esse método para verificar se a saudação do usuário começa com a letra h
#ignorando espaços em branco e diferenças de maiúsculas e minúsculas.
def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
