import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Kevin Ayala - Marketing Digital", layout="wide")

# Estilo personalizado con colores
st.markdown("""
<style>
body {
    background-color: #ffffff;
    color: #000000;
    font-family: 'Helvetica', sans-serif;
}
h1, h2, h3 {
    color: #01C7C5;
}
button {
    border-radius: 8px;
}
.big-button {
    background-color: #01EF36;
    color: black;
    padding: 0.75em 2em;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    margin: 10px;
}
.service-card {
    background-color: #f5f5f5;
    padding: 20px;
    border-left: 8px solid #01C7C5;
    border-radius: 15px;
    margin-bottom: 15px;
}
a {
    text-decoration: none;
    color: white;
}
.footer {
    color: gray;
    text-align: center;
    font-size: 14px;
    padding: 30px;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# Encabezado principal
# ==========================
st.markdown("<h1 style='text-align: center;'>🎯 Kevin Ayala</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Marketing Digital & Diseño Gráfico</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Conecta con tu audiencia con diseños únicos y estrategias efectivas.</p>", unsafe_allow_html=True)

st.markdown("---")

# ==========================
# Sección de servicios
# ==========================
st.subheader("✨ Servicios que ofrezco")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='service-card'>
    <h4>✍️ Diseño de Flyers</h4>
    <p>Diseños atractivos y modernos para tus eventos, promociones y redes sociales.</p>
    <b>$60.000</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='service-card'>
    <h4>📢 Publicaciones Promocionadas</h4>
    <p>Impulsa tu contenido con campañas optimizadas en Facebook e Instagram.</p>
    <b>$36.000 c/u</b>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='service-card'>
    <h4>🎬 Videos Publicitarios</h4>
    <p>Crea videos cortos e impactantes para redes sociales.</p>
    <b>$100.000</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='service-card'>
    <h4>📱 Administración de Redes</h4>
    <p>Publicaciones, interacción con clientes y crecimiento orgánico.</p>
    <b>$100.000 por red</b>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# Botones
# ==========================
st.markdown("---")
st.subheader("📲 Contáctame fácilmente")

col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("<a href='https://wa.me/57300XXXXXXX' target='_blank'><button class='big-button'>WhatsApp</button></a>", unsafe_allow_html=True)
with col4:
    st.markdown("<a href='https://instagram.com/skin_digital1' target='_blank'><button class='big-button' style='background-color:#01C7C5;'>Instagram</button></a>", unsafe_allow_html=True)
with col5:
    st.markdown("<a href='https://inversionesbighouse.com' target='_blank'><button class='big-button' style='background-color:#000;color:#fff;'>Sitio Web</button></a>", unsafe_allow_html=True)

# ==========================
# Formulario de contacto
# ==========================
st.markdown("---")
st.subheader("📝 Escríbeme tu solicitud")

with st.form("form_contacto"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo electrónico")
    mensaje = st.text_area("Mensaje o servicio que necesitas")
    enviar = st.form_submit_button("Enviar")

    if enviar:
        st.success("¡Gracias por tu mensaje! Te responderé pronto.")

# ==========================
# Footer
# ==========================
st.markdown("<div class='footer'>© 2025 Kevin Ayala - Todos los derechos reservados</div>", unsafe_allow_html=True)
