"""
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
"""

class Tamagushi:

    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._fome = 0
        self._saude = 100
        self._idade = 0

    def getNome(self):
        return self._nome
    
    def getFome(self):
        return self._fome

    def getSaude(self):
        return self._saude
    
    def getIdade(self):
        return self._idade

    def setNome(self, nome):
        self._nome = nome

    def setFome(self, fome):
        self._fome = fome
        
    def setSaude(self, saude):
        self._saude = saude

    def setIdade(self, idade):
        self._idade = idade

    def calculaHumor(self):
        return (self._saude/(self._fome + 1))

    def mostraTamagushi(self):
        print("Nome: {}".format(self._nome))
        print("Idade: {}".format(self._idade))
        print("Fome: {}".format(self._fome))
        print("Saude: {}".format(self._saude))
        print("Humor: {}".format(self.calculaHumor()))


