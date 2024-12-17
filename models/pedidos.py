import json

class Pedidos:
  def __init__(self, cliente_id, produtos, valor_final, data_compra):
    self.objetos = self.carregar_pedidos()

  def carregar_pedidos(self):
    with open("data/pedidos.json", "r") as f:
      return json.load(f)
    