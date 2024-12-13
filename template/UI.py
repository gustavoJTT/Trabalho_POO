import streamlit as st
from view.view import View

class UI:


    @classmethod
    def Run(cls):
        if 'page' not in st.session_state:
            st.session_state.page = 'login'
            
        match st.session_state.page:
            case 'home':
                cls.__home()

            case'login':
                cls.__login()

            case'admin':
                cls.__admin()

    @classmethod
    def __home(cls):
        st.title("Bem-vindo à página principal!")

    @classmethod
    def __admin(cls):
        st.title("Bem-vindo à página de administrador")

    @classmethod
    def __login(cls):
        section = st.tabs(["Login", "Cadastro"])

        with section[0]:
            st.header("Login")
            username = st.text_input("Usuário", key="login_username")
            password = st.text_input("Senha", type="password", key="login_password")

            if st.button("Entrar"):
                View.login_authentication(username, password)

        with section[1]:
            st.header("Cadastro")
            username = st.text_input("Usuário", key="register_username")
            password = st.text_input("Senha", type="password", key="register_password")

            if st.button("Cadastrar"):
                View.register_authentication()

