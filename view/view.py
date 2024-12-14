import streamlit as st
import json

class View:
    @staticmethod
    def login_authentication(user: str, password: str):
        # Carregar as credenciais do arquivo JSON
        with open("data/user.json", "r") as f:
            credenciais = json.load(f)

        # Verificar se o usuário e senha estão presentes no arquivo JSON
        for credencial in credenciais:
            if credencial["id"] == user and credencial["password"] == password:
                st.session_state.page = "admin" if user == "admin" else "home"
                st.success(f"Bem-vindo, {user}!")
                return

        st.error("senha ou usuario invalido!")

    @staticmethod
    def register_authentication(username: str, nome: str, password: str):
        with open("data/user.json", "r") as f:
            credenciais = json.load(f)

        for credencial in credenciais:
            if credencial["id"] == username:
                st.error("Usuário já cadastrado")
                return

        novo_usuario = {"id": username, "nome": nome, "password": password}
        credenciais.append(novo_usuario)

        with open("data/user.json", "w") as f:
            json.dump(credenciais, f)

        st.success("Usuário cadastrado com sucesso")