# 🏠 House Image Rating & Classification System

An AI-driven web application that analyzes a house image and generates:

- ⭐ **Rating** (e.g., 6/10)  
- 🏷️ **Category** — Poor / Middle / Good  
- ✍️ **Reason** — An explanation describing the visual quality of the house  

This project combines a clean frontend UI with a Flask backend and an AI-powered analysis module.

---

## 🌟 Features

- Upload a house image directly from the browser  
- Get instant predictions with detailed reasoning  
- Simple and responsive UI built with HTML, CSS, and JavaScript  
- AI module analyzes image quality using reference examples  
- Automatic cleanup of temporary images after prediction  

---

## 📂 Project Structure

```
project/
│
├── predictor.py # Flask backend server
├── POOR_MID_GOOD.py # AI evaluation module
│
├── static/
│ └── styles.css # Frontend styling
│
├── templates/
│ └── index.html # Main webpage with upload and output UI
│
├── train_images/ # Pre-labelled reference images
└── test_images/ # Temporary folder for uploaded images
├──  .env/ # Environment variable

```
---

## 🚀 How It Works

1. The user uploads a house image via the web interface.  
2. The backend saves the image and runs the AI analysis module.  
3. The AI model compares the image with labelled examples and produces:
   - A rating (e.g., "7/10")  
   - A quality category  
   - A text explanation  
4. The backend extracts these details and returns them as JSON.  
5. The frontend displays the prediction nicely to the user.  
6. The uploaded image is removed from the server after processing.

---

## 🛠 Technologies Used

- **Python (Flask)** — Backend server  
- **HTML, CSS, JavaScript** — Web frontend  
- **Google Generative AI - Gemini** — Image reasoning  
- **Base64** — Image encoding  
- **Regex** — Extracting structured results  

---

## 📦 Installation

1. Install dependencies:
   ```bash
   pip install flask google-generativeai python-dotenv gunicorn waitress requests pillow flask-cors

2. Set your environment variable (export for Linux or set for Windows):
   ```bash
   export API_KEY="your_api_key_here"
   
3. Start the Flask server:
   ```bash
   python predictor.py

## 🧪 Usage

- Click Upload Image
- Select a house image
- Click Predict
- View:
  - Rating
  - Category
  - Explanation
