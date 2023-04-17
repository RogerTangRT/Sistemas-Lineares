import os


class CInterface():
    # Construtor
    def __init__(self):
        os.system('cls')
    # --------------------------------------------------------------------------------------
    # Nome:         mostra_titulo
    # Descrição:    Mostra o título Jogo da Velha em tela texto
    # Parametros:
    # Retorno:
    # --------------------------------------------------------------------------------------

    def mostra_titulo(self, titulo):
        print("+", "-"*len(titulo), "+")
        print("+", titulo, "+")
        print("+", "-"*len(titulo), "+")
