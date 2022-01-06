"""
    Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
"""

class Bola:
    
    def __init__(self, cor, circunferencia, material) -> None:
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor) -> None:
        self.cor = cor

    def mostraCor(self) -> str:
        return self.cor


bola = Bola("azul", 50, "borracha")
print(bola.mostraCor())

bola.trocaCor("vermelho")
print(bola.mostraCor())

