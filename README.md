# 📝 VisionTextExtractor - Document Text Extraction using Google Cloud Vision API

This project, **VisionTextExtractor**, uses **Google Cloud Vision API** to extract text from **local images**. 🖼️🔍

## ✨ Features
- ✅ Supports **only local images** (no Google Cloud Storage required)
- 🚀 Uses **Google Cloud Vision API** for text extraction
- ⚠️ Error handling for missing or invalid images

## 🔧 Prerequisites
### 1️⃣ Install Dependencies
Ensure you have **Python 3.7+** installed and install required packages:
```bash
pip install google-cloud-vision
```

### 2️⃣ Set Up Google Cloud Vision API
- 🔑 Create a **Google Cloud account** and enable the **Vision API**
- 🗝️ Generate a **Service Account Key** (JSON file)
- 🌍 Set the environment variable for authentication:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-key.json"
  ```
  **(For Windows, use `set` instead of `export`)**

## 🚀 Usage
### 1️⃣ Place Your Image in a Local Directory 📂
Ensure your image (e.g., `image.jpg`) is saved locally.

### 2️⃣ Run the Script ▶️
Modify `image_path` in `temp.py` and execute:
```bash
python temp.py
```

### 3️⃣ Output 📜
If successful, the script will print extracted text from the image.

## 🛠️ Troubleshooting
- ❌ **FileNotFoundError**: Ensure the image path is correct.
- 🔑 **Authentication Error**: Ensure the service key JSON file is correctly set.
- 📭 **Empty Output**: The image may not contain readable text.

## 📜 License
This project is licensed under the **MIT License**.

