import streamlit as st
from view.login_view import ViewLogin
from view.cliente_view import ClientView
import json

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
                cls.__admin()

    @classmethod
    def __cliente(cls):
        section = st.sidebar.selectbox("menu", ("home", "carrinho", "pedidos"))
        match section:
            case "home":
                st.header("Produtos")
                st.markdown("---")
                cls.listar_produtos(ClientView.listar_produtos())

            case "carrinho":
                st.header("carrinho")
            case "pedidos":
                st.header("pedidos")

        if st.sidebar.button("sair"):
            st.session_state.page = 'login'
            st.rerun()


    @classmethod
    def __admin(cls):
        st.title("Bem-vindo à página de administrador")
        section = st.sidebar.selectbox("Menu Administrador", ("clientes", "categorias", "produtos", "pedidos"))
        match section:
            case "clientes":
                st.header("Clientes cadastrados")

            case "categorias":
                st.header("categorias de produtos")

            case "produtos":
                st.header("Produtos")

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
    def adicionar_ao_carrinho(produto):
        with open('data/carrinho.json', 'a') as f:
            json.dump({
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'preco': produto.preco
            }, f)
            f.write('\n')

    @staticmethod
    def listar_produtos(prod):
        for idx, produto in enumerate(prod):
            with st.container(border=True):
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    st.image(produto.img, width=100, use_container_width=True)

                with col2:
                    st.subheader(produto.nome)
                    st.write(produto.descricao)
                    st.write(f"**Preço**: R${produto.preco}")
                    if st.button(f"Adicionar ao Carrinho", key=f'button-{idx}', type="primary"):
                        st.success(f"{produto.nome} adicionado ao carrinho!", icon="✅")
                        UI.adicionar_ao_carrinho(produto)