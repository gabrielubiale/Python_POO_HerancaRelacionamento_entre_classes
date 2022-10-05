import funcionario
class Operario(funcionario.Funcionario):
    def __init__(self, cpf, nome, setor, salario,valorProducao, comissao):
        super().__init__(cpf, nome, setor, salario)
        self.__valorProducao = valorProducao
        self.__comissao = comissao

    #def calcularSalario(self):