from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import csv

search_term = input("Which bot do you want to search for? ")

options = ChromeOptions()
driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"), options=options)
driver.maximize_window()

initial_page_url = "https://bot-docs.cloudfabrix.io/Bots/search_bots/"
driver.get(initial_page_url)

selector = '#output-div a'

search_button = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
)

link = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{search_term}')]"))
    )
link.click()



WebDriverWait(driver, 120).until(EC.url_changes(initial_page_url))

results = []

details = {

    "Description" : WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.XPATH,"//p[contains(text(), 'Bot Position In Pipeline:')]/following-sibling::p"))).text,
    
}
results.append(details)
driver.quit()



with open("Scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file,
                            fieldnames = ["Description"])
    writer.writeheader()
    writer.writerows(results)