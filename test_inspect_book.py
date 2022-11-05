from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_inspect_book():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://search.nlb.gov.sg/onesearch/Search?query=harry%20potter&cont=book")

    title = driver.title
    assert title == "OneSearch – Find book from libraries, archives and museums."

    driver.implicitly_wait(0.5)

    # search results
    bookList = driver.find_element(By.CSS_SELECTOR, "[id='bookCollapse']")

    bookDescription = bookList.find_element(By.CLASS_NAME, "media-body")
    bookName = bookDescription.find_element(By.CSS_SELECTOR, "[title='Harry Potter : a history of magic. ']")
    bookName.click()

    inspectTab = driver.window_handles[1]
    driver.switch_to.window(inspectTab)
    # switched to opened tab

    # now check for correct title
    bookTitle = driver.find_element(By.CSS_SELECTOR, "[class='card-title fullTitleh5']")
    bookTitleValue = bookTitle.text

    # value is different
    assert bookTitleValue == "Harry Potter : a history of magic"

    driver.quit()