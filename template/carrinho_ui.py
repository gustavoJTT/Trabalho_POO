import json
import streamlit as st
from view.carrinho_view import CarrinhoView

class CarrinhoUI:
  def __init__(self):
    self.carrinho = CarrinhoView()

  def run(self):
    st.header("Carrinho")
    st.markdown("---")
    carrinho_data = json.load(open("data/carrinho.json", "r"))
    produtos_data = json.load(open("data/produtos.json", "r"))
    cliente_id = st.session_state.user.id
    produtos_no_carrinho = [item for item in carrinho_data if item["cliente_id"] == cliente_id]
    for produto in produtos_no_carrinho:
      produto_info = next((p for p in produtos_data if p["id"] == produto["produto_id"]), None)
      if produto_info:
        with st.container(border=True):
            col1, col2= st.columns([1, 3])

            with col1:
              st.image(produto_info["img"], width=100, use_container_width=True)
            
            with col2:
              st.subheader(produto_info["nome"])
              st.write(f"Preco: R${produto_info['preco']}")
              st.write(f"Quantidade: {produto['quantidade']}")