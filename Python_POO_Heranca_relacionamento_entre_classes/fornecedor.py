import pessoa
class Fornecedor(pessoa.Pessoa):
    def __init__(self, cpf, nome, valorCredit, valorDivid):
        super().__init__(cpf, nome)
        self.__valorCredit = valorCredit
        self.__valorDivid = valorDivid
        
    def obterSaldo(self):
        saldoDivida = self.valorDivid-self.valorCredit
        return saldoDivida