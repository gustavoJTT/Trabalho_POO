import streamlit as st

# Habilitar tela cheia
st.set_page_config(
    page_title="Meu App",
    page_icon=":rocket:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)


if 'page' not in st.session_state:
    st.session_state.page = 'login'

if st.session_state.page == 'home':
    st.title("Bem-vindo à página principal!")

if st.session_state.page == 'login':
    section = st.tabs(["login", "cadastro"])
    with section[0]:
        st.header("Login")
        username = st.text_input("Usuário", key="login_username")
        password = st.text_input("Senha", type="password", key="login_password")

        if st.button("Entrar"):
            st.session_state.page = 'home'
            st.success(f"Bem-vindo, {username}!")

    with section[1]:
        st.header("Cadastro")
        username = st.text_input("Usuário", key="register_username")
        password = st.text_input("Senha", type="password", key="register_password")
        if st.button("Cadastrar"):
            st.success("Cadastrado com sucesso")
