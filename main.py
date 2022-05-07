import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service(r'C:\\Users\\Hackerman\\Downloads\\chromedriver.exe')
op = Options()
delay = 20
op.add_argument('start-minimized')
driver = webdriver.Chrome(options=op, service=ser)

driver.get("https://track.toggl.com/timer")

driver.find_element(By.ID, "email").send_keys("email")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.CLASS_NAME, "css-j3on6x-Button-Primary").send_keys(Keys.RETURN)

WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1f8yjlk-TimerButton-button')))
driver.find_element(By.CLASS_NAME, "css-1f8yjlk-TimerButton-button").send_keys(Keys.RETURN)

driver.get("https://www.youtube.com/watch?v=dsLsvshVvx4")
WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string'))).click()
driver.switch_to.frame(0)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span"))).click()
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)

subprocess.Popen(r"link_to_ide")