from CInterface import CInterface
from CMatriz import CMatriz

# --------------------------------------------------------------------------------------
# Função Principal
# --------------------------------------------------------------------------------------


def main():
    interface = CInterface()
    interface.mostra_titulo("Sistemas Lineares")

    matrix = CMatriz('[2 3 1 1; 4 7 4 3; 4 7 6 4; 6 9 9 8]')
    matrix.mostraMatrixA()
    matrix.mostraMatrixL()


# --------------------------------------------------------------------------------------
# Chama Programa Principal do jogo. Ponto de Entrada da aplicação
# --------------------------------------------------------------------------------------
main()
