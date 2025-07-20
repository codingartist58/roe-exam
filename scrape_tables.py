from playwright.sync_api import sync_playwright
import re

# Replace this with your actual list of URLs
seeds = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
urls = [f"https://sanand0.github.io/tdsdata/js_table/?seed={s}" for s in seeds]

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for url in urls:
        page.goto(url)
        numbers = page.locator("table td").all_text_contents()
        cleaned = [float(re.sub(r"[^\d.]", "", n)) for n in numbers if re.search(r"\d", n)]
        total_sum += sum(cleaned)

    print(f"Total sum: {total_sum}")
    browser.close()
