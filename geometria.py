"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

    Possua uma classe chamada Ponto, com os atributos x e y.
    Possua uma classe chamada Retangulo, com os atributos largura e altura.
    Possua uma função para imprimir os valores da classe Ponto
    Possua uma função para encontrar o centro de um Retângulo.
    Você deve criar alguns objetos da classe Retangulo.
    Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
    A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
    O valor do centro do objeto deve ser mostrado na tela
    Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

from math import sqrt

class Ponto:
    # Criando as coordenadas
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Distancia a origem
    def modulo(self):
        return sqrt((self.x ** 2) + (self.y ** 2))
    
    # Mostrando o ponto
    def mostraPonto(self):
        print(f"Abiscissa: {self.x} | Ordenada: {self.y}")
    
    # Obtendo a abscissa e a ordenada
    def abscissa(self):
        return self.x

    def ordenada(self):
        return self.y
    
    # Modificando o ponto
    def setAbscissa(self, ab):
        self.x = ab
    
    def setOrdenada(self, co):
        self.y = co
    
    # Representacao do ponto
    def __repr__(self):
        return f"{self.x},{self.y}"


class Retangulo:
    # Principais atributos
    def __init__(self, base, altura, pto = Ponto(0, 0)):
        self.altura = altura
        self.base = base
        self.pto = pto

    def centro(self):
        # Abscissa do centro - ((x + base) + x)/2, em que x eh a abscissa do ponto inferior esquerdo
        x_centro = ((self.pto.abscissa() + self.base) + self.pto.abscissa()) / 2

        # Ordenada do centro - ((y + ordenada) + y)/2, em que y eh a ordenada do ponto inferior esquerdo
        y_centro = ((self.pto.ordenada() + self.altura) + self.pto.ordenada()) / 2

        return Ponto(x_centro, y_centro)
    
    # Modificar alguns valores
    def setAltura(self, altura):
        self.altura = altura
    
    def setBase(self, base):
        self.base = base
    
    def setPonto(self, ab, co):
        self.pto.setAbscissa(ab)
        self.pto.setOrdenada(co)


base = float(input("Base do triangulo: "))
altura = float(input("Altura do triangulo: "))

ab = float(input("Abscissa do ponto inferior esquerdo: "))
co = float(input("Ordenada do ponto inferior esquerdo: "))

figura = Retangulo(base, altura, Ponto(ab, co))

# Criando um menu
control = ""
numero = 0
x = 0
y = 0

while control.upper() != "FIM":
    control = input("Alrerar base; Alterar altura; Alterar origem; Mostrar o centro; | FIM: ")

    if control.upper() == "ALTERAR BASE":
        numero = float(input("Qual o valor da base: "))
        figura.setBase(numero)
    elif control.upper() == "ALTERAR ALTURA":
        numero = float(input("Qual o valor da altura: "))
        figura.setAltura(numero)
    elif control.upper() == "ALTERAR ORIGEM":
        x = int(input("Abscissa: "))
        y = int(input("Ordenada: "))
        figura.setPonto(x, y)
    elif control.upper() == "MOSTRAR CENTRO":
        print(figura.centro())
    elif control.upper() != "FIM":
        print("Invalido")
    
    print("\n")


