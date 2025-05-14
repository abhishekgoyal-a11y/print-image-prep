from PIL import Image
import os

def get_image_size_inches(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Get pixel dimensions
        width_px, height_px = img.size
        
        # Try to get DPI from image metadata
        try:
            dpi_x, dpi_y = img.info['dpi']
        except (KeyError, TypeError):
            # If DPI information is not available, assume standard 96 DPI
            dpi_x = dpi_y = 96
            print("Note: DPI information not found in image, assuming 96 DPI")
        
        # Calculate dimensions in inches
        width_inches = width_px / dpi_x
        height_inches = height_px / dpi_y
        
        return width_inches, height_inches, dpi_x, dpi_y, width_px, height_px

def main():
    # Check both the original and resized images
    original_path = os.path.expanduser("Untitled design.jpg")
    resized_path = "Untitled_design_12x15_720_inches.jpg"
    
    print("Original Image:")
    width_in, height_in, dpi_x, dpi_y, width_px, height_px = get_image_size_inches(original_path)
    print(f"Dimensions: {width_in:.2f}\" × {height_in:.2f}\"")
    print(f"Resolution: {dpi_x:.0f} × {dpi_y:.0f} DPI")
    print(f"Pixel dimensions: {width_px} × {height_px} pixels")
    print("\n" + "="*50 + "\n")
    
    print("Resized Image:")
    width_in, height_in, dpi_x, dpi_y, width_px, height_px = get_image_size_inches(resized_path)
    print(f"Dimensions: {width_in:.2f}\" × {height_in:.2f}\"")
    print(f"Resolution: {dpi_x:.0f} × {dpi_y:.0f} DPI")
    print(f"Pixel dimensions: {width_px} × {height_px} pixels")

if __name__ == "__main__":
    main() 