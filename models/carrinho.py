import json

class Carrinho:
  def __init__(self, id, id_produto, quantidade):
    self.id = id
    self.id_produto = id_produto
    self.quantidade = quantidade

class Carrinhos:
  def __init__(self):
    self.objetos = self.carregar_carrinho()

  def carregar_carrinho(self):
    try:
      with open("data/carrinho.json", "r") as arquivo:
        return json.load(arquivo)
    except FileNotFoundError:
      return []

  def inserir(self, cliente_id, produto, quantidade):
    self.objetos.append({"id": cliente_id, "id_produto": produto.id, "quantidade": quantidade})
    self.salvar()

  def salvar(self):
    with open("data/carrinho.json", "w") as arquivo:
      json.dump(self.objetos, arquivo)