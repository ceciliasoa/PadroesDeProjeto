# coding=utf-8
class Cozinha:
    _instance = None

    def __init__(self):
        self.some_attribute = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

if __name__ == "__main__":
  
  print("Criando duas variáveis chamando a instância singleton ... \n")
  fogao1 = Cozinha.instance()
  fogao2 = Cozinha.instance()

  if fogao1 == fogao2:
    print("Singleton funciona, ambas as variáveis contêm a mesma instância. \n")
  else:
    print("Singleton falhou, as variáveis contêm instâncias diferentes. \n")

  print("Adicionando um atributo ao primeiro Singleton: ")
  fogao1.pedidos = ["sopa"]
  fogao2.pedidos.append("arroz")
  
  print(f"Atributo do primeiro singleton: {fogao1.pedidos}")
  print(f"Atributo do segundo singleton: {fogao2.pedidos}")