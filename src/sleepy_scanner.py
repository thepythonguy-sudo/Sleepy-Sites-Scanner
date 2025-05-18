import csv
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# Utils
HEADLESS = True
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
DATE_FORMATS = ["%B %d, %Y", "%d %B %Y", "%Y-%m-%d"]  # Add more if needed


def get_driver():
    options = Options()
    if HEADLESS:
        options.add_argument("--headless")
    options.add_argument(f"user-agent={USER_AGENT}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def load_urls(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def get_page_source(url):
    try:
        driver = get_driver()
        driver.get(url)
        time.sleep(5)  # Wait for page load
        html = driver.page_source
        last_modified = driver.execute_script("return document.lastModified")
        driver.quit()
        return html, last_modified
    except Exception as e:
        print(f"Error loading {url}: {e}")
        return None, None


def parse_date_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    possible_tags = soup.find_all(['time', 'span', 'p'])
    for tag in possible_tags:
        text = tag.get_text(strip=True)
        for fmt in DATE_FORMATS:
            try:
                return datetime.strptime(text, fmt)
            except:
                continue
    return None


def classify_site(post_date):
    if post_date is None:
        return "Unknown"
    days_old = (datetime.today() - post_date).days
    if days_old > 365:
        return "Dormant"
    elif days_old < 60:
        return "Active"
    else:
        return "Possibly Inactive"


def save_result(data, output_file="results.csv"):
    header = ["Website", "Last Updated", "Status"]
    write_header = not os.path.exists(output_file)
    with open(output_file, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        writer.writerow(data)


def main():
    urls = load_urls("urls.txt")
    for url in urls:
        print(f"\n🔍 Checking: {url}")
        html, fallback_date = get_page_source(url)
        if not html:
            save_result([url, "Error loading", "Error"])
            continue
        post_date = parse_date_from_html(html)
        if not post_date and fallback_date:
            try:
                post_date = datetime.strptime(fallback_date, "%m/%d/%Y, %I:%M:%S %p")
            except:
                post_date = None
        status = classify_site(post_date)
        readable_date = post_date.strftime("%Y-%m-%d") if post_date else "Unknown"
        print(f"   ➤ Last Update: {readable_date} | Status: {status}")
        save_result([url, readable_date, status])


if __name__ == "__main__":
    main()
