from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import cv2
import os

port = int(os.environ.get("PORT", 8080))

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename, operation):
    img = cv2.imread(f"upload/{filename}")

    if img is None:  # Handle invalid files
        return None

    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        case "cwebp":
            newFilename = f"static/saved/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFilename, img)  # Save immediately
            return newFilename
        case "cjpg":
            newFilename = f"static/saved/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFilename, img)  # Save immediately
            return newFilename
        case "cpng":
            newFilename = f"static/saved/{filename.split('.')[0]}.png"
            cv2.imwrite(newFilename, img)  # Save immediately
            return newFilename
        case "blur":
            imgProcessed = cv2.GaussianBlur(img, (15, 15), 0)
        case "edges":
            imgProcessed = cv2.Canny(img, 100, 200)
        case "resize":
            imgProcessed = cv2.resize(img, (300, 300))  # Resize to 300x300
        case "rotate":
            imgProcessed = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        case _:
            return None

    # Save the processed image for all other cases
    newFilename = f"static/saved/{filename}"
    cv2.imwrite(newFilename, imgProcessed)
    return newFilename

    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        operation = request.form.get("operation")
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('home'))
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('home'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_file_path = processImage(filename, operation)

            if new_file_path is None:  # If image processing failed
                flash("Image processing failed. Please try again.")
                return redirect(url_for('home'))

            # Pass the processed image URL to the result page
            processed_image_url = new_file_path.replace("static/", "/static/")
            return render_template("result.html", processed_image_url=processed_image_url)

    return render_template("index.html")


app.run(debug=False, host='0.0.0.0', port=port)
