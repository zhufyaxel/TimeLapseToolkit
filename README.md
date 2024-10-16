# Image to Video/GIF Conversion Tool

[中文](README_CN.md) | English

This is a powerful image processing toolkit designed for batch processing images, creating videos, and GIFs. It's particularly suitable for processing time-lapse photography results, but can also be used for other scenarios requiring batch image processing.

## Example Outputs

### Sample GIF
![Sample GIF](output/output-ffmpeg.gif)

### Sample Video
[Click here to view sample video](output/output_video.mp4)

## Main Features

1. Batch image compression
2. Convert image sequences to video
3. Convert image sequences to GIF

## Environment Setup

1. Ensure that Python 3.6 or higher is installed on your system.

2. Note for Windows users: The scripts in this project need to be run in an environment similar to Git Bash. If you haven't installed Git Bash yet, please download and install it from the [official website](https://git-scm.com/download/win).

3. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

4. Run the initialization script:
   - Windows (in Git Bash): `./init_project.sh`
   - Mac/Linux: `bash init_project.sh`

5. Activate the virtual environment:
   - Windows (in Git Bash): `source venv/Scripts/activate`
   - Mac/Linux: `source venv/bin/activate`

6. Install FFmpeg (if not already installed):
   - Run `bash install_ffmpeg.sh`

7. If you encounter codec issues on Windows:
   - Run `bash install_openh264.sh`

## Usage Instructions

### 1. Compress Images

Run the command: `python compress_images.py`

Follow the prompts to enter:
- Source image folder path (default: 'input_images')
- Path to save compressed images (default: 'input_images_zipped')
- Compression quality (1-100, default: 85)
- Whether to use lossless compression (y/n, default: n)
- Whether to resize images (enter scale factor, e.g., 0.5 for half size, 2 for double size)

### 2. Create Video

Run the command: `python create_video_from_images.py`

Follow the prompts to enter:
- Input folder (containing PNG images)
- Output folder
- Output video filename
- Number of frames per image
- Video frame rate
- Choose codec (avc1, mp4v, X264, H264)

### 3. Create GIF

Run the command: `python create_gif_from_images.py`

Follow the prompts to enter:
- Input folder (containing images)
- Output folder
- Output GIF filename
- Output size percentage (1-100)
- GIF frame rate
- Compression level (1-3)
- Choose creation method (1: ffmpeg, 2: imageio)

## Notes

- Ensure that the images in the input folder are of consistent size.
- For video and GIF creation, it's recommended to use PNG format images for best quality.
- If you encounter performance issues, try adjusting the compression level or output size.
- Windows users should ensure to run all scripts in Git Bash or a similar Unix-like environment.

## Troubleshooting

- If you encounter a "FFmpeg not found" error, make sure FFmpeg is correctly installed and added to the system PATH.
- For Windows users, if you encounter codec issues, try running the `install_openh264.sh` script.
- If you have problems running scripts on Windows, make sure you're using Git Bash or a similar environment, not the regular Command Prompt or PowerShell.

If you encounter any issues while using these tools, feel free to open an issue or contact us for help.
