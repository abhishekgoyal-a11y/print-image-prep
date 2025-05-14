from PIL import Image
import os
from math import log10, sqrt
import numpy as np

def calculate_psnr(original, resized):
    """Calculate PSNR (Peak Signal-to-Noise Ratio) between two images"""
    # Convert images to numpy arrays
    img1 = np.array(original)
    img2 = np.array(resized)
    
    # Resize img2 to match img1's dimensions for comparison
    if img1.shape != img2.shape:
        resized_temp = Image.fromarray(img2)
        resized_temp = resized_temp.resize(original.size, Image.LANCZOS)
        img2 = np.array(resized_temp)
    
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def analyze_image(image_path):
    """Analyze various aspects of image quality"""
    img = Image.open(image_path)
    
    # Basic information
    width, height = img.size
    format_type = img.format
    mode = img.mode
    
    # Get DPI
    try:
        dpi_x, dpi_y = img.info['dpi']
    except (KeyError, TypeError):
        dpi_x = dpi_y = 96
    
    # File size
    file_size = os.path.getsize(image_path) / 1024  # Size in KB
    
    # Bits per pixel (color depth)
    bits_per_pixel = len(img.getbands()) * 8
    
    # Calculate pixels per inch (PPI)
    ppi = sqrt((width ** 2 + height ** 2) / ((width/dpi_x) ** 2 + (height/dpi_y) ** 2))
    
    return {
        'dimensions': (width, height),
        'format': format_type,
        'mode': mode,
        'dpi': (dpi_x, dpi_y),
        'file_size': file_size,
        'bits_per_pixel': bits_per_pixel,
        'ppi': ppi,
        'total_pixels': width * height,
        'image_object': img
    }

def main():
    original_path = "Untitled design.jpg"
    resized_path = "Untitled_design_12x15_inches.jpg"
    
    # Analyze both images
    original_stats = analyze_image(original_path)
    resized_stats = analyze_image(resized_path)
    
    # Calculate PSNR between original and resized
    psnr_value = calculate_psnr(original_stats['image_object'], resized_stats['image_object'])
    
    # Print detailed analysis
    print("=== Original Image Analysis ===")
    print(f"Dimensions: {original_stats['dimensions'][0]} × {original_stats['dimensions'][1]} pixels")
    print(f"Resolution: {original_stats['dpi'][0]:.0f} × {original_stats['dpi'][1]:.0f} DPI")
    print(f"Effective PPI: {original_stats['ppi']:.1f}")
    print(f"File Size: {original_stats['file_size']:.1f} KB")
    print(f"Color Depth: {original_stats['bits_per_pixel']} bits per pixel")
    print(f"Total Pixels: {original_stats['total_pixels']:,}")
    print(f"Color Mode: {original_stats['mode']}")
    
    print("\n=== Resized Image Analysis ===")
    print(f"Dimensions: {resized_stats['dimensions'][0]} × {resized_stats['dimensions'][1]} pixels")
    print(f"Resolution: {resized_stats['dpi'][0]:.0f} × {resized_stats['dpi'][1]:.0f} DPI")
    print(f"Effective PPI: {resized_stats['ppi']:.1f}")
    print(f"File Size: {resized_stats['file_size']:.1f} KB")
    print(f"Color Depth: {resized_stats['bits_per_pixel']} bits per pixel")
    print(f"Total Pixels: {resized_stats['total_pixels']:,}")
    print(f"Color Mode: {resized_stats['mode']}")
    
    print("\n=== Quality Comparison ===")
    print(f"PSNR (Peak Signal-to-Noise Ratio): {psnr_value:.2f} dB")
    
    # Print quality assessment
    print("\n=== Quality Assessment ===")
    print("Resolution Quality:", end=" ")
    if resized_stats['total_pixels'] > original_stats['total_pixels']:
        print("✓ Resized image has higher resolution")
    else:
        print("✗ Original image has higher resolution")
        
    print("Print Quality:", end=" ")
    if resized_stats['dpi'][0] > original_stats['dpi'][0]:
        print("✓ Resized image has better print quality (higher DPI)")
    else:
        print("✗ Original image has better print quality")
        
    print("Storage Efficiency:", end=" ")
    pixels_per_kb_original = original_stats['total_pixels'] / original_stats['file_size']
    pixels_per_kb_resized = resized_stats['total_pixels'] / resized_stats['file_size']
    if pixels_per_kb_resized > pixels_per_kb_original:
        print("✓ Resized image has better storage efficiency")
    else:
        print("✗ Original image has better storage efficiency")
    
    # Overall recommendation
    print("\n=== Recommendation ===")
    if resized_stats['dpi'][0] >= 300 and resized_stats['total_pixels'] > original_stats['total_pixels']:
        print("The resized image is better for high-quality printing and detailed viewing.")
    elif original_stats['file_size'] < resized_stats['file_size'] and original_stats['dpi'][0] >= 150:
        print("The original image might be sufficient for most purposes while being more storage efficient.")
    else:
        print("Choose based on your specific needs:")
        print("- Use resized image for high-quality printing")
        print("- Use original image for web/screen display or storage efficiency")

if __name__ == "__main__":
    main() 