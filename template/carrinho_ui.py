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
    contador = 0
    for produto in produtos_no_carrinho:
        produto_info = next((p for p in produtos_data if p["id"] == produto["produto_id"]), None)
        if produto_info:
            with st.container(border=True):
                col1, col2, col3 = st.columns([2, 3, 3])

                with col1:
                    st.image(produto_info["img"], width=100, use_container_width=True)
                
                with col2:
                    st.subheader(produto_info["nome"])
                    st.write(f"Preco: R${produto_info['preco']}")
                    st.write(f"Quantidade: {produto['quantidade']}")
                    valor_total = float(produto_info['preco']) * float(produto['quantidade'])
                    st.write(f"Valor final do(s) produto(s): R${valor_total:.2f}")

                with col3:
                  contador += 1 #contador de botões, tentei fazer para sincronizar com os itens do carrinho e remover eles quando os números foream clicados
                  if st.button("Remover do carrinho", key=f"remover_botao_{contador}", type="primary"):
                      item_remover = next((item for item in produtos_no_carrinho if item["id_sequencia"] == contador))
                      if item_remover:
                          produtos_no_carrinho.remove(item_remover)
                          self.carrinho.remover_item(item_remover["produto_id"])
                          st.success("Item removido com sucesso!")