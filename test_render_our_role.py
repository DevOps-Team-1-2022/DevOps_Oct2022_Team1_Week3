from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def test_navigate_our_role():
    driver = webdriver.Chrome(service=ChromeService(
        executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/about-us/About-NLB/our-role")
    driver.maximize_window()
    driver.implicitly_wait(1)

    breadcrumb = driver.find_element(
        by=By.ID, value="breadcrumbcomponent")
    assert breadcrumb.text == "Home / About Us / About NLB / Our Role"
    descTitle = driver.find_element(
        by=By.CLASS_NAME, value="descTitle")
    assert descTitle.text == "Our Role"
    descText = driver.find_element(
        by=By.CLASS_NAME, value="descText")
    assert descText.text == "Understand the roles of the Libraries and Archives."
    contentTitle = driver.find_element(by=By.XPATH,
                                       value="//h1[text()='NLB Act & Statutory Functions']")
    contentBody = driver.find_element(By.ID, value="collapseNotes-1")
    assert contentBody.text == '''The National Library Board (NLB) is a statutory board established under the National Library Board Act (Chapter 197) (NLB Act). The NLB Act sets out the NLB’s functions and powers.\nThe functions of the NLB include the following:\nto establish libraries (such as the National Library and Public Libraries) and to administer the National Archives of Singapore (NAS) including the Oral History Centre under NAS\nto promote reading and encourage learning through the use of libraries.\nto provide a repository of library materials published in Singapore.\nto acquire a comprehensive collection of library materials relating to Singapore and its people.\nto provide a repository of archives of national or historical significance and to facilitate access to these archives.\nto conduct records management programmes for the Government including setting standards and procedures.\nto record, preserve and disseminate the history of Singapore through oral history.\nto share information on library and archival collections by any means including through publications and exhibitions.\nNLB has the power to do all things necessary or convenient to be done in connection with its functions including the following:\nto make copies of any online material available on a Singapore website.\nto require that library materials (print and electronic versions) published in Singapore be deposited with NLB.\nto require that public records of national or historical significance be transferred to NAS.\nto require that sound or audio-visual recordings that have been broadcasted or made public be deposited with NAS.\nto acquire by purchase, donation or otherwise any library or archival materials of national or historical significance.\nto collaborate with other libraries, information providers, archives and oral history centres.\nto undertake and facilitate research on libraries, librarianship, archives, archival work and oral history.\nto enter into contracts.\nto form or participate in the formation of a company.\nto charge fees, commissions or rent for any services or facilities provided.\nThe NLB may make regulations for carrying out the purposes of the NLB Act. There is currently only one set of regulations under the NLB Act – NLB (Fees and Charges) Regulations.'''

    driver.quit()
