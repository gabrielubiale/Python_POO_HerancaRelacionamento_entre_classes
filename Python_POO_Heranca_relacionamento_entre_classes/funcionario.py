import pessoa
class Funcionario(pessoa.Pessoa):
    def __init__(self, cpf, nome, setor, salario):
        self.__setor = setor
        self.__salario = salario

    def mostraDados(self):
        return super().mostraDados()+" "+self.getSetor()

    def getSetor(self):
        return self.__setor