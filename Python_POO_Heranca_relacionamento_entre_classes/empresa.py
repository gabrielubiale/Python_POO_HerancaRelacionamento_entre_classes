from fornecedor import Fornecedor
import funcionario
class Empresa():
    __func = []
    def __init__( self, codigo, nome, endereco, cnpj): 
        self.__codigo = codigo
        self.__nome = nome
        while True:
            print("1 - Contratar:")
            print("2 - Exibir lista de funcionarios:")
            print("3 - Obter Saldo de divida com fornecedor:")
            print("4 - Calcular Comissão de vendedor:")
            #outras Opções aqui
            op=int( input() )
   
            if op==1:
                self.contratar()
            elif op==2:
                self.exibir()
            elif op ==3:
                self.obterSaldo()
            elif op==4:
                self.calcularComissao()
            else:
                print("Opçao invalida")

    def contratar(self):
        cpf = input("cpf: ")
        nome = input("Nome: ")
        setor = input("Setor: ")
        salario = input("Salario: ")
        self.__func.append( funcionario.Funcionario(cpf, nome, setor, salario) )
 
    def exibir(self):
        for fun in self.__func:
            print(fun.mostraDados())

    def mostraDados(self):
        print(str(self.__codigo)+" "+self.__nome)

    def obterSaldo(Fornecedor):
        valorCredit = float(input("Digite o credito: "))
        valorDivid = float(input("Digite da divida: "))
        saldoDivida = valorCredit-valorDivid
        if(saldoDivida > 0):
            print("Saldo Positivo em:", saldoDivida)
        else:
            print("A empresa está devendo para o fornecedor:", saldoDivida)

    def calcularComissao(Vendedor):
        valorDeVenda = float(input("Digite quanto ele vendeu: "))
        comissao = float(input("Digite a comissao: "))
        valorComissao = valorDeVenda*comissao
        print(valorComissao)