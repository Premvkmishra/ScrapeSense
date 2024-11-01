# 🛍️ Noon Product Scraper and Analysis

This project is a Python-based tool designed to **scrape product data** from a Noon webpage and **perform insightful analysis** on the extracted data. It leverages **Selenium** for web scraping and **pandas** for data analysis, focusing on speed, efficiency, and accuracy.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Scrape the Data](#step-1-scrape-the-data)
  - [Step 2: Analyze the Data](#step-2-analyze-the-data)
- [Files](#files)
- [Results and Analysis](#results-and-analysis)
  - [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)

---

## 📌 Overview

This tool provides:
1. **Scraping of product details** (name, price, brand, seller) from the [Noon website](https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/).
2. **Data storage in CSV format** for easy access and manipulation.
3. **Data Analysis** to gather insights, such as finding the most and least expensive products, counting items by brand and seller, and creating visual distributions.

---

## ✨ Features

- **Efficient Web Scraping**: Fast and accurate scraping using Selenium and user-agent switching.
- **Proxy Integration**: Proxy usage to avoid IP blocks during data extraction.
- **Data Insights**: Detailed analysis of scraped data to derive meaningful insights.
- **Visual Representations**: Bar charts showcasing brand and seller distributions.

---

## 📋 Requirements

Ensure you have the following installed:

- **Python 3.7+**
- Required Libraries: `selenium`, `pandas`, `matplotlib`, `webdriver_manager`

Install these via pip:

```bash
pip install selenium pandas matplotlib webdriver_manager

🔧 Installation
Clone the repository:

```bash`
git clone https://github.com/your-username/noon-product-scraper.git
cd noon-product-scraper
Install dependencies:


pip install -r requirements.txt
🚀 Usage
Step 1: Scrape the Data
Run the scraper.py script to scrape product details and save them to a CSV file:

```bash
python scraper.py
This generates a file noon_products.csv containing:

Product Name
Price
Brand
Seller
Step 2: Analyze the Data
Run analysis.py to analyze the data and generate visual insights:

```bash
python analysis.py
The analysis will be printed in the console, highlighting the most and least expensive products and showing counts by brand and seller.
A graph file analysis_graphs.png will be saved in the assets folder.

📂 Files
scraper.py: Script for scraping product data. Includes proxy support and random user-agent selection.
analysis.py: Script for analyzing scraped data, cleaning it, and generating insights.
noon_products.csv: Output file with scraped product details.
assets/analysis_graphs.png: Bar chart visualization of the product distribution by brand and seller.

📊 Results and Analysis
The analysis script (analysis.py) performs the following:

Data Cleaning: Removes rows with missing values.
Most Expensive Product: Displays the most costly product.
Cheapest Product: Shows the least costly product.
Product Count by Brand: Counts products for each brand.
Product Count by Seller: Counts products for each seller.
Visualization
Brand Distribution: Bar chart showing the count of products by brand.
Seller Distribution: Bar chart showing the count of products by each seller.
The charts are saved as analysis_graphs.png in the assets folder.

🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request with suggestions or enhancements.

📜 License
This project is open source and available under the MIT License. Please follow all assignment guidelines regarding usage and sharing.