import funcionario
class Vendedor(funcionario.Funcionario):
    def __init__(self, cpf, nome, setor, salario, valorDeVenda, comissao):
        super().__init__(cpf, nome, setor, salario)
        self.__valorDeVenda = valorDeVenda
        self.__comissao = comissao

    def calcularComissao(self, valorDeVenda, comissao):
        valorComissao = self.valorDeVenda*self.comissao
        return valorComissao