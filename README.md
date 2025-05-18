# 💤 Sleepy Sites Scanner

**A Python tool that scans websites and classifies them as Active, Possibly Inactive, or Dormant based on their last updated content.**  
Perfect for identifying outdated or "sleeping" websites!

---

## 🧠 What It Does

- Takes a list of URLs from `urls.txt`
- Uses headless Selenium to load each site
- Tries to detect the last updated date of the site
- Categorizes websites as:
  - 🟢 Active (updated in last 60 days)
  - 🟡 Possibly Inactive (60–365 days)
  - 🔴 Dormant (not updated in over a year)
- Saves results in a clean CSV file: `results.csv`

---

## 🛠️ How to Use

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/sleepy-sites-scanner.git
   cd sleepy-sites-scanner

