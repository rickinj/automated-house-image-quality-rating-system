# predictor.py (flask)
from flask import Flask, request, jsonify, render_template
import os
import subprocess
from pathlib import Path
import re

app = Flask(__name__)

TEST_IMAGE_DIR = r"path\to\test_images"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Clear any previous test images first
    for old in os.listdir(TEST_IMAGE_DIR):
        os.remove(os.path.join(TEST_IMAGE_DIR, old))

    # Save the new file in test_images folder
    filepath = os.path.join(TEST_IMAGE_DIR, file.filename)
    file.save(filepath)

    # Run your AI code (calls POOR_MID_GOOD.py)
    result = subprocess.run(
        ["python", "POOR_MID_GOOD.py"],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    # Extract rating, category, reason using regex
    rating_match = re.search(r"Rating[:\-]?\s*(\d+\/\d+|\d+)", output, re.I)
    category_match = re.search(r"Category[:\-]?\s*([A-Za-z]+)", output, re.I)
    reason_match = re.search(r"Reason[:\-]?\s*(.*)", output, re.I)

    # ✅ Delete the image after processing
    try:
        os.remove(filepath)
    except Exception as e:
        print(f"Warning: could not delete test image: {e}")

    return jsonify({
        "rating": rating_match.group(1) if rating_match else "",
        "category": category_match.group(1) if category_match else "",
        "reason": reason_match.group(1) if reason_match else output
    })

if __name__ == "__main__":
    app.run(debug=True)
