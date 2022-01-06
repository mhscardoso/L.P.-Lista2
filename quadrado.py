"""
    Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:

    def __init__(self, lado) -> None:
        self.lado = lado
    
    def mudaLado(self, lado):
        self.lado = lado
    
    def mostraLado(self):
        return self.lado
    
    def calculaArea(self):
        return self.lado ** 2


