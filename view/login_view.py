import streamlit as st
from models.cliente import Clientes, Cliente

class ViewLogin:
    @staticmethod
    def login_authentication(user: str, password: str):
        for cliente in Clientes.listar():
            if (cliente.email == user or cliente.nome == user) and cliente.senha == password:
                if cliente.adm:
                    st.session_state.page = 'admin'
                else:
                    st.session_state.page = 'home'
                st.session_state.user = cliente
                st.success(f"bem vindo, {cliente.nome}")
                return
            
        st.error("email ou senha invalido!")

    @staticmethod
    def register_authentication(Username: str, User_email: str, telefone : str, password: str):
        liberado = True
        for cliente in Clientes.listar():
            if cliente.email == User_email:
               liberado = False

        if liberado:
            c = Cliente(
                id = 0,
                nome = Username,
                email = User_email,
                fone = telefone,
                senha = password
            )
            Clientes.inserir(c)
            st.success("Usuário cadastrado com sucesso")
        else:
            st.error("ja existe um usuario com esse email")
