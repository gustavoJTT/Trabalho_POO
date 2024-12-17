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

        for i, pedido in enumerate(pedidos):
            with st.expander(f"Pedido {i+1}"):
                st.write(f"Data do pedido: {pedido['data_compra']}")
                st.write(f"Valor total: R${pedido['valor_final']:.2f}")
                st.write("---")
                st.write(f"Produtos:")
                for produto in pedido['produtos']:
                    produto_dict = {
                        'nome': produto.get('nome', 'Produto não encontrado'),
                        'quantidade': produto.get('quantidade', 0)
                    }
                    st.write(f"- {produto_dict['nome']} (x{produto_dict['quantidade']})")