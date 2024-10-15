# Generación y Clasificación de Imágenes con Stable Diffusion y Hugging Face

Este repositorio contiene una aplicación web desarrollada en **Streamlit** que integra dos modelos preentrenados de **Hugging Face**: uno para la **generación de imágenes** y otro para la **clasificación de imágenes**. Los modelos utilizados son:

- **CompVis/stable-diffusion-v1-4** para la generación de imágenes.
- **microsoft/resnet-50** para la clasificación de imágenes.

## Funcionalidades

### 1. **Generación de Imágenes**
- Sección ubicada en el lado izquierdo de la interfaz.
- Permite ingresar un **prompt** (texto) que describe la imagen que deseas generar.
- Al hacer clic en **"Generar"**, el modelo **Stable Diffusion** generará una imagen basada en el texto proporcionado.

### 2. **Clasificación de Imágenes**
- Sección ubicada en el lado derecho de la interfaz.
- Puedes cargar una imagen desde tu dispositivo para que sea clasificada usando el modelo **ResNet-50**
  
### 3. **Conexión entre la Generación y la Clasificación**
- La imagen generada en la sección de **Generación de Imágenes** puede ser clasificada directamente en la sección de **Clasificación de Imágenes** con solo hacer clic en el botón correspondiente.
