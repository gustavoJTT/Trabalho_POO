from models.produto import Produto, Produtos
from models.cliente import Clientes

class AdmView:
    @staticmethod
    def cadastra_produto(nome, descricao, preco, img, estoque, id_categoria):
        p = Produto(
            id = 0,
            nome = nome,
            descricao = descricao,
            preco = preco,
            img = img,
            estoque = estoque,
            id_categoria = id_categoria
        )
        Produtos.inserir(p)

    @staticmethod   
    def listar_produtos():
        return Produtos.listar()
    
    @staticmethod
    def remover_produto(produto):
        Produtos.excluir(produto)

    @staticmethod
    def atualizar_produto(id, nome, descricao, preco, img, estoque, id_categoria):
        p = Produto(
            id = id,
            nome = nome,
            descricao = descricao,
            preco = preco,
            img = img,
            estoque = estoque,
            id_categoria = id_categoria
        )
        Produtos.atualizar(p)

    @staticmethod
    def listar_clientes():
        return Clientes.listar()
    
    @staticmethod
    def remover_cliente(client):
        Clientes.excluir(client)

    @staticmethod
    def alterar_adm(client):
        client.adm = not(client.adm)
        Clientes.salvar()