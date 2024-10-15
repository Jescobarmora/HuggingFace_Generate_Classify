from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch

# Cargar el modelo de generación de imágenes (Stable Diffusion XL)
def load_image_generation_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    return StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    ).to(device)

# Cargar el modelo de clasificación de imágenes (ResNet)
def load_image_classification_model():
    return pipeline("image-classification", model="microsoft/resnet-50")

# Generar imagen usando el modelo ya cargado
def generate_image(prompt, generator):
    image = generator(prompt).images[0]
    return image

# Clasificar una imagen usando el modelo ya cargado
def classify_image(image, classifier):
    predictions = classifier(image)
    return predictions[0]["label"]