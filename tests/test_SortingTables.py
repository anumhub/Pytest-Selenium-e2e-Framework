from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []
    driver.get( "https://rahulshettyacademy.com/seleniumPractise/#/offers" )
    # click on column header
    before_first = driver.find_elements(By.XPATH, "//tr/td[1]")[0].text
    driver.find_element( By.XPATH, "//span[text()='Veg/fruit name']" ).click()
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.XPATH, "//tr/td[1]")) > 0 and
                  d.find_elements(By.XPATH, "//tr/td[1]")[0].text != before_first
    )
    # collect all veggie names -> BrowserSortedveggieList ( A,B, C)
    veggieWebElements = driver.find_elements( By.XPATH, "//tr/td[1]" )
    for ele in veggieWebElements:
        browserSortedVeggies.append( ele.text )

    originalBrowserSortedList = browserSortedVeggies.copy()

    # Sort this BrowserSortedveggieList => newSortedList -> (A,B,C)
    browserSortedVeggies.sort()

    assert browserSortedVeggies == originalBrowserSortedList


