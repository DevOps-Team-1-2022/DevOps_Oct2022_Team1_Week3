from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

def test_loginD():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/home")

    # Check page title
    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    # Click on Visit us  button
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="a[href='https://cassamv2.nlb.gov.sg/cas/login?service=https%3a%2f%2fwww.nlb.gov.sg%2fmylibrary%2fcas&applicationId=NLB'")
    login_button.click()

    #Get the WebElement corresponding to the User Name
    username = driver.find_element(by=By.ID, value="username")
    #Get the webElement correspoding to the Password Field 
    password = driver.find_element(by=By.ID, value="password")

    username.send_keys("lincolnchia")
    password.send_keys("Test12345")

    enter_button = driver.find_element(by=By.NAME, value="submit")
    enter_button.click()

    get_url = driver.current_url
    # Chekck URL
    assert get_url == "https://www.nlb.gov.sg/mylibrary"

    driver.quit()