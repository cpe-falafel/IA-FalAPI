from PIL import Image
import os


def crop_center(image, crop_width, crop_height):
    img_width, img_height = image.size
    left = (img_width - crop_width) // 2
    top = (img_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    return image.crop((left, top, right, bottom))


def process_images(input_folder, output_folder, crop_width=256, crop_height=256):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            if img.width < crop_width or img.height < crop_height:
                print(f"Image {filename} trop petite pour un crop 256x256, ignorée.")
                continue

            cropped_img = crop_center(img, crop_width, crop_height)
            cropped_img.save(os.path.join(output_folder, filename))
            print(f"Image {filename} recadrée et enregistrée.")


input_folder = "images_goreV0"
output_folder = "images_gore"

process_images(input_folder, output_folder)
