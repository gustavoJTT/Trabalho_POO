import streamlit as st
from view.pedidos_view import PedidosView

class PedidosUI:
    @classmethod
    def run(cls):
        st.header("Pedidos")
        st.write("---")
        cliente_id = st.session_state.user.id
        pedidos_view = PedidosView(None, None, None, None)
        pedidos = pedidos_view.listar_pedidos(cliente_id)

        if not pedidos:
            st.markdown("<center><b>Ainda não há pedidos<b></center>", unsafe_allow_html=True) #deixa usar coisas de html no texto
        else:
            for i, pedido in enumerate(pedidos):
                with st.container(border=True):
                    st.subheader(f"Pedido do dia {pedido['data_compra']}")
                    st.write(f"Valor total da compra: R${pedido['valor_final']:.2f}")
                    st.write("---")
                    st.write(f"Produtos;")

                    for produto in pedido['produtos']:
                        produto_dict = {'nome': produto.get('nome'), 'quantidade': produto.get('quantidade')}
                        st.write(f"- {produto_dict['nome']}  ->  x{produto_dict['quantidade']}")
