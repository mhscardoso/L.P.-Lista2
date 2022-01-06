"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

class Macaco:
    
    # Atributos: nome e bucho
    def __init__(self, nome = "") -> None:
        self.nome = nome
        self.bucho = []
    
    # Adiciona a comida a lista, que representa o estomago
    def comer(self, comida):
        self.bucho.append(comida)
    
    # Visualiza o que tem no estomago do macado
    def verBucho(self):
        for comida in self.bucho:
            print(comida, end=" | ")
        print()
    
    # Remove alimento do estomago do macaco
    def digerir(self):
        if len(self.bucho) == 0:
            print("Macaco sem comida")
            return
        self.bucho.pop(0)
    
    # Como sera o macaco, representado
    def __repr__(self):
        return f"Macaco {self.nome}"


# Criando os macacos
macaco1 = Macaco("Irineu")
macaco2 = Macaco("Macaco Louco")

# para o macaco 1
print(macaco1)
macaco1.comer("salada")
macaco1.comer("Bife")
macaco1.comer("Banana")

macaco1.verBucho()

macaco1.digerir()

macaco1.verBucho()

print("\n")

# Para o macaco 2
print(macaco2)
macaco2.comer("alface")
macaco2.comer("cenoura")
macaco2.comer("batata liberal")

macaco2.verBucho()

macaco2.digerir()
macaco2.digerir()

macaco2.verBucho()

macaco2.comer(macaco1)

macaco2.verBucho()




