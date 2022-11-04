from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

"""
This is to test that the search button renders the search form when clicked 
"""

def test_render_global_search():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    # NLB Home Page
    driver.get("https://www.nlb.gov.sg/main/home")

    # Wait to load because not everyone's wifi is fast
    driver.implicitly_wait(2)

    #If small screen need to click to open the hamburger button to get search_btn
    width = driver.get_window_size()["width"]
    if(width < 1200):
        hamburger_btn =  driver.find_element(by=By.CLASS_NAME, value="navbar-toggler")
        hamburger_btn.click()

    # click search button
    search_btn = driver.find_element(by=By.ID, value="btnOpenTopSearchModal")
    search_btn.click()

    # check input form with correct placeholder
    input_form = driver.find_element(By.XPATH, "//input[@id='navSearch']")
    input_form_txt = input_form.get_attribute("placeholder") 
    assert input_form_txt == "What would you like to find?"

    # check search submit button with correct "Search" text , if small apparently no button (ask the UX designer)
    if(width > 1000):
        submit_search_btn = driver.find_element(By.XPATH, "//input[@id='navSearch']/following-sibling::button")
        assert submit_search_btn.text == "Search"

    #  check search option: Catalogue , OneSearch, Search within this site

    #  small screen
    if(width < 1000):
        search_option_btn = driver.find_element(By.ID, "mobileScopeDropdown")
        search_option_btn.click()
        submit_option_dropdown = driver.find_element(By.CSS_SELECTOR,"[aria-labelledby='mobileScopeDropdown']")
        children = submit_option_dropdown.find_elements(By.XPATH, "./*")
        assert len(children) == 3

        catalogue =children[0].find_elements(By.XPATH, "./*")[1] 
        one_search = children[1].find_elements(By.XPATH, "./*")[1] 
        within_site = children[2].find_elements(By.XPATH, "./*")[1] 

        assert catalogue.text == "Catalogue"
        assert one_search.text == "OneSearch"
        assert within_site.text == "Within This Site"

    # Not so small screen
    else:
        catalogue = driver.find_element(By.CSS_SELECTOR, "[for='searchLoc_Catalogue']")
        one_search = driver.find_element(By.CSS_SELECTOR, "[for='searchLoc_OneSearch']")
        within_site = driver.find_element(By.CSS_SELECTOR, "[for='searchLoc_within']")

        assert catalogue.text == "Catalogue"
        assert one_search.text == "OneSearch"
        assert within_site.text == "Search Within This Site"

         # check close button can click
        close_btn_container = driver.find_element(By.CLASS_NAME, "fa-times")
        close_btn_container.click()

   

    driver.quit()
    
test_render_global_search()