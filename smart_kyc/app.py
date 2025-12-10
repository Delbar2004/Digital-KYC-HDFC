print("--- INITIALIZING SYSTEM ---")
from flask import Flask, request, jsonify, render_template
import os
import easyocr  # New Library
from quality_check import analyze_image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# Load OCR Reader (This runs once when server starts)
print("--- LOADING OCR MODEL (Wait 10s...) ---")
reader = easyocr.Reader(['en']) 
print("--- SYSTEM READY ---")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-id', methods=['POST'])
def upload_id():
    if 'file' not in request.files: return jsonify({"message": "No file"}), 400
    file = request.files['file']

    # 1. Advanced Quality Check
    is_valid, score, message = analyze_image(file)

    if not is_valid:
        return jsonify({
            "status": "fail", 
            "message": f"❌ {message} (Score: {int(score)})"
        }), 400

    # 2. Save File
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)

    # 3. Perform OCR (Read Text)
    try:
        results = reader.readtext(save_path, detail=0)
        extracted_text = ", ".join(results) # Join all found text
    except:
        extracted_text = "Could not read text"

    return jsonify({
        "status": "success",
        "message": "✅ ID Verified & Scanned!",
        "extracted_text": extracted_text[:100] + "..." # Send text back to phone
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)