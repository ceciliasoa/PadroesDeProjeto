# coding=utf-8
from abc import ABC, abstractmethod

class Construtor(ABC):
    @abstractmethod
    def metodo_fabrica(self):
      pass

class GelatoConstrutor(Construtor):
    def metodo_fabrica(self):
      produto = Gelato()
      produto.preparo.append("creme")
      produto.preparo.append("essencia")
      produto.preparo.append("corante de morango")
      produto.preparo.append("calda")
      produto.preparo.append("adiciona no pote")
      return produto


class PicoleConstrutor(Construtor):
    def metodo_fabrica(self):
      produto = Picole()
      produto.preparo.append("suco")
      produto.preparo.append("corante de morango")
      produto.preparo.append("adiciona no palito")
      produto.preparo.append("cobertura")
      return produto


class Sorvete(ABC):
  @abstractmethod
  def mostrar_sorvete(self):
    pass


class Gelato(Sorvete):
  def __init__(self):
    self.preparo = []    

  def mostrar_sorvete(self):
    print(f"gelato: {self.preparo}")


class Picole(Sorvete):
  def __init__(self):
    self.preparo = []    
    
  def mostrar_sorvete(self):
    print(f"picole: {self.preparo}")


def cliente(construtor: Construtor()) -> None:

  produto = construtor.metodo_fabrica()
  produto.mostrar_sorvete()


if __name__ == "__main__":
    cliente(GelatoConstrutor())
    print("\n")
    cliente(PicoleConstrutor())
 