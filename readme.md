# Image Editor

A Flask-based web application that allows users to upload images, apply various transformations (like grayscale, blur, edge detection, etc.), preview the processed image, and download the result. The project uses OpenCV for image processing and Tailwind CSS for styling.

## Features
- Upload an image in supported formats (PNG, JPG, JPEG, WEBP, GIF).
- Apply image transformations:
  - Convert to Grayscale
  - Blur
  - Edge Detection
  - Resize
  - Rotate
  - Format Conversion (PNG, JPG, WEBP).
- Preview the processed image.
- Download the processed image.
- Responsive design with animations.

## Setup
- Clone the Repository
    ```bash
    git clone https://github.com/Nikhil-2x/Image-editor.git
cd Image-editor
    ```
- Set Up Virtual Environment
    ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
    ```
- Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```