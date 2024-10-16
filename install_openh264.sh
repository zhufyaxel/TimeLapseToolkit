#!/bin/bash
# TimeLapseToolkit: OpenH264 Installation Script

# Download libopenh264
echo "Downloading libopenh264..."
curl -L -o openh264.tar.gz https://github.com/cisco/openh264/releases/download/v2.1.1/openh264-2.1.1-win64.dll.bz2

# Unzip file
echo "Unzipping libopenh264..."
mkdir -p $HOME/openh264
tar -xjf openh264.tar.gz -C $HOME/openh264

# Setting environment variables
echo "Setting environment variables..."
export OPENH264_DIR="$HOME/openh264"
export PATH="$OPENH264_DIR:$PATH"

# Writing environment variables to .bashrc
echo "Writing environment variables to .bashrc..."
echo "export OPENH264_DIR=\"$HOME/openh264\"" >> $HOME/.bashrc
echo "export PATH=\"\$OPENH264_DIR:\$PATH\"" >> $HOME/.bashrc

# Prompt user to restart terminal
echo "Installation complete. Please restart the terminal to apply changes."
