# page_title: Cotizador Servicios 
import streamlit as st 
import streamlit as st
from pathlib import Path
import streamlit as st
from modules.Cotizador import Cotizador
from PIL import Image
import time 
from routes.mensaje_rcourant_whatsapp import whatsapp_rcourant


# Configuración de la página
st.set_page_config(
    page_title="CERC Cotizador",
    page_icon='💸',
    layout='wide',
    menu_items={
        "About": "Centro Educativo Richard Courant"\
        " By ∴"
    }
)

st.title("📚 Cotizador de Servicios")
st.markdown("Completa los campos para conocer el costo aproximado de tu servicio. **El costo final puede variar.**")

# Cargamos la imagen del logo 
with st.sidebar:
    imagen_logo = Image.open("assets/cerc_logo.png")
    st.image(imagen_logo, caption="Richard Courant", use_container_width=True)


cotizador = Cotizador()

# Formularios con selectbox
tipo_servicio = st.selectbox("**Tipo de servicio**", ["Tarea", "Examen", "Proyecto", "Clase", "Regularizacion"])
nivel = st.selectbox("**Nivel académico**", ["Universidad", "Bachillerato", "Secundaria"])
urgencia = st.selectbox("**Urgencia**", ["Alta (Hoy o Mañana)", "Media (de 2 a 4 días)", "Baja (más de 4 días)"])
area = st.selectbox("**Área de la materia**", ["Fisico_Matematicas", "Quimico_Biologicas", "Sociales", "Humanidades"])
dificultad = st.selectbox("**Dificultad**", ["Alta", "Media", "Baja"])

# Botón para cotizar

if st.button("Calcular cotización", type="primary"):
    with st.spinner("Calculando"): 
        time.sleep(1.5)
    
    # Quitar la info de la urgencia 
    urgencia = urgencia.split("(")[0].strip()

    resultado = cotizador.cotizar_servicio(
        tipo_servicio=tipo_servicio,
        nivel=nivel,
        urgencia=urgencia,
        area_materia=area,
        dificultad=dificultad
    )

    if "error" in resultado:
        st.error(f"Ocurrió un error al cotizar: {resultado['error']}")
    else:
        st.success(f"💰 Tarifa estimada: ${resultado['total']} MXN")

        with st.expander("Ver desglose", icon="🔍"):
            st.write(f"Tarifa base: ${resultado['base']}")
            st.write(f"Extra por nivel: ${resultado['extra_nivel']}")
            st.write(f"Extra por urgencia: ${resultado['extra_urgencia']}")
            st.write(f"Extra por dificultad: ${resultado['extra_dificultad']}")
            st.write(f"Extra por área: ${resultado['extra_area']}")

        mensaje= f"""
        Hola, He cotizado mi servicio en la pagina:
        Tarifa base: ${resultado['base']}
        Extra por nivel: ${resultado['extra_nivel']}
        Extra por urgencia: ${resultado['extra_urgencia']}
        Extra por dificultad: ${resultado['extra_dificultad']}
        Extra por área: ${resultado['extra_area']}
        =============================
        *Tarifa Final: ${resultado['total']}*
        """
        whatsapp_rcourant(mensaje=mensaje)

if __name__ == "__main__":
    print("Cotizador inciado")


