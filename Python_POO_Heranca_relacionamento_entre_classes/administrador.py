import funcionario
class Admintrador(funcionario.Funcionario):
    def __init__(self, cpf, nome, setor, salario, ajudaDeCusto):
        super().__init__(self, nome, setor, salario)
        self.__ajudaDeCusto = ajudaDeCusto