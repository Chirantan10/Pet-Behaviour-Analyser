#!/bin/bash

# Install FFmpeg in the container
echo "Installing FFmpeg..."
curl -fsSL https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz | tar -xJ
mkdir -p ~/bin
mv ffmpeg-*-static/ffmpeg ~/bin/
mv ffmpeg-*-static/ffprobe ~/bin/
export PATH=$HOME/bin:$PATH

echo "FFmpeg installed successfully!"

# Start the Flask app
python app.py
