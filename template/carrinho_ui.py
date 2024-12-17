import streamlit as st
from view.carrinho_view import CarrinhoView

class CarrinhoUI:
  def __init__(self):
    self.carrinho_service = CarrinhoView()

  def run(self):
    st.header("Carrinho")
    st.markdown("---")
    cliente_id = st.session_state.user.id
    produtos_no_carrinho = self.carrinho_service.get_produtos_no_carrinho(cliente_id)
    produtos_data = self.carrinho_service.listar_produtos()

    if not produtos_no_carrinho:
      st.markdown("<center><b>Não há itens no carrinho ainda<b></center>", unsafe_allow_html=True) #deixa usar coisas de html no texto
    else:
      self.exibir_produtos(produtos_data, produtos_no_carrinho)
      self.exibir_subtotal(produtos_no_carrinho)

  def exibir_produtos(self, produtos_data, produtos_no_carrinho):
    for i, produto in enumerate(produtos_no_carrinho):
      produto_quant = next((p for p in produtos_data if p["id"] == produto["produto_id"]), None)
      if produto_quant:
        with st.container(border=True):
          col1, col2, col3 = st.columns([2, 3, 3])

          with col1:
            st.image(produto_quant["img"], width=100, use_container_width=True)
          
          with col2:
            st.subheader(produto_quant["nome"])
            st.write(f"Preco: R${produto_quant['preco']}")
            st.write(f"Quantidade: {produto['quantidade']}")
            st.write("---")
            valor_total = float(produto_quant['preco']) * float(produto['quantidade'])
            st.write(f"Valor final do(s) produto(s): R${valor_total:.2f}")

          with col3:
            if st.button("Remover do carrinho", key=f"remover_botao_{i}", type="secondary"):
              self.carrinho_service.remover_item(produto["produto_id"])
              st.success("Item removido com sucesso!")

  def exibir_subtotal(self, produtos_no_carrinho):
    subtotal = self.carrinho_service.calcular_subtotal(produtos_no_carrinho)
    st.markdown("---")
    col1, col2 = st.columns([4, 2])
    with col1:
      st.subheader(f"Subtotal: R${subtotal:.2f}")
    with col2:
      if st.button("Confirmar compra", type="primary"):
        cliente_id = st.session_state.user.id
        self.carrinho_service.salvar_limpar(cliente_id)
        st.success("Compra confirmada!")