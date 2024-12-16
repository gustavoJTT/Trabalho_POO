import streamlit as st
from view.adm_view import AdmView

class AdmUI:
    @classmethod
    def admin(cls):
        section = st.sidebar.selectbox("Menu Administrador", ("clientes", "categorias", "produtos", "pedidos"))
        match section:
            case "clientes":
                st.header("Clientes cadastrados")

            case "categorias":
                st.header("categorias de produtos")

            case "produtos":
                st.header("Produtos")
                cls.cadastro_produto_button()
                st.write("---")
                cls.manter_produto(AdmView.listar_produtos())

            case "pedidos":
                st.header("pedidos")

        if st.sidebar.button("sair"):
            st.session_state.page = 'login'
            st.rerun()

    @classmethod
    def manter_produto(cls, prod):
        if len(prod) == 0:
            st.subheader("nenhum produto disponivel")
        else:
            for idx, produto in enumerate(prod):
                with st.container(border=True):
                    col1, col2, col3 = st.columns([2, 3, 1])
                    
                    with col1:
                        st.image(produto.img, width=100, use_container_width=True)

                    with col2:
                        st.subheader(f"{produto.id} : {produto.nome}")
                        st.write(f"quantidade em estoque: {produto.estoque}")
                        st.write(produto.descricao)
                        st.write(f"**Preço**: R${produto.preco}")

                    with col3:
                        if st.button(f"Remover", key=f'button-{idx}', type="primary", use_container_width= True):
                            AdmView.remover_produto(produto)
                            st.rerun()

                        cls.atualizar_produto_button(produto)
    @staticmethod
    def cadastro_produto_button():
        with st.expander("novo produto"):
            nome = st.text_input("Nome", key="nome_produto")
            descricao = st.text_input("Descrição", key="descricao_produto")
            preco = st.text_input("preço", key="preco_produto")
            img = st.text_input("Imagem", key="img_produto")
            estoque = st.text_input("estoque", key="estoque_produto")
            id_C = st.text_input("ID da categoria", key="categoria_produto")

            if st.button("cadastra"):
                AdmView.cadastra_produto(nome, descricao, preco, img, estoque, id_C)
                st.rerun()

    @staticmethod
    def atualizar_produto_button(prod):
        with st.expander("atualizar produto",):
            nome = st.text_input("Nome", key="nome_att", value=prod.nome)
            descricao = st.text_input("Descrição", key="descricao_att", value=prod.descricao)
            preco = st.text_input("preço", key="preco_att", value=prod.preco)
            img = st.text_input("Imagem", key="img_att", value=prod.img)
            estoque = st.text_input("estoque", key="estoque_att", value=prod.estoque)
            id_C = st.text_input("ID da categoria", key="categoria_att", value=prod.id_categoria)

            if st.button("atualizar"):
                AdmView.atualizar_produto(prod.id, nome, descricao, preco, img, estoque, id_C)
                st.rerun()
    
    @classmethod
    def manter_cliente(cls, clients):
        if len(clients) == 0:
            st.subheader("nenhum produto disponivel")
        else:
            for idx, client in enumerate(clients):
                with st.container(border=True):
                    col1, col2= st.columns([3, 1])
                    
                    with col1:
                        st.subheader(f"{client.id} : {client.nome}")
                        st.write(f"Email: {client.email}")
                        st.write(f"Telefone: {client.fone}")
                        st.write(f"Administrador: {client.adm}")
                    with col2:
                        pass






