import streamlit as st

class View:
    def __init__(self):
        with open('template/login.html', 'r', encoding='utf-8') as file:
            self.html_content = file.read()

    def show(self):
        st.markdown(self.html_content, unsafe_allow_html=True)

# Criar uma instância da classe e chamar o método para exibir o HTML
view = View()
view.show()
