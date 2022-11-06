from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

def test_navigate_library_location():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/home")

    # Check page title
    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    # Click on Visit us  button
    visit_us_button = driver.find_element(
        by=By.ID, value="discover-menu-name-41")
    # Click on our libraries and locations 
    library_location_button = driver.find_element(by=By.ID, value="2-navdetail-1")

    action = ActionChains(driver)
    action.move_to_element(visit_us_button).perform()
    action.move_to_element(library_location_button).perform()
    #click on all libraries and locations 
    our_role_button = driver.find_element(
        by=By.PARTIAL_LINK_TEXT, value="All Libraries and Locations")
    action.move_to_element(our_role_button).click(our_role_button).perform()

    # Check url
    url = driver.current_url
    assert url == "https://www.nlb.gov.sg/main/visit-us/our-libraries-and-locations"

    # Chekc page title 
    assert driver.title == "Our Libraries & Locations"

    driver.quit()