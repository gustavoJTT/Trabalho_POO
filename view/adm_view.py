from models.produto import Produto, Produtos

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
        
