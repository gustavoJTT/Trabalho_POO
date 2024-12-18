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
    id_sequencia = len(self.objetos) + 1
    self.objetos.append({"cliente_id": cliente_id, "produto_id": produto_id, "quantidade": quantidade, "id_sequencia": id_sequencia}) #sequencia pra tentar remover oq bate a sequencia e o contador do carrinho_ui
    self.salvar()

  def salvar(self):
    with open("data/carrinho.json", "w") as arquivo:
      json.dump(self.objetos, arquivo)

  def remover_item(self, item_id):
    x = next((item for item in self.objetos if item["id_sequencia"] == item_id), None)
    if x != None:
      self.objetos.remove(x)
      self.salvar()

  def limpar(self):
    self.objetos = []
    self.salvar()