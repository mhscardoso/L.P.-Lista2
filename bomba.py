"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    tipoCombustivel.
    valorLitro
    quantidadeCombustivel
    Possua no mínimo esses métodos:
    abastecerPorValor( ) - método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    abastecerPorLitro( ) - método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    alterarValor( ) - altera o valor do litro do combustível.
    alterarCombustivel( ) - altera o tipo do combustível.
    alterarQuantidadeCombustivel( ) - altera a quantidade de combustível restante na bomba.
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

class bombaCombustivel:
    
    # Modelando a classe
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel = 1000):
        self.tipoCompustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    # Obter os valores
    def getTipo(self):
        return self.tipoCompustivel

    def getValor(self):
        return self.valorLitro

    def getQtd(self):
        return self.quantidadeCombustivel
    
    
    # Alterar os valores
    def setTipo(self, novoTipo):
        self.tipoCompustivel = novoTipo

    def setValor(self, novoValor):
        self.valorLitro = novoValor

    def setQtd(self, novoQtd):
        self.quantidadeCombustivel = novoQtd
    

    # Abastecer o carro
    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        self.quantidadeCombustivel -= litros
        print("Serao adicionados {} litros de {} ao veiculo.".format(litros, self.tipoCompustivel))
    
    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        print("Os {} litros de {} valem {}R$.".format(litros, self.tipoCompustivel, valor))
    
    # Mostrando todos os dados
    def mostraBomba(self):
        print("---------------------------------")
        print(f"Tipo:            {self.getTipo()}")
        print(f"Valor por Litro: {self.getValor()}")
        print(f"Quantidade:      {self.getQtd()}")
        print("---------------------------------")


bomba1 = bombaCombustivel("Alcool", 7.05)           # Valor padrao para a bomba
bomba2 = bombaCombustivel("Gasolina", 7.95, 3000)   # Valor diferente do padrao


# Para a bomba 1
print("Bomba 1")
bomba1.mostraBomba()
bomba1.setQtd(2000)
bomba1.mostraBomba()


# Para a bomba 2
print("Bomba 2")
bomba2.mostraBomba()
bomba2.setTipo("Gasolina Aditivada")
bomba2.mostraBomba()
bomba2.setValor(8.1)
bomba2.mostraBomba()
