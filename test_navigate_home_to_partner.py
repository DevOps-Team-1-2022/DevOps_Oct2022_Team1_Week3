from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

"""
This is to test that the partner us button is indeed going to parner us page
"""

def test_navigate_home_to_partner():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    # NLB Home Page
    driver.get("https://www.nlb.gov.sg/main/home")

    # Wait to load because not everyone's wifi is fast
    driver.implicitly_wait(2)

    # Many many container, click on partner us
    partner_us_container = driver.find_elements(By.XPATH, "//button[@class='buttonParallelogram secondaryBorder']")[5]
    partner_us_redirect = partner_us_container.find_elements(By.XPATH, "./*")[0]
    partner_us_redirect.click()
    
    # Check breadcrumb element, it is really in partner us page
    breadcrumb = driver.find_element(By.CLASS_NAME,"introTitleColor").find_elements(By.XPATH, "./*")
    home = breadcrumb[0]
    partner_us = breadcrumb[1]

    assert home.text == "Home"
    assert partner_us.text == "Partner Us"


    driver.quit()
    
test_navigate_home_to_partner()