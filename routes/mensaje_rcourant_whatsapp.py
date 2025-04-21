import streamlit as st
import urllib.parse


def whatsapp_rcourant(mensaje: str):
    """Botón que abre el chat de WhatsApp con mensaje precargado"""
    mensaje_encoded = urllib.parse.quote(mensaje)
    numero = "5215580860729"
    whatsapp_url = f"https://wa.me/{numero}?text={mensaje_encoded}"

    st.markdown(
        f'''
        <a href="{whatsapp_url}" target="_blank">
            <button style="
                background-color:#25D366;
                color:white;
                padding:10px 16px;
                border:none;
                border-radius:6px;
                font-size:16px;
                font-weight:bold;
                cursor:pointer;
            ">
            📲 Escribirme por WhatsApp
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )
