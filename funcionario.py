"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
"""

class Funcionario:
    
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
    

    def setNome(self, nome):
        self.nome = nome
    
    def setSalario(self, salario):
        self.salario = salario
    
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario


fun = Funcionario("Irineu", 5600)
print(fun.getNome())
print(fun.getSalario())

fun.setNome("Irineia")
fun.setSalario(6200)

print(fun.getNome())
print(fun.getSalario())



