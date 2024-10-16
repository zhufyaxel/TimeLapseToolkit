import os
import cv2
from PIL import Image
import numpy as np

def create_video_from_images(input_folder, output_file, frames_per_image, fps, codec):
    # Get all PNG image files
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    image_files.sort()  # Ensure images are in order

    if not image_files:
        print("No PNG image files found.")
        return

    # Read the first image to get dimensions
    first_image = Image.open(os.path.join(input_folder, image_files[0]))
    width, height = first_image.size

    try:
        print(f"Using codec: {codec}")
        fourcc = cv2.VideoWriter_fourcc(*codec)
        video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

        # Process each image
        for image_file in image_files:
            image_path = os.path.join(input_folder, image_file)
            image = Image.open(image_path)
            
            # Check if image dimensions match
            if image.size != (width, height):
                print(f"Skipping file {image_file} due to mismatched dimensions.")
                continue
            
            frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            
            # Write each image for the specified number of frames
            for _ in range(frames_per_image):
                video_writer.write(frame)

        # Release the video writer
        video_writer.release()
        print(f"Video successfully created: {output_file} using codec: {codec}")
    except Exception as e:
        print(f"Failed to use codec {codec}: {e}")

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
    default_output_file = os.path.join(output_folder, 'output_video.mp4')

    output_file = input(f"Enter output video filename (default: {default_output_file}): ") or default_output_file
    if os.path.dirname(output_file) == '':
        output_file = os.path.join(output_folder, output_file)

    frames_per_image = input("Enter number of frames per image (default: 1): ") or 1
    fps = input("Enter video frame rate (default: 30): ") or 30

    # Ensure frames_per_image and fps are integers
    frames_per_image = int(frames_per_image)
    fps = int(fps)

    # Provide codec options
    codecs = ['avc1', 'mp4v', 'X264', 'H264']
    print("Available codecs:")
    for i, codec in enumerate(codecs):
        print(f"{i + 1}: {codec}")
    
    codec_choice = input("Select codec (enter number, default: 1): ") or 1
    codec_choice = int(codec_choice) - 1

    if 0 <= codec_choice < len(codecs):
        selected_codec = codecs[codec_choice]
    else:
        print("Invalid choice, using default codec: avc1")
        selected_codec = 'avc1'

    create_video_from_images(input_folder, output_file, frames_per_image, fps, selected_codec)

if __name__ == "__main__":
    main()
