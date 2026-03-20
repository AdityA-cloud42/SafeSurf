# 🌐 SafeSurf - Advanced URL Safety Analyzer

SafeSurf is a web-based phishing URL detection tool built using Python and Flask. It analyzes URLs using rule-based techniques such as checking HTTPS security, suspicious keywords, URL length, and special characters to determine whether a link is safe or potentially malicious.

The application provides an interactive interface where users can input a URL and instantly receive a **risk score, classification, and detailed explanation**, helping them avoid phishing attacks.

---

## 🚀 Features

* 🔍 Detects phishing or suspicious URLs
* 📊 Risk scoring system (0–4 scale)
* ⚠️ Shows detailed reasons for classification
* 🔒 HTTPS security check
* 🧠 Keyword-based phishing detection
* 💻 Clean and modern UI

---

## 🛠️ Tech Stack

* Python
* Flask
* HTML / CSS

---

## 📌 How It Works

SafeSurf uses rule-based analysis to evaluate URLs:

* Checks if the URL uses HTTPS
* Detects special characters like `@`
* Looks for phishing-related keywords (login, verify, bank, etc.)
* Evaluates URL length

Based on these checks, it classifies the URL as:

* ✅ **Safe (No Threat Detected)**
* ⚠️ **Unsafe (Phishing Detected)**

---

## 📷 Screenshots

### ✅ Safe URL Detection

![Safe Output](screenshots/safe.png)

### ⚠️ Unsafe URL Detection

![Unsafe Output](screenshots/unsafe.png)

---

## ▶️ Run Locally

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the application:

```
python app.py
```

3. Open in browser:

```
http://127.0.0.1:5000
```

---

## 📌 Future Improvements

* 🤖 Machine Learning-based phishing detection
* 🌐 API integration (Google Safe Browsing)
* 📊 URL history tracking
* 🎨 Enhanced UI/UX

---

## 👨‍💻 Author

Aditya

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
