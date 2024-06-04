from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
import time 

URL = "https://physics.nist.gov/cgi-bin/Xcom/xcom2?Method=Elem&Output2=Hand"

driver = webdriver.Chrome()

for num in range(10):
    driver.get(URL)
    element = driver.find_element(By.NAME, "ZNum")
    element.send_keys(num)

    driver.find_element(By.NAME, "Submit Information").submit()

    try:
        driver.find_element(By.XPATH, '/html/body/form[2]/p/input[4]').click()

        coherent = driver.find_element(By.NAME, "coherent").click()
        incoherent = driver.find_element(By.NAME, "incoherent").click()
        photoelectric = driver.find_element(By.NAME, "photoelectric").click()
        pp_nuclear = driver.find_element(By.NAME, "nuclear").click()
        pp_electron = driver.find_element(By.NAME, "electron").click()
        tot_w_coherent = driver.find_element(By.NAME, "with").click()
        tot_wo_coherent = driver.find_element(By.NAME, "without").click()
    except NoSuchElementException:
        print("No element found")

    time.sleep(3)

    driver.find_element(By.NAME, "Download data").submit()

driver.quit()

