# Load model directly
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification

image = Image.open("Felis_catus-cat_on_snow.jpg")

processor = AutoImageProcessor.from_pretrained("google/efficientnet-b7")
model = AutoModelForImageClassification.from_pretrained("google/efficientnet-b7")
inputs = processor(image, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

# model predicts one of the 1000 ImageNet classes
predicted_label = logits.argmax(-1).item()
print(model.config.id2label[predicted_label]),

