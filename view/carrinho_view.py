from models.carrinho import Carrinho

class CarrinhoView:
  def __init__(self):
    self.carrinho = Carrinho()

  def adicionar_item(self, cliente_id, produto_id, quantidade):
    self.carrinho.inserir(cliente_id, produto_id, quantidade)

  def filtro_id(self, id):
    return self.carrinho.listar_id(id)
  
  def remover_item(self, produto_id):
    self.carrinho.remover_item(produto_id)
    self.salvar()