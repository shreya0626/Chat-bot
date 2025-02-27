import json
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Documentation URLs
CDP_URLS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

# "How-to" Questions
QUESTIONS = {
    "zeotap": [
        "How can I integrate my data with Zeotap?",
        "How do I create an audience in Zeotap?",
        "How do I activate data in Zeotap?"
    ]
}

# Configure WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_page(url):
    """Extracts all meaningful content from a page."""
    print(f"Scraping: {url}")

    driver.get(url)

    # Wait for JavaScript-rendered content
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(5)

    # Click expandable sections (if any)
    try:
        expand_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'expand')]")
        for button in expand_buttons:
            driver.execute_script("arguments[0].click();", button)
            time.sleep(2)
    except Exception:
        pass

    # Get subpage links
    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = [a["href"] for a in soup.find_all("a", href=True) if "docs.zeotap.com" in a["href"]]

    return soup.get_text(strip=True), links

def extract_answers(text, questions):
    """Finds relevant answers based on predefined questions."""
    answers = {}
    for question in questions:
        lower_question = question.lower()
        if lower_question in text.lower():
            start_idx = text.lower().find(lower_question)
            extracted_answer = text[start_idx: start_idx + 500]  # Extract surrounding text
            answers[question] = extracted_answer
        else:
            answers[question] = "No direct information found."
    return answers

def scrape_and_store():
    """Scrapes documentation and saves relevant answers."""
    structured_data = {}
    os.makedirs("data", exist_ok=True)

    for cdp, url in CDP_URLS.items():
        print(f"Scraping {cdp} documentation...")
        raw_text, sub_links = scrape_page(url)

        # Scrape subpages
        for sub_url in sub_links[:5]:  # Limit to avoid excessive requests
            sub_text, _ = scrape_page(sub_url)
            raw_text += "\n" + sub_text  # Merge texts

        structured_data[cdp] = extract_answers(raw_text, QUESTIONS.get(cdp, []))

        # Save to JSON
        with open(f"data/{cdp}.json", "w", encoding="utf-8") as f:
            json.dump({cdp: structured_data[cdp]}, f, indent=4)

    print("Scraping completed.")

if __name__ == "__main__":
    scrape_and_store()
    driver.quit()
