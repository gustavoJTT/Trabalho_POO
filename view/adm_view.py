from models.produto import Produto, Produtos
from models.cliente import Clientes
from models.categoria import Categoria, Categorias
from models.pedidos import Pedidos
import streamlit as st

class AdmView:
    @staticmethod
    def cadastra_produto(nome, descricao, preco, img, estoque, id_categoria):
        liberado = True
        for p in Produtos.listar():
            if nome == p.nome:
                liberado = False
        if liberado:
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
        else:
            st.error("ja existe um produto com esse nome")

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
        client.set_adm(not(client.adm))
        Clientes.salvar()

    @staticmethod
    def listar_categoria():
        return Categorias.listar()
    
    @staticmethod
    def remover_categoria(categoria):
        Categorias.excluir(categoria)

    @staticmethod
    def atualizar_categoria(id, descri):
        c = Categoria(id, descri)
        Categorias.atualizar(c)
    
    @staticmethod
    def cadastra_categoria(descriçao):
        c = Categoria(0, descriçao)
        Categorias.inserir(c)

    @staticmethod
    def listar_pedidos():
        pedidos = Pedidos.carregar_pedidos()
        return pedidos
    
    @staticmethod
    def listar_pedidos_por_cliente():
        pedidos = AdmView.listar_pedidos()
        pedidos_por_cliente = {}
        for pedido in pedidos:
            if pedido["cliente_id"] not in pedidos_por_cliente:
                pedidos_por_cliente[pedido["cliente_id"]] = []
            pedidos_por_cliente[pedido["cliente_id"]].append(pedido)

        return pedidos_por_cliente
    
    @staticmethod
    def buscar_cliente_por_id(cliente_id):
        clientes = Clientes.listar()
        for cliente in clientes:
            if cliente.id == cliente_id:
                return cliente
        return None