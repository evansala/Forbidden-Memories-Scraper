from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("/Users/evansala/Downloads/chromedriver")
url = "https://yugipedia.com/wiki/High_Mage_Anubisius"
driver.get(url)

POW_TEC_BCD = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[2]")
time.sleep(10)
POW_TEC_BCD.click()
wait = WebDriverWait(driver, 10)
element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[1]")))

TEC_SA = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[1]")
time.sleep(10)
TEC_SA.click()
element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[3]")))


time.sleep(10)
POW_SA = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[3]")
POW_SA.click()

driver.close()
