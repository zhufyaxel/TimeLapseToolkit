import os
from PIL import Image

def compress_image(input_path, output_path, quality=85, lossless=False, scale=None):
    with Image.open(input_path) as img:
        if scale and scale != 1:
            new_size = (int(img.width * scale), int(img.height * scale))
            img = img.resize(new_size, Image.LANCZOS)
        
        if lossless:
            img.save(output_path, optimize=True)
        else:
            img.save(output_path, optimize=True, quality=quality)

def get_user_input():
    print("Welcome to the Image Compression Tool!")
    
    input_dir = input("Enter the source image folder path (default is 'input_images'): ") or "input_images"
    output_dir = input("Enter the path to save compressed images (default is 'input_images_zipped'): ") or "input_images_zipped"
    
    quality = input("Enter compression quality (1-100, default is 85, press Enter for default): ")
    quality = int(quality) if quality.isdigit() and 1 <= int(quality) <= 100 else 85
    
    lossless = input("Use lossless compression? (y/n, default is n): ").lower() == 'y'
    
    scale_input = input("Resize images? If yes, enter scale factor (e.g., 0.5 for half size, 2 for double size), press Enter to skip: ")
    scale = float(scale_input) if scale_input else None
    
    return input_dir, output_dir, quality, lossless, scale

def main():
    input_dir, output_dir, quality, lossless, scale = get_user_input()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            compress_image(input_path, output_path, quality, lossless, scale)
            print(f"Compressed: {filename}")

    print("All images have been compressed!")

if __name__ == "__main__":
    main()
