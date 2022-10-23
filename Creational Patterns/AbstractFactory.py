# coding=utf-8
from abc import ABC, abstractmethod

class FabricaSala(ABC):
    @abstractmethod
    def adiciona_sofa(self):
        pass

    @abstractmethod
    def adiciona_lustre(self):
        pass
      
    @abstractmethod
    def adiciona_rack(self):
        pass

class FabricaSalaIndustrial(FabricaSala):
    def adiciona_sofa(self):
        return SofaIndustrial()

    def adiciona_lustre(self):
        return LustreIndustrial()
      
    def adiciona_rack(self):
        return RackIndustrial()

class FabricaSalaMinimalista(FabricaSala):
    def adiciona_sofa(self):
        return SofaMinimalista()

    def adiciona_lustre(self):
        return LustreMinimalista()
      
    def adiciona_rack(self):
        return RackMinimalista()

class Sofa(ABC):
    @abstractmethod
    def cria_sofa(self):
        pass

class SofaIndustrial(Sofa):
    def cria_sofa(self):
        return "sofá industrial adicionado"

class SofaMinimalista(Sofa):
    def cria_sofa(self):
        return "sofá minimalista adicionado"

class Lustre(ABC):

    @abstractmethod
    def cria_lustre(self):
        pass
      
class LustreIndustrial(Lustre):
    def cria_lustre(self):
        return "lustre industrial adicionado"

class LustreMinimalista(Lustre):
    def cria_lustre(self):
        return "lustre minimalista adicionado"

class Rack(ABC):

    @abstractmethod
    def cria_rack(self):
        pass

class RackIndustrial(Rack):
    def cria_rack(self):
        return "rack industrial adicionado"

class RackMinimalista(Rack):
    def cria_rack(self):
        return "rack minimalista adicionado"

def cliente(fabrica):

    sofa = fabrica.adiciona_sofa()
    lustre = fabrica.adiciona_lustre()
    rack = fabrica.adiciona_rack()

    print(sofa.cria_sofa())
    print(lustre.cria_lustre())
    print(rack.cria_rack())

if __name__ == "__main__":
    print("Sala industrial é escolhida:")
    cliente(FabricaSalaIndustrial())

    print("\n")

    print("Sala minimalista é escolhida:")
    cliente(FabricaSalaMinimalista())