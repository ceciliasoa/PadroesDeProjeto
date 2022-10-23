# coding=utf-8
from abc import ABC, abstractmethod
import copy

class Usuario(ABC):
  _genero = None
  _idade = None

  @abstractmethod
  def clone(self):
    pass
    
  def getGenero(self):
    return self._genero
    
  def getIdade(self):
    return self._idade
  
class Usuario_F(Usuario):
  def __init__(self, idade):
    self._genero = "Feminino"
    self._idade = idade
    
  def clone(self):
    return copy.copy(self)
  
class Usuario_M(Usuario):
  def __init__(self, idade):
    self._genero = "Masculino"
    self._idade = idade
    
  def clone(self):
    return copy.copy(self)

if __name__ == "__main__":
  usuario1 = Usuario_F(29)
  usuario2 = Usuario_M(20)
  
  print("usuários:")
  print(usuario1.getGenero(), usuario1.getIdade())
  print(usuario2.getGenero(), usuario2.getIdade())

  clone_usuario1 = usuario1.clone()
  clone_usuario2 = usuario2.clone()
  print("\n")
  print("clone dos usuários:")
  print(usuario1.getGenero(), usuario1.getIdade())
  print(usuario2.getGenero(), usuario2.getIdade())
  