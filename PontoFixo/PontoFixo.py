import os  # Usado para limpara a tela
# -----------------------------------------------------------------------------
# Classe PontoFixo


class CPontoFixo():
    erro = 0.001

    def __init__(self):
        os.system('cls')
        print("----------")
        print("Ponto Fixo")
        print("----------")

    def ObtemChuteInicial(self):
        return float(input("Digite um valor de chute inicial: "))

    def modulo(self, x):
        if (x < 0):
            return (-1)*x
        else:
            return x

    def CalculaResultado(self, x0):

        x = self.g(x0)
        condicaoParada = self.modulo(x - x0)
        # Verifica a condição de parada
        if (condicaoParada < self.erro):
            return x
        else:
            return self.CalculaResultado(x)

    def g(self, x0):
        return (x0+1) ** (1/3)


# -----------------------------------------------------------------------------
# Função Principal


def main():
    pontoFixo = CPontoFixo()  # Cria instância da classe Ponto Fixo
    x0 = pontoFixo.ObtemChuteInicial()
    resultado = pontoFixo.CalculaResultado(x0)
    print(resultado)


# -----------------------------------------------------------------------------
# Chama Programa Principal
main()
