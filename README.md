# Smart Digital KYC System 🏦 ✅

### *Reducing Customer Drop-off & Boosting Conversion Rates in Banking*

## 📌 Project Overview
Traditional banking KYC (Know Your Customer) processes are often slow, requiring physical visits or cumbersome file uploads, leading to high user drop-off rates (30-40%). 

**This project offers a solution:** A frictionless, web-based Digital KYC system that allows users to instantly capture and verify identity documents using their mobile or laptop camera without installing any apps.

## 🎯 Problem Statement
* **The Issue:** High friction during customer onboarding leads to abandoned applications.
* **The Solution:** A "Phase 3" Digital KYC implementation that is browser-based, fast, and works across devices on a local network.
* **The Goal:** Reduce onboarding time from 10 minutes to under 30 seconds.

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **Frontend:** HTML5, CSS, JavaScript (MediaDevices API)
* **Image Processing:** OpenCV (`cv2`), NumPy
* **Data Transfer:** AJAX / JSON (Base64 Encoding)

## ✨ Key Features
* **📸 Live Camera Capture:** Accesses device camera directly in the browser.
* **📱 Cross-Device Support:** Host on a laptop, access via mobile phone on the same WiFi.
* **⚡ Real-time Uploads:** Images are converted to Base64 and processed instantly by the Flask server.
* **📂 Automated Storage:** Captures are automatically saved with unique timestamps in the server backend.

## 📂 Project Structure
```text
DigitalKYC/
│
├── app.py              # Main Flask Application (Server Logic)
├── templates/
│   └── index.html      # Frontend UI (Camera & Capture Logic)
├── static/
│   └── uploads/        # Directory where captured KYC images are saved
└── README.md           # Project Documentation# Digital-KYC-HDFC
Web-based KYC image capture system using Python, Flask, and OpenCV. Features cross-device support (Mobile-to-Localhost) for instant identity verification without app installation.
