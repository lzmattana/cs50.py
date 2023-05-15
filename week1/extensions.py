"""
Run your program with python extensions.py. Type happy.jpg and press Enter. Your program should output:
image/jpeg
Run your program with python extensions.py. Type document.pdf and press Enter. Your program should output:
application/pdf

Este código primeiro recebe o nome do arquivo como entrada do usuário.
Em seguida, ele verifica se o nome do arquivo termina com um dos sufixos especificados,
usando o método endswith() da string. O método lower() é usado para transformar o nome do arquivo em minúsculas,
para que possamos verificar os sufixos sem levar em conta o caso.
"""

file = input("File name: ")
if nome_arquivo.lower().endswith(('.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip')):
    if nome_arquivo.lower().endswith('.gif'):
        print("image/gif")
    elif nome_arquivo.lower().endswith(('.jpg', '.jpeg')):
        print("image/jpeg")
    elif nome_arquivo.lower().endswith('.png'):
        print("image/png")
    elif nome_arquivo.lower().endswith('.pdf'):
        print("application/pdf")
    elif nome_arquivo.lower().endswith('.txt'):
        print("text/plain")
    elif nome_arquivo.lower().endswith('.zip'):
        print("application/zip")
else:
    print("Not supported.")