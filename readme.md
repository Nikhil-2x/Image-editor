# Image Editor

A Flask-based web application that allows users to upload images, apply various transformations (like grayscale, blur, edge detection, etc.), preview the processed image, and download the result. The project uses OpenCV for image processing and Tailwind CSS for styling.

## Features

- Image Upload and Processing(Supported formats: PNG, JPG, JPEG, WEBP, GIF).
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
- Feedback Form:
  - Collect user feedback with details like name, email, and feedback message.
  - Store feedback securely in a MySQL database.
  - Admin page to view all feedback
- Security:
  - Credentials for MySQL are stored in a .env file using python-dotenv.

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
- Configure Database
  - Create a MySQL database named credentials and a feedback table:
    ```sql
        CREATE DATABASE credentials;
        USE credentials;
        CREATE TABLE feedback (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            feedback_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ```
- Add your database credentials to a .env file:

  ```
  DB_HOST=localhost
  DB_USER=root
  DB_PASSWORD=your_password
  DB_NAME=credentials

  ```
