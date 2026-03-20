def check_url(url):
    score = 0

    if len(url) > 75:
        score += 1

    if '@' in url:
        score += 1

    suspicious_words = ['login', 'verify', 'bank', 'update', 'secure']
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    if not url.startswith("https"):
        score += 1

    if score >= 2:
        return "⚠️ Unsafe (Phishing Detected)"
    else:
        return "✅ Safe (No Threat Detected)"