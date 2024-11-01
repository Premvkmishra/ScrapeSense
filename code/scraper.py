import time
import csv
from random import choice
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# User-Agent strings to mimic different browsers
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
]

# URL to scrape
url = 'https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/'

def scrape_data():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument(f"user-agent={choice(user_agents)}")  # Set a random user-agent

    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(url)

        # Use WebDriverWait to wait for the elements to be present
        wait = WebDriverWait(driver, 10)  # 10 seconds timeout

        # Locate product name and price using the updated selectors
        product_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[data-qa^="pdp-name"]'))).text.strip()
        price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-qa^="pdp-price"]'))).text.strip()

        # Placeholder values for brand and seller
        brand = "Brand not found"  # Update this with the correct selector after inspecting
        seller = "Seller not found"  # Update this with the correct selector after inspecting

        # Example: Update brand and seller selectors as needed
        try:
            brand = driver.find_element(By.CSS_SELECTOR, 'div.brand-class').text.strip()  # Replace with actual selector
            seller = driver.find_element(By.CSS_SELECTOR, 'div.seller-class').text.strip()  # Replace with actual selector
        except Exception as e:
            print("Brand or seller not found:", e)

        # Save file in current working directory
        with open('noon_products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Price', 'Brand', 'Seller'])  # Write headers

            # Write product details to CSV
            writer.writerow([product_name, price, brand, seller])
            print("Product scraped successfully:", product_name, price, brand, seller)

        print("Scraping complete. Data saved to noon_products.csv.")
    except Exception as e:
        print(f"Error fetching the URL: {e}")
    finally:
        driver.quit()  # Close the WebDriver

if __name__ == '__main__':
    start_time = time.time()
    scrape_data()
    print(f"Scraping finished in {time.time() - start_time} seconds.")
