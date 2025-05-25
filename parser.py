import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd

pages_to_parse = 10

base_url = "https://pricing.parts/ru/spares?page="
file_path = "table.xlsx"

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

results = []

print(f'Парсинг: {pages_to_parse} стр.\nТоваров: {pages_to_parse * 50}шт.')

for page in range(1, pages_to_parse + 1):
    url = f"{base_url}{page}"
    print(f"🔎 Парсинг страницы {page}: {url}")
    driver.get(url)
    rows = driver.find_elements(By.CSS_SELECTOR, "tr")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 4:
            brand = cols[0].text.strip()
            part_number = cols[1].text.strip()
            description = cols[2].text.strip()
            price_text = cols[3].text.strip()
            
            if price_text.count("$") >= 2:
                price_rub = price_text.split("$")[2].strip()
                price_rub_min = price_rub.split('—')[0].strip()
                price_rub_max = price_rub.split('—')[1].strip()
            else:
                price_rub = price_text

            results.append({
                "Марка": brand,
                "Номер запчасти": part_number,
                "Описание": description,
                "Цена мин(руб)": price_rub_min,
                "Цена макс(руб)": price_rub_max
            })

df = pd.DataFrame(results)
df.to_excel(file_path, index=False, engine='openpyxl')