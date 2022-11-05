from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_render_facilities():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/services/facilities")

    # Check page title
    title = driver.title
    assert title == "Facilities"

    # Check page header
    header = driver.find_element(By.CLASS_NAME, "secondaryFont").text
    assert header == "Facilities"

    # Check card names
    cardNames = {"eNewspaper Stations":1, "Multimedia Stations":1, "Printing Services":1, "Book a Room or Venue":1, "Wifi at the Library":1}
    serviceCards = driver.find_elements(By.CSS_SELECTOR, "div[class = 'servicesCard']")
    for serviceCard in serviceCards:
        aTags = serviceCard.find_elements(By.TAG_NAME, "a")
        cardHeaderTag = aTags[0]
        assert cardNames[cardHeaderTag.text] == 1

    driver.quit()
