import streamlit as st
from view.login_view import ViewLogin
from view.cliente_view import ClientView
from view.carrinho_view import CarrinhoView
from template.carrinho_ui import CarrinhoUI
from template.adm_ui import AdmUI

class UI:
    @classmethod
    def Run(cls):
        if 'page' not in st.session_state:
            st.session_state.page = 'login'

        if 'user' not in st.session_state:
            st.session_state.user = None

        st.set_page_config(
        page_title="APP",  
        page_icon="🚀",           
        initial_sidebar_state="expanded"
        )

            
        match st.session_state.page:
            case 'home':
                cls.__cliente()

            case'login':
                cls.__login()

            case'admin':
                AdmUI.admin()

    @classmethod
    def __cliente(cls):
        section = st.sidebar.selectbox("menu", ("home", "carrinho", "pedidos"))
        match section:
            case "home":
                st.header("Produtos")
                st.markdown("---")
                cls.listar_produtos(ClientView.listar_produtos())

            case "carrinho":
                carrinho_ui = CarrinhoUI()
                carrinho_ui.run()
            case "pedidos":
                st.header("pedidos")

        if st.sidebar.button("sair"):
            st.session_state.page = 'login'
            st.rerun()


    @classmethod
    def __login(cls):

        with st.container(border=True):

            section = st.tabs(["Login", "Cadastro"])

            with section[0]:
                st.header("Login")
                username = st.text_input("Nome de usuario ou Email", key="login_username")
                password = st.text_input("Senha", type="password", key="login_password")

                if st.button("Entrar"):
                    ViewLogin.login_authentication(username, password)

            with section[1]:
                st.header("Cadastro")
                username = st.text_input("nome", key="register_username")
                email = st.text_input("email", key="register_email")
                tel = st.text_input("telefone", key="register_tel")
                password = st.text_input("Senha", type="password", key="register_password")

                if st.button("Cadastrar"):
                    ViewLogin.register_authentication(username, email, tel, password)

    @staticmethod
    def listar_produtos(prod):
        carrinho_view = CarrinhoView()
        for idx, produto in enumerate(prod):
            with st.container(border=True):
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    st.image(produto.img, width=100, use_container_width=True)

                with col2:
                    st.subheader(produto.nome)
                    st.write(produto.descricao)
                    st.write(f"**Preço**: R${produto.preco}")
                    quantidade = st.number_input("Quantidade", min_value=1, value=1, key=f'quantidade-{idx}')
                    if st.button(f"Adicionar ao Carrinho", key=f'button-{idx}', type="primary"):
                        cliente_id = st.session_state.user.id
                        carrinho_view.adicionar_item(cliente_id, produto.id, quantidade)
                        st.success(f"{produto.nome} adicionado ao carrinho!", icon="✅")