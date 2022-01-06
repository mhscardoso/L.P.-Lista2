"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.)
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


print("Bem vindo ao mundo do seu bichinho virtual!")
nome = input("Escolha um nome para seu Tamagushi: ")
tg = Tamagushi(nome)
tg.mostraTamagushi()


