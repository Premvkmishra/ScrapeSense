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


user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
]


url = 'https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/'

def scrape_data():
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument(f"user-agent={choice(user_agents)}")  

    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(url)

        
        wait = WebDriverWait(driver, 10) 

       
        product_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[data-qa^="pdp-name"]'))).text.strip()
        price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-qa^="pdp-price"]'))).text.strip()

        
        brand = "Brand not found"  
        seller = "Seller not found"  

       
        try:
            brand = driver.find_element(By.CSS_SELECTOR, 'div.brand-class').text.strip()  
            seller = driver.find_element(By.CSS_SELECTOR, 'div.seller-class').text.strip()  
        except Exception as e:
            print("Brand or seller not found:", e)

        
        with open('noon_products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Price', 'Brand', 'Seller'])  # Write headers

           
            writer.writerow([product_name, price, brand, seller])
            print("Product scraped successfully:", product_name, price, brand, seller)

        print("Scraping complete. Data saved to noon_products.csv.")
    except Exception as e:
        print(f"Error fetching the URL: {e}")
    finally:
        driver.quit()  

if __name__ == '__main__':
    start_time = time.time()
    scrape_data()
    print(f"Scraping finished in {time.time() - start_time} seconds.")
