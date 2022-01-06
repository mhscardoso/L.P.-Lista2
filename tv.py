"""
    Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class Televisor:

    def __init__(self, canal: str, volume: int) -> None:
        self._canal = canal
        self._volume = volume
    

    def mudarCanal(self, canal_novo):
        if canal_novo == self._canal:
            print("A TV ja esta neste canal")
            return        
        self._canal = canal_novo

    
    def aumentaVolume(self, aumento):
        if aumento <= 0:
            print("Dado invalido")
            return
        elif self._volume + aumento > 100:
            print("O volume da TV se limita no intervalo de 0 a 100")
            self._volume = 100
            return

        self._volume += aumento
    

    def diminuiVolume(self, diminuicao):
        if diminuicao <= 0:
            print("Dado invalido")
            return
        elif self._volume - diminuicao < 0:
            print("O volume da TV se limita no intervalo de 0 a 100")
            self._volume = 0
            return
        
        self._volume -= diminuicao


    def dados(self):
        print("A TV esta no canal {} com volume {}".format(self._canal, self._volume))
    

