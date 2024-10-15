import streamlit as st
from utils import generate_image, classify_image, load_image_generation_model, load_image_classification_model
from PIL import Image

# Inicializar el estado de sesión
if 'image_generation_model' not in st.session_state:
    with st.spinner("Cargando modelos, por favor espera..."):
        st.session_state.image_generation_model = load_image_generation_model()
        st.session_state.classification_model = load_image_classification_model()
    st.success("Modelos cargados exitosamente!")

# Título de la aplicación
st.title("Generación y Clasificación de Imágenes con Hugging Face")

col1, col2 = st.columns(2)

with col1:
    st.header("Generar Imágenes")
    prompt = st.text_input("Ingresa una solicitud para generar una imagen:")
    
    if 'generated_image' in st.session_state:
        st.image(st.session_state.generated_image, caption="Imagen Generada", use_column_width=True)
    
    if st.button("Generar"):
        if prompt:
            with st.spinner("Generando imagen..."):
                # Generar imagen usando el modelo cargado previamente
                image = generate_image(prompt, st.session_state.image_generation_model)
                st.session_state.generated_image = image  # Guardar la imagen en el estado de sesión
                st.image(image, caption="Imagen Generada", use_column_width=True)
        else:
            st.warning("Por favor, ingresa una solicitud.")

with col2:
    st.header("Clasificar Imágenes")
    
    # Permitir al usuario subir una imagen para clasificar
    uploaded_file = st.file_uploader("Sube una imagen para clasificar", type=["png", "jpg", "jpeg"])
    
    # Clasificar la imagen generada si no se ha subido una imagen nueva
    if st.button("Clasificar Imagen Generada"):
        if 'generated_image' in st.session_state:
            with st.spinner("Clasificando imagen generada..."):
                label = classify_image(st.session_state.generated_image, st.session_state.classification_model)
                st.success(f"Clasificación: {label}")
        else:
            st.warning("No se ha generado ninguna imagen para clasificar.")
    
    # Mostrar y clasificar la imagen subida por el usuario
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen Subida", use_column_width=True)
        
        if st.button("Clasificar Imagen Subida"):
            with st.spinner("Clasificando imagen subida..."):
                label = classify_image(image, st.session_state.classification_model)
                st.success(f"Clasificación: {label}")
