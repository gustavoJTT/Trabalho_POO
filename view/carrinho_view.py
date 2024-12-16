from models.carrinho import Carrinho

class CarrinhoView:
  def __init__(self):
    self.carrinho = Carrinho()

  def adicionar_item(self, cliente_id, produto_id, quantidade):
    self.carrinho.inserir(cliente_id, produto_id, quantidade)

  def filtro_id(self, id):
    return self.carrinho.listar_id(id)
  
  from models.carrinho import Carrinho

class CarrinhoView:
  def __init__(self):
    self.carrinho = Carrinho()

  def adicionar_item(self, cliente_id, produto_id, quantidade):
    self.carrinho.inserir(cliente_id, produto_id, quantidade)

  def filtro_id(self, id):
    return self.carrinho.listar_id(id)

  def remover_item(self, item_id):
    self.carrinho.objetos = [item for item in self.carrinho.objetos if item["produto_id"] != item_id]
    self.carrinho.salvar()