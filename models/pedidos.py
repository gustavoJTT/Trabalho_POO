import json

class Pedidos:
  def __init__(self, cliente_id, produtos, valor_final, data_compra):
    self.cliente_id = cliente_id
    self.produtos = produtos
    self.valor_final = valor_final
    self.data_compra = data_compra
    
  @classmethod
  def carregar_pedidos(cls):
    try:
      with open("data/pedidos.json", "r") as arquivo:
        return json.load(arquivo)
    except FileNotFoundError:
      return []
    
  @classmethod
  def listar_por_cliente_id(cls, cliente_id):
    pedidos = cls.carregar_pedidos()
    return [pedido for pedido in pedidos if pedido.cliente_id == cliente_id]
