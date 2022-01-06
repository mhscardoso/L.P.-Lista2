"""
    Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

"""

class Conta:
    
    # Modelando a classe
    def __init__(self, numero: str, nome, saldo = 0.0):
        self._numero = numero
        self._nome = nome
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
    
    def dados(self):
        print("\n\n--------------------------------------")
        print("Nome do cliente: {}".format(self._nome))
        print("Numero da conta: {}".format(self._numero))
        print("Saldo em banco : {} R$".format(self._saldo))
        print("--------------------------------------\n\n")

# Criando a classe conta
print("CRIE UMA CONTA NO BANCO LP")
nome = input("Digite seu nome: ")
numero = input("Qual o numero da conta: ")
dinheiro = input("Quantia atual: ")

conta = 0

if not dinheiro:
    conta = Conta(numero, nome)
else:
    dinheiro = float(dinheiro)
    conta = Conta(numero, nome, dinheiro)

opcoes = ["MUDAR NOME", "DEPOSITAR", "SACAR", "DADOS", "TERMINAR"]
opcao = ""

while opcao != opcoes[4]:
    # Mostrando as opcoes
    for op in opcoes:
        print(op, end = " | ")
    print()

    opcao = input("Escolha uma opcao acima: ")
    opcao = opcao.upper()

    if opcao not in opcoes:
        print("Opcao invalida")
        continue
    
    if opcao == opcoes[0]:
        # Mudar o nome
        novo_nome = input("Qual seu nome? ")
        conta.alterarNome(novo_nome)
    elif opcao ==  opcoes[1]:
        # Depositar
        quantia = float(input("Qual a quantia para depositar? "))
        conta.deposito(quantia)
    elif opcao == opcoes[2]:
        # Sacar
        quantia = float(input("Qual a quantia para sacar? "))
        conta.saque(quantia)
    elif opcao == opcoes[3]:
        # Mostrar dados
        conta.dados()

