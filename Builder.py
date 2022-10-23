# coding=utf-8
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    @abstractmethod
    def sanduiche(self):
        pass

    @abstractmethod
    def adiciona_pao(self):
        pass

    @abstractmethod
    def adiciona_carne(self):
        pass

    @abstractmethod
    def adiciona_queijo(self) :
        pass
      
    @abstractmethod
    def adiciona_tomate(self) :
        pass


class ConcreteBuilder(Builder):

    def __init__(self) :
        self.reset()

    def reset(self) :
        self._sanduiche = Sanduiche()

    @property
    def sanduiche(self):
        sanduiche = self._sanduiche
        self.reset()
        return sanduiche
      
    def adiciona_pao(self) :
        self._sanduiche.add("Pão")
       
    def adiciona_carne(self) :
        self._sanduiche.add("Carne")

    def adiciona_queijo(self) :
        self._sanduiche.add("Queijo")

    def adiciona_tomate(self) :
        self._sanduiche.add("Tomate")
      
    def adiciona_alface(self) :
        self._sanduiche.add("Alface")


class Sanduiche():
    
    def __init__(self) :
        self.ingredientes = []

    def add(self, ingrediente) :
        self.ingredientes.append(ingrediente)

    def lista_ingredientes(self) :
        print(', '.join(self.ingredientes))


class Director:
   
    def __init__(self) :
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder) :
        self._builder = builder

    def xburger(self) :
        self.builder.adiciona_pao()
        self.builder.adiciona_carne()
        self.builder.adiciona_queijo()

    def xburger_salada(self) :
      self.builder.adiciona_pao()
      self.builder.adiciona_carne()
      self.builder.adiciona_queijo()
      self.builder.adiciona_tomate()
      self.builder.adiciona_alface()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("xburger: ")
    director.xburger()
    builder.sanduiche.lista_ingredientes()

    print("\n")

    print("xburger com salada: ")
    director.xburger_salada()
    builder.sanduiche.lista_ingredientes()

    print("\n")

    print("Pedido customizado: ")
    builder.adiciona_pao()
    builder.adiciona_queijo()
    builder.adiciona_tomate()
    builder.sanduiche.lista_ingredientes()