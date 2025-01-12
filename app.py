from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import cv2
import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()


connection = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)


# port = int(os.environ.get("PORT", 8080))

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



@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        feedback_text = request.form['feedback']
        
        # Check if feedback content is empty
        if not feedback_text:
            flash("Feedback cannot be blank. Please provide your input.", "error")
            return redirect(url_for('feedback'))

        # Insert the feedback into the database
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO feedback (name, email, feedback_text) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, feedback_text))
                connection.commit()
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

        return redirect(url_for('feedback_received'))

    return render_template('feedback.html')

@app.route('/feedback_received')
def feedback_received():
    return render_template('feedback_received.html')

@app.route('/admin/feedback')
def view_feedback():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM feedback ORDER BY created_at DESC")
            feedback_data = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
        feedback_data = []

    return render_template('admin_feedback.html', feedback_data=feedback_data)


app.run(debug=True)
