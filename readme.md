# Image Editor

A Flask-based web application that allows users to upload images, apply various transformations (like grayscale, blur, edge detection, etc.), preview the processed image, and download the result. The project uses OpenCV for image processing, MongoDB Atlas for feedback storage, and Tailwind CSS for styling.

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
  - Feedback is securely stored in MongoDB Atlas.
- Security:
  - MongoDB credentials are stored in a .env file using python-dotenv.

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
- Configure MongoDB Atlas
  - Set up a MongoDB Atlas cluster and create a database named ytmanager.
  - Inside the ytmanager database, create a collection named credentials for storing feedback.
  - Add your MongoDB URI to the .env file:
    ```
    MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority
    ```
    Replace <username>, <password>, <cluster-url>, and <database> with your actual MongoDB Atlas credentials.
- Run the Application