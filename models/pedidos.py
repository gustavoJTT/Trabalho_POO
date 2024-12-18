import json

class Pedidos:
  def __init__(self, cliente_id, produtos, valor_final, data_compra):
    self.objetos = self.carregar_pedidos()

  @classmethod
  def carregar_pedidos(self):
    with open("data/pedidos.json", "r") as f:
      return json.load(f)
    
  @classmethod
  def listar_pedidos(cls, cliente_id):
    with open("data/pedidos.json", "r") as f:
      pedidos = json.load(f)
      return [pedido for pedido in pedidos if pedido["cliente_id"] == cliente_id]