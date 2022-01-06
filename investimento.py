"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""

class contaInvestimento:
    
    # Modelando a classe
    def __init__(self, numero: str, nome, taxaJuros, saldo = 0.0):
        self._numero = numero
        self._nome = nome
        self.taxa = taxaJuros
        self._saldo = saldo
    
    def alterarNome(self, nome):
        self._nome = nome
    
    def deposito(self, quantia):
        if quantia <= 0:
            print("Impossivel realizar este deposito")
            return
        self._saldo += quantia
    
    def saque(self, quantia):
        if quantia <= 0:
            print("Impossivel realizar o saque")
            return
        self._saldo -= quantia
    

    def adicioneJuros(self):
        self._saldo *= (1 + self.taxa)
    
    def dados(self):
        print("\n\n--------------------------------------")
        print("Nome do cliente: {}".format(self._nome))
        print("Numero da conta: {}".format(self._numero))
        print("Saldo em banco : {:.2f} R$".format(self._saldo))
        print("--------------------------------------\n\n")


conta = contaInvestimento("12345678", "Jose", 0.01, 10000)

for i in range(5):
    conta.adicioneJuros()

conta.dados()


