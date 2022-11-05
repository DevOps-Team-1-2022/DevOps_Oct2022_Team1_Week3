from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_search_book():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/home")

    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    homeSearchInput = driver.find_element(By.CLASS_NAME, "input-group")
    # includes both search bar and search "go" button

    homeSearchBar = homeSearchInput.find_element(By.ID, "searchBox")
    homeSearchButton = homeSearchInput.find_element(By.CSS_SELECTOR, "[class='btn btn-primary height50']")
    
    homeSearchBar.send_keys("harry potter")
    homeSearchButton.click()

    searchTab = driver.window_handles[1]
    driver.switch_to.window(searchTab)
    # switched to opened tab

    # now check for "harry potter" in search bar
    searchSearchBar = driver.find_element(By.CSS_SELECTOR, "[class='input-group']")
    # GG MY NAMING CONVENTION
    searchSearchBarValue = searchSearchBar.find_element(By.ID, "query")
    value = searchSearchBarValue.get_attribute("value")
    assert value == "harry potter"

    driver.quit()