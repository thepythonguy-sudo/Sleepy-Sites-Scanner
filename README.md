

![Sleepy Sites Scanner Logo](https://raw.githubusercontent.com/thepythonguy-sudo/sleepy-sites-scanner/main/assets/sleepy_logo.png)

# 😴 Sleepy Sites Scanner

*Shhh... kuch websites ab so chuki hain — aur ye tool unhe dhoond nikaalega 💡*

![Stars](https://img.shields.io/github/stars/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square)
![Forks](https://img.shields.io/github/forks/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square)
![Issues](https://img.shields.io/github/issues/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square)
![License](https://img.shields.io/github/license/thepythonguy-sudo/sleepy-sites-scanner?style=flat-square)

---

## 🧠 About the Project

**Sleepy Sites Scanner** ek Python based web scraping tool hai jo internet ke kone kone me soyi hui websites ko dhoondta hai — yaani aise sites jo kabhi update hi nahi hoti.

**Use cases:**
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
├── assets/
│   └── sleepy\_logo.png
├── data/
│   ├── urls.txt
│   └── results.csv
├── src/
│   └── sleepy\_scanner.py
├── requirements.txt
└── README.md

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

`data/urls.txt` me har line pe ek URL likho:

```
https://example.com
https://another-site.org
```

2. **Run the Scanner**

```bash
python3 src/sleepy_scanner.py
```

3. **Check Results**

`data/results.csv` me milenge sare results — status, title, timestamp etc.

---

## 🛠️ Built With

* Python 3
* BeautifulSoup
* Requests
* CSV Module

---

## 🧨 Future Plans

* [ ] Selenium integration for JS-heavy pages
* [ ] Auto-scan on GitHub Actions
* [ ] Web dashboard to monitor status
* [ ] Docker support

---

## 👑 Author

Made with 💙 by [thepythonguy-sudo](https://github.com/thepythonguy-sudo)
*“Internet ke kabristan me ghus ke soney waali sites ko jagana mera kaam hai!”*

---

## 📜 License

MIT — use it, break it, fork it — just give credit 🙏

````

---

