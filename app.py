import streamlit as st

st.set_page_config(page_title="Kevin Ayala - Marketing y Diseño", layout="centered")

st.title("🎨 Kevin Ayala - Marketing Digital y Diseño Gráfico")
st.subheader("Soluciones creativas para tu negocio 💡")

st.markdown("""
Ofrezco servicios de:
- ✍️ Diseño de flyers: $60.000
- 🎬 Videos publicitarios: $100.000
- 📱 Administración de redes: $100.000 por red
- 📢 Publicaciones promocionadas: $36.000
""")

st.markdown("---")

st.header("📂 Portafolio")
st.markdown("👉 Aquí puedes mostrar tus mejores diseños (te enseño cómo agregar imágenes luego)")

st.markdown("---")

st.header("📞 Contáctame")
with st.form("contact_form"):
    nombre = st.text_input("Tu nombre")
    correo = st.text_input("Correo electrónico")
    mensaje = st.text_area("Mensaje o solicitud")
    enviado = st.form_submit_button("Enviar")

    if enviado:
        st.success(f"¡Gracias {nombre}! Te responderé pronto al correo {correo}.")

st.markdown("---")

st.markdown("📲 [Escríbeme por WhatsApp](https://wa.me/57300XXXXXXX)")
st.markdown("📸 [Instagram](https://instagram.com/skin_digital1)")
