import json
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

  def listar(self):
    with open("data/carrinho.json", "r") as file:
      return json.load(file)

  def listar_produtos(self):
    with open("data/produtos.json", "r") as file:
      return json.load(file)

  def adicionar_item(self, cliente_id, produto_id, quantidade):
    self.carrinho.inserir(cliente_id, produto_id, quantidade)

  def remover_item(self, item_id):
    self.carrinho.objetos = [item for item in self.carrinho.objetos if item["produto_id"] != item_id]
    self.carrinho.salvar()

  def filtro_id(self, id):
    return self.carrinho.listar_id(id)

  def cacular_qtd_prod(self, produtos):
    subtotal = 0
    for produto in produtos:
      subtotal += produto["preco"] * produto["quantidade"]
    return subtotal
  
  def calcular_subtotal(self, produtos):
    subtotal = 0
    
    # Itera sobre cada produto na lista de produtos
    for produto in produtos:
        produto_quant = next((p for p in self.listar_produtos() if p["id"] == produto["produto_id"])) #gpt
        
        if produto_quant:
            valor_total = float(produto_quant['preco']) * float(produto['quantidade'])
            subtotal += valor_total
    
    # Retorna o subtotal calculado
    return subtotal