# 🌐 SafeSurf - Phishing URL Detector

SafeSurf is a web-based application that helps users identify whether a given URL is **safe or potentially malicious (phishing)** using rule-based analysis.

---

## 🚀 Features

* 🔍 Detects phishing or suspicious URLs
* 🔒 Checks HTTPS security
* ⚠️ Identifies suspicious keywords (login, verify, bank, etc.)
* 📏 Analyzes URL length and structure
* 💻 Simple and user-friendly web interface

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **HTML / CSS**

---

## 📌 How It Works

SafeSurf analyzes URLs using multiple rules:

* Checks if the URL uses **HTTPS**
* Detects **special characters** like `@`
* Looks for **suspicious keywords**
* Evaluates **URL length**

Based on these checks, it classifies the URL as:

* ✅ **Safe (No Threat Detected)**
* ⚠️ **Unsafe (Phishing Detected)**

---

## ▶️ Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python app.py
```

### 3. Open in browser

```
http://127.0.0.1:5000
```

---

---

## 📌 Future Improvements

* 🤖 Machine Learning-based detection
* 🌐 Integration with phishing detection APIs
* 🎨 Improved UI/UX
* ☁️ Live deployment

---

## 👨‍💻 Author

Aditya

---

## ⭐ If you like this project

Give it a star on GitHub!
