import json
from models.pedidos import Pedidos

class PedidosView:
  
  def __init__(self, cliente_id, produtos, valor_final, data_compra):
    self.pedidos = Pedidos(cliente_id, produtos, valor_final, data_compra)

  def listar_pedidos(self, cliente_id):
    with open("data/pedidos.json", "r") as f:
      pedidos = json.load(f)
      return [pedido for pedido in pedidos if pedido["cliente_id"] == cliente_id]