from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def test_navigate_our_role():
    driver = webdriver.Chrome(service=ChromeService(
        executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/home")
    driver.maximize_window()
    driver.implicitly_wait(1)

    about_us_button = driver.find_element(
        by=By.ID, value="discover-menu-name-198")
    about_nlb_button = driver.find_element(by=By.ID, value="6-navdetail-1")

    action = ActionChains(driver)
    action.move_to_element(about_us_button).perform()
    action.move_to_element(about_nlb_button).perform()
    our_role_button = driver.find_element(
        by=By.PARTIAL_LINK_TEXT, value="Our Role")
    action.move_to_element(our_role_button).click(our_role_button).perform()

    assert driver.current_url == "https://www.nlb.gov.sg/main/about-us/About-NLB/our-role"

    driver.quit()
