from PIL import Image
import os

# Load the original image
image_path = os.path.expanduser("~/Downloads/Untitled design.jpg")
original_image = Image.open(image_path)

# Set the target size in inches and DPI
target_size_inches = (12, 15)
dpi = 300  # Standard high resolution for print

# Calculate target pixel dimensions
target_size_pixels = (int(target_size_inches[0] * dpi), int(target_size_inches[1] * dpi))

# Resize the image with high-quality resampling
resized_image = original_image.resize(target_size_pixels, Image.LANCZOS)

# Save the resized image in the current directory
resized_image_path = "Untitled_design_12x15_inches.jpg"
resized_image.save(resized_image_path, dpi=(dpi, dpi))

print(f"Original image loaded from: {image_path}")
print(f"Resized image saved as: {resized_image_path}")