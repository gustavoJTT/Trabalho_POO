import json

class Pedidos:
  def __init__(self, cliente_id, produtos, valor_final, data_compra):
    self.cliente_id = cliente_id
    self.produtos = produtos
    self.valor_final = valor_final
    self.data_compra = data_compra
    