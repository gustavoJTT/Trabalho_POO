import streamlit as st
from view.adm_view import AdmView

class AdmUI:
    @classmethod
    def admin(cls):
        section = st.sidebar.selectbox("Menu Administrador", ("clientes", "categorias", "produtos", "pedidos"))
        match section:
            case "clientes":
                st.header("Clientes cadastrados")
                st.write("---")
                cls.manter_cliente(AdmView.listar_clientes())

            case "categorias":
                st.header("categorias de produtos")
                st.write("---")
                cls.cadastra_categoria()
                st.write('---')
                cls.manter_categoria(AdmView.listar_categoria())

            case "produtos":
                st.header("Produtos")
                st.write("---")
                cls.cadastro_produto_button()
                st.write("---")
                cls.manter_produto(AdmView.listar_produtos())

            case "pedidos":
                st.header("Pedidos")
                st.write("---")
                pedidos_por_cliente = AdmView.listar_pedidos_por_cliente()
                if not pedidos_por_cliente:
                    st.markdown("<center><b>Ainda não há pedidos<b></center>", unsafe_allow_html=True)
                else:
                    for cliente_id, pedidos_cliente in pedidos_por_cliente.items():
                        cliente = AdmView.buscar_cliente_por_id(cliente_id)
                        with st.expander(f"ID: {cliente_id} | {cliente.nome}"):
                            if not pedidos_cliente:
                                st.markdown(f"<center><b>Cliente {cliente_id} - {cliente.nome} ainda não fez pedidos<b></center>", unsafe_allow_html=True)
                            else:
                                for i, pedido in enumerate(pedidos_cliente):
                                    with st.container(border=True):
                                        st.subheader(f"Pedido do dia {pedido['data_compra']}")
                                        st.write(f"Valor total da compra: R${pedido['valor_final']:.2f}")
                                        st.write("---")
                                        st.write(f"Produtos;")

                                        for produto in pedido["produtos"]:
                                            produto_dict = {'nome': produto.get('nome'), 'quantidade': produto.get('quantidade')}
                                            st.write(f"- {produto_dict['nome']}  ->  x{produto_dict['quantidade']}")

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
                    col1, col2, col3 = st.columns([1, 4, 1])
                    
                    with col1:
                        st.image(produto.img, width=100, use_container_width=True)

                    with col2:
                        st.subheader(f"ID: {produto.id} | {produto.nome}")
                        st.write(f"quantidade em estoque: {produto.estoque}")
                        st.write(produto.descricao)
                        st.write(f"**Preço**: R${produto.preco}")

                    with col3:
                        if st.button(f"Remover", key=f'button-{idx}', type="primary", use_container_width= True):
                            AdmView.remover_produto(produto)
                            st.rerun()

                        cls.atualizar_produto_button(produto,idx)

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
    def atualizar_produto_button(prod, key):
        with st.expander("atualizar produto",):
            nome = st.text_input("Nome", key=f"nome_att{key}", value=prod.nome)
            descricao = st.text_input("Descrição", key=f"descricao_att{key}", value=prod.descricao)
            preco = st.text_input("preço", key=f"preco_att{key}", value=prod.preco)
            img = st.text_input("Imagem", key=f"img_att{key}", value=prod.img)
            estoque = st.text_input("estoque", key=f"estoque_att{key}", value=prod.estoque)
            id_C = st.text_input("ID da categoria", key=f"categoria_att{key}", value=prod.id_categoria)

            if st.button("atualizar", key=f"atu{key}"):
                AdmView.atualizar_produto(prod.id, nome, descricao, preco, img, estoque, id_C)
                st.rerun()
    
    @classmethod
    def manter_cliente(cls, clients):
        if len(clients) == 0:
            st.subheader("nenhum cliente cadastrado")
        else:
            for idx, client in enumerate(clients):
                with st.container(border=True):
                    col1, col2= st.columns([3, 1])
                    
                    with col1:
                        st.subheader(f"ID: {client.id} | {client.nome}")
                        st.write(f"Email: {client.email}")
                        st.write(f"Telefone: {client.fone}")
                        st.write(f"Administrador: {client.adm}")

                    with col2:
                        if st.button("Remover", key=f'button-{idx}', use_container_width= True):
                            AdmView.remover_cliente(client)
                            st.rerun()

                        if client.adm:
                            if st.button("Remover ADM", key=f'button_admR-{idx}',  use_container_width= True):
                                AdmView.alterar_adm(client)
                                st.rerun()
                        else:
                            if st.button("Torna ADM", key=f'button_admT-{idx}', use_container_width= True):
                                AdmView.alterar_adm(client)
                                st.rerun()

    @classmethod
    def manter_categoria(cls, cat):
        if len(cat) == 0:
            st.subheader("nenhuma categoria registrada")
        else:
            for idx, categoria in enumerate(cat):
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1], vertical_alignment="top")
                    
                    with col1:
                        st.subheader(f"ID: {categoria.id}")
                        with st.container(border=True):
                            st.write(categoria.descricao)
                        

                    with col2:

                        if st.button(f"Remover", key=f'button_cat-{idx}', type="primary", use_container_width= True):
                            AdmView.remover_categoria(categoria)
                            st.rerun()

                        cls.atualizar_categoria_button(categoria, idx)
        
    @staticmethod
    def atualizar_categoria_button(cat, key):
        with st.expander("atualizar categoria",):
            descricao = st.text_input("Descrição", key=f"descricao_cat{key}", value=cat.descricao)


            if st.button("atualizar", key=f"ac{key}"):
                AdmView.atualizar_categoria(cat.id, descricao)
                st.rerun()
    
    @staticmethod
    def cadastra_categoria():
        with st.expander("nova categoria"):
            d = st.text_input("descriçao")
            if st.button("cadastra categoria"):
                AdmView.cadastra_categoria(d)
                st.rerun()