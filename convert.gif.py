#!/usr/bin/env python3
import imageio
import os

# List your image file paths in the order you want them in the GIF
image_folder = 'tmdb_backgrounds'
image_files = sorted([os.path.join(image_folder, file)
                     for file in os.listdir(image_folder)
                     if file.endswith('.png') or file.endswith('.jpg')])

# Output GIF path
output_gif = 'Movie_output.gif'

# Create GIF
with imageio.get_writer(output_gif, mode='I', duration=20000) as writer:
    for filename in image_files:
        image = imageio.v3.imread(filename)
        writer.append_data(image)

print(f"GIF saved as {output_gif}")
