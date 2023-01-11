from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome("/Users/evansala/Downloads/chromedriver")
url = "https://yugipedia.com/wiki/High_Mage_Anubisius"
driver.get(url)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[3]/a')))
POW_TEC_BCD_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[3]/a")
POW_TEC_BCD_button.send_keys(Keys.RETURN)
# POW_TEC_BCD_button.click()
# time.sleep(5)

pow_tec_bcd_list = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/div[2]/table").text
print(pow_tec_bcd_list)

# wait = WebDriverWait(driver, 10)
# element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[1]")))
# driver.implicitly_wait(7)
# time.sleep(5)
# TEC_SA = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[1]")
# TEC_SA.click()
# element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[3]")))
#
#
# driver.implicitly_wait(7)
# POW_SA = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[4]/div/div[2]/ul/li[3]")
# POW_SA.click()

driver.close()
