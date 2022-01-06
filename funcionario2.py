"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)

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
    
    def aumentarSalario(self, aumento):
        self.salario *= (1 + (aumento / 100))


fun = Funcionario("Irineu", 5600)
fun.aumentarSalario(10)
print(fun.getNome())
print(fun.getSalario())

fun.setNome("Irineia")
fun.setSalario(6200)

fun.aumentarSalario(5)

print(fun.getNome())
print(fun.getSalario())