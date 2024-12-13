import streamlit as st

class View:
    @staticmethod
    def login_authentication(user:str, password:str):
        if user == "admin" and password == "1234":
            st.session_state.page = 'admin'
            st.success(f"Bem-vindo, {user}!")

        elif user == "flavio" or "gustavo":
             st.session_state.page = 'home'
             st.success(f"Bem-vindo, {user}!")

        else:
            st.error("senha ou usuario invalido!")

    @staticmethod
    def register_authentication():
            st.success("Cadastrado com sucesso")
