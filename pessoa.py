"""
    Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
# Modelagem da classe pessoa
class Pessoa:

    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
    
    def envelhecer(self, anos_passados):
        idade_antiga = self._idade
        self._idade += anos_passados
        anos_considerados = 0
        
        if self._idade <= 21 and idade_antiga < 21:
            anos_considerados = anos_passados
        elif self._idade > 21 and idade_antiga < 21:
            anos_considerados = anos_passados - (self._idade - 21)
        else:
            anos_considerados = 0
        
        self._altura += 0.5 * anos_considerados
    
    def engordar(self, peso):
        if peso <= 0:
            print("Para emagrecer, utilize a funcao EMAGRECER")
            return
        
        self._peso += peso
    
    def emegrecer(self, peso):
        if peso <= 0:
            print("Para engordar, utiliza a funcao ENGORDAR")
            return
        
        if self._peso - peso <= 0:
            print("Isso nao faz sentido")
            return
        
        self._peso -= peso
    
    def crescer(self, tamanho):
        d = ""
        if tamanho > 100:
            d = input("Tem certeza que cresceu mais de 100 cm? (S/n) ")
            if d in "Ss":
                self._altura += tamanho
            else:
                return
        elif tamanho < 0:
            print("Dado incongruente")
            return
        else:
            self._altura += tamanho


# Pedindo os dados da pessoa
print("------------ Diario da sua vida -------------")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: (kg) "))
altura = float(input("Digite sua altura: (cm) "))

# Criando a pessoa
pessoa = Pessoa(nome, idade, peso, altura)

print("\n\n")

# Lista de possiveis decisoes
decisoes = ["ENVELHECER", "ENGORDAR", "EMAGRECER", "CRESCER", "FIM"]
decisao = ""

# Loop infinito
while decisao != "FIM":

    # Mostrando as decisoes possiveis
    print("Decisoes: ", end="")
    for d in decisoes:
        print(d, end=" | ")
    print()

    decisao = input("Escolha uma decisao acima: ")
    if decisao.upper() not in decisoes:
        print("Escolha apenas alguma dessas decisoes")
        continue

    decisao = decisao.upper()

    if decisao == decisoes[0]:
        # Caso envelhecer
        anos_acrescidos = int(input("Quantos anos voce envelheceu? "))
        pessoa.envelhecer(anos_acrescidos)
        print("A sua idade eh: {} e com isso, sua altura eh {} cm.".format(pessoa._idade, pessoa._altura), end="\n\n")
    elif decisao == decisoes[1]:
        # Caso engordar
        peso_acrescido = float(input("Quanto voce engordou? (kg) "))
        pessoa.engordar(peso_acrescido)
        print("Seu peso eh: {}".format(pessoa._peso), end="\n\n")
    elif decisao == decisoes[2]:
        # Caso emagrecer
        peso_decrescido = float(input("Quanto voce emagreceu? (kg) "))
        pessoa.emegrecer(peso_decrescido)
        print("Seu peso eh: {}".format(pessoa._peso), end="\n\n")
    elif decisao == decisoes[3]:
        # Caso crescer
        tamanho_aumentado = float(input("Quanto voce cresceu? (cm) "))
        pessoa.crescer(tamanho_aumentado)
        print("A sua altura eh de: {} cm".format(pessoa._altura), end="\n\n")
    else:
        continue



