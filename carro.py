"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

    Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
    O consumo é especificado no construtor e o nível de combustível inicial é 0.
    Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
    Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
    meuFusca.andar(100);            # anda 100 quilômetros.
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""

class Carro:

    # Modelando a classe
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
    
    # Getters
    def obterGasolina(self):
        print("Nivel de gasolina: {:.2f}".format(self.combustivel))
        return self.combustivel
    
    def obterConsumo(self):
        print("Consumo do veiculo: {} km/L".format(self.consumo))
        return self.consumo
    
    # Setter
    def adicionarGasolina(self, litros):
        self.combustivel += litros
    
    # Andar
    def andar(self, dist):
        consumido = dist / self.consumo
        if self.combustivel - consumido < 0:
            print("Pude andar apenas {:.2f} km.".format(self.consumo * self.combustivel))
            print("O VEICULO NAO POSSUI COMBUSTIVEL")
            self.combustivel = 0
            return
        
        self.combustivel -= consumido
        print("Andei os {:.2f} km e tenho {:.2f} L de combustivel sobrando.".format(dist, self.combustivel))

    
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.


