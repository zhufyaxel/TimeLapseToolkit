import os
import subprocess
from PIL import Image
import glob
import re
import sys
import imageio
import concurrent.futures
import numpy as np

def get_consistent_images(input_folder):
    image_extensions = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp']
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(input_folder, f'*.{ext}')))
        image_files.extend(glob.glob(os.path.join(input_folder, f'*.{ext.upper()}')))
    
    if not image_files:
        print("No image files found.")
        return [], None

    first_image = Image.open(image_files[0])
    width, height = first_image.size
    consistent_images = [image_files[0]]

    for image_file in image_files[1:]:
        with Image.open(image_file) as img:
            if img.size == (width, height):
                consistent_images.append(image_file)
            else:
                print(f"Skipping image with inconsistent size: {image_file}")

    return consistent_images, (width, height)

def resize_image(image_path, new_size):
    with Image.open(image_path) as img:
        img = img.resize(new_size, Image.LANCZOS)
        output_path = f"resized_{os.path.basename(image_path)}"
        img.save(output_path)
    return output_path

def create_gif_with_ffmpeg(input_folder, output_file, fps, compress_level=3, scale_percent=100):
    consistent_images, original_size = get_consistent_images(input_folder)
    if not consistent_images:
        print("No images with consistent size found. Unable to create GIF.")
        return

    # Calculate new dimensions, ensuring both width and height are even
    new_width = int(original_size[0] * scale_percent / 100)
    new_width = new_width if new_width % 2 == 0 else new_width + 1
    new_height = int(original_size[1] * scale_percent / 100)
    new_height = new_height if new_height % 2 == 0 else new_height + 1
    new_size = (new_width, new_height)

    # Create a temporary text file listing all resized image files
    with open("filelist.txt", "w") as f:
        for image in consistent_images:
            f.write(f"file '{image}'\nduration {1/fps}\n")

    try:
        # First create a temporary video file
        temp_video = "temp_video.mp4"
        video_command = [
            'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt',
            '-vf', f'scale={new_size[0]}:{new_size[1]}:flags=lanczos',
            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'ultrafast', temp_video
        ]
        subprocess.run(video_command, check=True, capture_output=True, text=True)

        # Then convert the video to GIF
        gif_command = [
            'ffmpeg', '-y', '-i', temp_video,
            '-vf', f'fps={fps},split[s0][s1];[s0]palettegen=max_colors=256[p];[s1][p]paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle',
            '-loop', '0', output_file
        ]
        subprocess.run(gif_command, check=True, capture_output=True, text=True)

        print(f"GIF successfully created: {output_file}")
        print(f"Output size: {new_size[0]}x{new_size[1]}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create GIF: {e}")
        print("Error output:")
        print(e.stdout)
        print(e.stderr)
    finally:
        # Delete temporary files
        os.remove("filelist.txt")
        if os.path.exists(temp_video):
            os.remove(temp_video)

def create_gif_with_imageio(input_folder, output_file, fps, compress_level=3, scale_percent=100):
    consistent_images, original_size = get_consistent_images(input_folder)
    if not consistent_images:
        print("No images with consistent size found. Unable to create GIF.")
        return

    # Calculate new dimensions
    new_width = int(original_size[0] * scale_percent / 100)
    new_height = int(original_size[1] * scale_percent / 100)
    new_size = (new_width, new_height)

    images = []
    for filename in consistent_images:
        with Image.open(filename) as img:
            img = img.resize(new_size, Image.LANCZOS)
            # Ensure image is in RGB mode
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # Convert PIL image to numpy array
            img_array = np.array(img)
            images.append(img_array)

    # Create GIF using imageio
    duration = 1.0 / fps  # seconds
    imageio.mimsave(output_file, images, format='GIF', duration=duration, loop=0)

    print(f"GIF successfully created: {output_file}")
    print(f"Output size: {new_size[0]}x{new_size[1]}")

# Add selection in main function
def main():
    default_input_folder = os.path.join(os.getcwd(), 'input_images')
    default_output_folder = os.path.join(os.getcwd(), 'output')
    os.makedirs(default_output_folder, exist_ok=True)

    # Input folder selection
    print("Select input folder:")
    print(f"1. Use default folder ('{default_input_folder}')")
    print("2. Choose another folder")
    print("3. Enter path manually")
    input_choice = input("Enter option (1/2/3): ")

    if input_choice == '1':
        input_folder = default_input_folder
    elif input_choice == '2':
        folders = [f for f in os.listdir() if os.path.isdir(f)]
        print("Available folders:")
        for i, folder in enumerate(folders):
            print(f"{i+1}. {folder}")
        folder_choice = int(input("Select folder number: ")) - 1
        input_folder = folders[folder_choice]
    else:
        input_folder = input(f"Enter input folder path: ")

    # Output folder selection
    print("\nSelect output folder:")
    print(f"1. Use default folder ('{default_output_folder}')")
    print("2. Choose another folder")
    print("3. Enter path manually")
    output_choice = input("Enter option (1/2/3): ")

    if output_choice == '1':
        output_folder = default_output_folder
    elif output_choice == '2':
        folders = [f for f in os.listdir() if os.path.isdir(f)]
        print("Available folders:")
        for i, folder in enumerate(folders):
            print(f"{i+1}. {folder}")
        folder_choice = int(input("Select folder number: ")) - 1
        output_folder = folders[folder_choice]
    else:
        output_folder = input(f"Enter output folder path: ")

    os.makedirs(output_folder, exist_ok=True)
    default_output_file = os.path.join(output_folder, 'output.gif')

    output_file = input(f"Enter output GIF filename (default: {default_output_file}): ") or default_output_file
    if os.path.dirname(output_file) == '':
        output_file = os.path.join(output_folder, output_file)

    # Get original image size
    _, original_size = get_consistent_images(input_folder)
    if original_size:
        print(f"Original image size: {original_size[0]}x{original_size[1]}")
        scale_percent = input("Enter output size percentage (1-100, default: 100): ") or 100
    else:
        print("Unable to get original image size, will use default size.")
        scale_percent = 100

    fps = input("Enter GIF frame rate (default: 10): ") or 10
    compress_level = input("Enter compression level (1-3, 1 lowest, 3 highest, default: 2): ") or 2

    fps = int(fps)
    compress_level = int(compress_level)
    scale_percent = int(scale_percent)

    if scale_percent < 1 or scale_percent > 100:
        print("Output size percentage must be between 1 and 100. Using default value 100.")
        scale_percent = 100

    method = input("Choose method to create GIF (1: ffmpeg, 2: imageio, default: 1): ") or "1"

    if method == "1":
        create_gif_with_ffmpeg(input_folder, output_file, fps, compress_level, scale_percent)
    elif method == "2":
        create_gif_with_imageio(input_folder, output_file, fps, compress_level, scale_percent)
    else:
        print("Invalid choice, using ffmpeg method.")
        create_gif_with_ffmpeg(input_folder, output_file, fps, compress_level, scale_percent)

if __name__ == "__main__":
    main()
