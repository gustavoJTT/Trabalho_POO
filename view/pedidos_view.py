from models.pedidos import Pedidos

class PedidosView:
  
  def __init__(self, cliente_id, produtos, valor_final, data_compra):
    self.pedidos = Pedidos(cliente_id, produtos, valor_final, data_compra)

  def listar_pedidos(self, cliente_id):
    return Pedidos.listar_pedidos(cliente_id)