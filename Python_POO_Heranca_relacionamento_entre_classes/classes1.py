class Pessoa:
  def __innit__(self,nome, cpf, idade):
    self.nome = nome
    self.cpf = cpf
    self.idade = idade

    p1 = Pessoa('Gabriel','123','21')
    print(p1.nome, p1.cpf, p1.idade)