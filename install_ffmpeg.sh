#!/bin/bash

# Define FFmpeg download URL and target directory
FFMPEG_URL="https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
FFMPEG_DIR="$HOME/ffmpeg"

# Check the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "macOS environment detected"
    
    # Install FFmpeg using Homebrew
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    echo "Installing FFmpeg using Homebrew..."
    brew install ffmpeg

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Linux environment detected"
    
    # Install FFmpeg using package manager
    if command -v apt-get &> /dev/null; then
        echo "Installing FFmpeg using apt-get..."
        sudo apt-get update
        sudo apt-get install -y ffmpeg
    elif command -v yum &> /dev/null; then
        echo "Installing FFmpeg using yum..."
        sudo yum install -y ffmpeg
    else
        echo "Unsupported package manager. Please install FFmpeg manually."
        exit 1
    fi

elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Windows environment detected"

    # Create target directory
    mkdir -p "$FFMPEG_DIR"

    # Download FFmpeg
    echo "Downloading FFmpeg..."
    curl -L -o ffmpeg.zip "$FFMPEG_URL"

    # Unzip FFmpeg
    echo "Unzipping FFmpeg..."
    unzip -o ffmpeg.zip -d "$FFMPEG_DIR"
    rm ffmpeg.zip

    # Find the unzipped FFmpeg directory
    FFMPEG_BIN_DIR=$(find "$FFMPEG_DIR" -type d -name "bin" | head -n 1)

    # Set PATH
    if [[ -n "$FFMPEG_BIN_DIR" ]]; then
        echo "Setting PATH..."
        echo "export PATH=\"$FFMPEG_BIN_DIR:\$PATH\"" >> ~/.bashrc
        source ~/.bashrc
    else
        echo "FFmpeg bin directory not found."
    fi
else
    echo "Unsupported operating system."
    exit 1
fi

# Verify installation
if ffmpeg -version > /dev/null 2>&1; then
    echo "FFmpeg installation successful."
else
    echo "FFmpeg installation failed, please check manually."
fi
