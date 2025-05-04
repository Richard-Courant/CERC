# page_title: Inicio 
import streamlit as st
from pathlib import Path
import streamlit as st
from modules.Cotizador import Cotizador
from PIL import Image
from routes.mensaje_rcourant_whatsapp import  whatsapp_rcourant
import os 

# Configuración de la página
st.set_page_config(
    page_title="CER Courant",
    page_icon='🧠',
    layout='wide',
    menu_items={
        "About": "Centro Educativo Richard Courant"
                 " By ∴"
    }
)

# Título principal
st.title("🎓🧠 Centro Educativo Richard Courant")

# Logo en la barra lateral
with st.sidebar:
    imagen_logo = Image.open("assets/cerc_logo.png")
    st.image(imagen_logo, caption="Richard Courant", use_container_width=False)


# Espaciado
st.markdown("---")

# Misión
st.subheader("🎯 Nosotros")
st.markdown("""
Buscamos proporcionar un acompañamiento académico integral, personalizado y accesible, que impulse el desarrollo intelectual y emocional de los estudiantes. En CERC buscamos despertar el pensamiento crítico, fomentar la curiosidad y acompañar cada proceso educativo con compromiso, empatía y excelencia.
""")

# Enviar mensaje a Richar Courant 
mensaje = "¡Hola! Quiero pedir información sobre los servicios de Richard Courant."
whatsapp_rcourant(mensaje=mensaje)

filepath_base = r"/assets/cerc_rcourant_base.png"

if os.path.exists(filepath_base): 
    imagen_base = Image.open(filepath_base)
    st.image(imagen_base)