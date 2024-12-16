from models.carrinho import Carrinho

class CarrinhoView:
  def __init__(self):
    self.carrinho = Carrinho()

  def adicionar_item(self, cliente_id, produto_id, quantidade):
    self.carrinho.inserir(cliente_id, produto_id, quantidade)

