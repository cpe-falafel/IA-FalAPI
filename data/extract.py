import os

from PIL import Image
import io
import pandas as pd

df = pd.read_parquet('')

output_dir = ""
os.makedirs(output_dir, exist_ok=True)

for index, row in df.iterrows():
    image_data = row['image']['bytes']
    image = Image.open(io.BytesIO(image_data))

    largeur, hauteur = image.size
    if largeur >= 256 and hauteur >= 256:
        image.save(os.path.join(output_dir, f"image_{index}.png"))
        print(f"Image {index} sauvegardée : {largeur}x{hauteur}")
