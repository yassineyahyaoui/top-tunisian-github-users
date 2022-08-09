from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://github.com/gayanvoice/top-github-users/blob/main/markdown/total_contributions/tunisia.md")

driver.implicitly_wait(60)
driver.find_element(By.CSS_SELECTOR, "a#raw-url").click()

driver.implicitly_wait(60)
full_content_raw = driver.find_element(By.CSS_SELECTOR, "pre").text

print(full_content_raw[6444:-5431])

driver.quit()


# driver.implicitly_wait(60)
# email = driver.find_element(By.CSS_SELECTOR, "input#login_field")
# password = driver.find_element(By.CSS_SELECTOR, "input#password")
#
# email.send_keys("muhamedyaseenyahyaoui@gmail.com")
# password.send_keys("mayway2805")
#
# driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary.btn-block.js-sign-in-button").click()
