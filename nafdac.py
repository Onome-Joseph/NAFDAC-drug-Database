import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL structure
BASE_URL = "https://greenbook.nafdac.gov.ng/products/details/{:02d}"

# Headers for CSV
columns = [
    "Product name", "ROA", "Applicant Name", "NRN", "Status", "Composition",
    "ATC Code/ATCvet Code", "Product Category", "Marketing Category", "Packsize",
    "Product Description", "Manufacturer Name", "Manufacturer Country", 
    "Approval Date", "Expiry Date"
]

# List to store scraped data
data = []

# Range of pages to scrape (from 2 to 7907 inclusive)
for page_id in range(2, 7908):
    url = BASE_URL.format(page_id)
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Skipping {url} - Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract values from left (card) and right column
        left_card = soup.select_one(".naf-card .card-body")
        right_column = soup.select_one(".col-md-7 .row")

        # Helper function to get value by header name
        def get_value(container, header_text):
            tag = container.find("h1", string=lambda x: x and header_text.lower() in x.lower())
            return tag.find_next_sibling("p").get_text(strip=True) if tag else ""

        product_name = left_card.find("h1").get_text(strip=True) if left_card else ""
        spans = left_card.find_all("span") if left_card else []
        composition_dose = " ".join([s.get_text(strip=True) for s in spans])
        roa = get_value(left_card, "ROA")
        applicant_name = get_value(left_card, "Applicant Name")
        nrn = get_value(left_card, "NRN")
        status = get_value(left_card, "Status")

        composition = get_value(right_column, "Composition")
        atc_code = get_value(right_column, "ATC Code")
        product_category = get_value(right_column, "Product Category")
        marketing_category = get_value(right_column, "Marketing Category")
        packsize = get_value(right_column, "Packsize")
        product_description = get_value(right_column, "Product Description")
        manufacturer_name = get_value(right_column, "Manufacturer Name")
        manufacturer_country = get_value(right_column, "Manufacturer Country")
        approval_date = get_value(right_column, "Approval Date")
        expiry_date = get_value(right_column, "Expiry Date")

        # Add row
        data.append([
            product_name, roa, applicant_name, nrn, status, composition,
            atc_code, product_category, marketing_category, packsize,
            product_description, manufacturer_name, manufacturer_country,
            approval_date, expiry_date
        ])

        print(f"Scraped page {page_id}")
        time.sleep(0.5)  # Respectful delay to avoid overloading the server

    except Exception as e:
        print(f"Error on page {page_id}: {e}")
        continue

# Save to CSV
df = pd.DataFrame(data, columns=columns)
df.to_csv("nafdac_products.csv", index=False)
print("Scraping complete. Data saved to nafdac_products.csv.")
