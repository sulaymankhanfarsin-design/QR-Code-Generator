from flask import Flask, render_template, request
import qrcode
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the folder where QR codes will be saved
STATIC_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_image_path = None  # Variable to hold the path to the QR image

    if request.method == 'POST':
        # Get the URL from the form
        url = request.form['url']
        
        if url: # Check if the URL is not empty
            # Generate the QR code
            img = qrcode.make(url)
            
            # Define the file path to save the QR code
            # We'll always overwrite the same file to save space
            qr_image_path = os.path.join(STATIC_FOLDER, 'qr_code.png')
            
            # Save the image
            img.save(qr_image_path)
            
            # Pass the file path to the template
            # We pass 'qr_code.png' because the HTML src is relative to 'static'
            qr_image_path = 'qr_code.png'

    # Render the HTML page. 
    # If a POST request was made, qr_image_path will have a value.
    # If it was a GET request, it will be None.
    return render_template('index.html', qr_image_path=qr_image_path)

# This allows you to run the app by just running `python app.py`
if __name__ == '__main__':
    app.run(debug=True)