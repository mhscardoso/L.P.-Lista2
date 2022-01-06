"""
    Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo:

    def __init__(self, comprimento, largura) -> None:
        self.comprimento = comprimento
        self.largura = largura

    def mudaComprimento(self, comprimento):
        self.comprimento = comprimento
    
    def mudaAltura(self, largura):
        self.largura = largura
    
    def mostraLados(self):
        return f"Este retangulo tem um comprimento de {self.comprimento} e largura de {self.largura}."
    
    def calculaPerimetro(self):
        return (self.comprimento + self.largura) * 2
    
    def calculaArea(self):
        return self.comprimento * self.largura

print("Logistica de Pisos\n")
comprimento = float(input("Qual o comprimento do local? "))
largura = float(input("Qual a largura do local? "))

local = Retangulo(comprimento, largura)
print(local.mostraLados())
print(f"Perimetro do local (tamanho do rodape): {local.calculaPerimetro()}")
print("Area do local: {}".format(local.calculaArea()))

azulejo = input("Qual a area do azulejo? ")
azulejo = float(azulejo)
print("Azulejos necessarios: {}".format(local.calculaArea() / azulejo))
