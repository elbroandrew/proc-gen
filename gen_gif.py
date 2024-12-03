import os
from PIL import Image
import vars

image_folder = vars.path

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
sorted_images = sorted(images, key=lambda x: int(os.path.splitext(x)[0]))

frames = []
for i in sorted_images:
    new_frame = Image.open(f"output/{i}")
    frames.append(new_frame)

frames[0].save('result.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=100, loop=0)