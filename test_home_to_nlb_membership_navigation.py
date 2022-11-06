from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

def test_render_facilities():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    action = ActionChains(driver)
    driver.get("https://www.nlb.gov.sg/main/home")

    # Check page title
    title = driver.title
    assert title == "Home"

    # Click "NLB Membership" button
    usingTheLibraryElement = driver.find_element(By.CSS_SELECTOR, "a[href='/main/services/library-membership")
    usingTheLibraryElement.click()

    # Check url
    url = driver.current_url
    assert url == "https://www.nlb.gov.sg/main/services/library-membership"

    # Check page title
    assert driver.title == "Library Membership"

    driver.quit()