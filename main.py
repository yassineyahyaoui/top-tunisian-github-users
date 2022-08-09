from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://github.com/gayanvoice/top-github-users/blob/main/markdown/total_contributions/tunisia.md")

driver.implicitly_wait(60)
my_list = driver.find_elements(By.CSS_SELECTOR, "table td a img[width='24']")

for item in my_list:
    print(item.get_attribute("alt"))


# driver.implicitly_wait(60)
# email = driver.find_element(By.CSS_SELECTOR, "input#login_field")
# password = driver.find_element(By.CSS_SELECTOR, "input#password")
#
# email.send_keys("muhamedyaseenyahyaoui@gmail.com")
# password.send_keys("mayway2805")
#
# driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary.btn-block.js-sign-in-button").click()
