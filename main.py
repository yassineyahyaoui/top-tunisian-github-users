from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://github.com/gayanvoice/top-github-users/blob/main/markdown/total_contributions/tunisia.md")

driver.implicitly_wait(60)
avatars_list = driver.find_elements(By.CSS_SELECTOR, "table td a img[width='24']")

users_list = []

for avatar in avatars_list:
    users_list.append(avatar.get_attribute("alt")[10:])

for user in users_list:
    driver.get("https://github.com/" + user)
    print(driver.find_element(By.CSS_SELECTOR, ".js-yearly-contributions .position-relative h2.f4.text-normal.mb-2").text[:-31])


# driver.implicitly_wait(60)
# email = driver.find_element(By.CSS_SELECTOR, "input#login_field")
# password = driver.find_element(By.CSS_SELECTOR, "input#password")
#
# email.send_keys("muhamedyaseenyahyaoui@gmail.com")
# password.send_keys("mayway2805")
#
# driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary.btn-block.js-sign-in-button").click()
