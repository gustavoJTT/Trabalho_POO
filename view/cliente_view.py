import streamlit as st
from models.produto import Produtos

class ClientView:
    @staticmethod
    def listar_produtos():
        return Produtos.listar()
