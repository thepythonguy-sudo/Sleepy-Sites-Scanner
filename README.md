```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/thepythonguy-sudo/sleepy-sites-scanner/main/assets/sleepy_logo.png" width="200" alt="Sleepy Sites Logo"/>
</p>

<h1 align="center">😴 Sleepy Sites Scanner</h1>

<p align="center">
  <i>Shhh... kuch websites ab so chuki hain — aur ye tool unhe dhoond nikaalega 💡</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square">
  <img src="https://img.shields.io/github/forks/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square">
  <img src="https://img.shields.io/github/issues/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square">
  <img src="https://img.shields.io/github/license/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square">
</p>

---

## 🧠 About the Project

**Sleepy Sites Scanner** ek Python based web scraping tool hai jo internet ke kone kone me soyi hui websites ko dhoondta hai — yaani aise sites jo kabhi update hi nahi hoti.

Use cases:
- Broken or dormant website detection
- Domain flipping & acquisition research
- Internet archives ke liye content tracking

---

## 🚀 Features

- ✅ Takes list of URLs from a `.txt` file  
- ✅ Checks for HTTP response codes and last updated content  
- ✅ Detects signs of "sleepiness" (404s, static timestamps, no updates, etc.)  
- ✅ Stores results neatly in a CSV  
- ✅ Fully open-source & customizable  
- ✅ Lightweight — BeautifulSoup + Requests based (no browser needed)

---

## 🗂️ Project Structure

```

sleepy-sites-scanner/
│
├── assets/                  # Logos, images etc.
│
├── data/
│   ├── urls.txt             # Your list of websites to scan
│   └── results.csv          # Output after scanning
│
├── src/
│   └── sleepy\_scanner.py    # The main engine
│
├── requirements.txt         # Python dependencies
└── README.md                # You're reading it!

````

---

## 📥 Installation

```bash
git clone https://github.com/thepythonguy-sudo/sleepy-sites-scanner.git
cd sleepy-sites-scanner
pip install -r requirements.txt
````

---

## ⚙️ Usage

1. **Prepare your URLs**

`data/urls.txt` me har line pe ek URL likh do:

```
https://example.com
https://another-site.org
```

2. **Run the Scanner**

```bash
python3 src/sleepy_scanner.py
```

3. **Check Results**

`data/results.csv` me aayega sab kuch — status, titles, last modified etc.

---

## 📸 Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/thepythonguy-sudo/sleepy-sites-scanner/main/assets/demo_result.png" width="700" alt="Output Screenshot"/>
</p>

---

## 🛠️ Built With

* Python 3
* BeautifulSoup
* Requests
* CSV Module
* Your brain 🧠

---

## 👑 Creator

Made with 💙 by [thepythonguy-sudo](https://github.com/thepythonguy-sudo)

---

## 🧨 Future Plans

* Add Selenium support for JavaScript-heavy pages
* GitHub Actions for auto-checking sites weekly
* Live dashboard for monitoring scanned sites
* Docker support

---

## 📜 License

MIT — use it, fork it, star it, break it — just give credit 🙏

---

<p align="center">
  <strong>✨ Sleepy Sites Scanner ✨</strong><br>
  <i>"Internet ke kabristan me ghus ke soney waali sites ko jagana mera kaam hai!"</i>
</p>
```

---

