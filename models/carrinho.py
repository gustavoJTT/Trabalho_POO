import json

class Carrinho:
  def __init__(self):
    self.objetos = self.carregar_carrinho()

  def carregar_carrinho(self):
    try:
      with open("data/carrinho.json", "r") as arquivo:
          return json.load(arquivo)
    except FileNotFoundError:
      return []

  def inserir(self, cliente_id, produto_id, quantidade):
    self.objetos.append({"cliente_id": cliente_id, "produto_id": produto_id, "quantidade": quantidade})
    self.salvar()

  def salvar(self):
    with open("data/carrinho.json", "w") as arquivo:
        json.dump(self.objetos, arquivo)

  def remover_item(self, produto_id):
    self.objetos = [item for item in self.objetos if item["produto_id"] != produto_id]
    self.salvar()

  def limpar(self):
    self.objetos = []
    self.salvar()