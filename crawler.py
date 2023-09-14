from selenium import webdriver
from selenium.webdriver.common.by import By

# Define the URL of the website you want to crawl
base_url = "https://community.petcloud.com.au/portal/en/kb"

# Initialize the Selenium webdriver
driver = webdriver.Chrome()  # You can use other drivers like Firefox or Edge
visited_links = set()

def extract_links(url, depth=2):
    if depth == 0 or url in visited_links:
        return
    
    visited_links.add(url)

    driver.get(url)
    
    # Find all anchor (a) elements on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    

    # Extract and print the href attribute (link) from each anchor element
    for link in links:
        href = link.get_attribute("href")
        if href:
            print(href)
            # Recursively crawl the linked page
            extract_links(href, depth - 1)


extract_links(base_url, depth=2)

# Close the browser
driver.quit()
