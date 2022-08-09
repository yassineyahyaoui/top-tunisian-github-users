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
    driver.implicitly_wait(60)
    try:
        name = driver.find_element(By.CSS_SELECTOR, "span.p-name.vcard-fullname.d-block.overflow-hidden").text
    except:
        name = "None"
    contribution = driver.find_element(By.CSS_SELECTOR, ".js-yearly-contributions .position-relative h2.f4.text-normal.mb-2").text[:-31]
    try:
        company = driver.find_element(By.CSS_SELECTOR, "li.vcard-detail.pt-1.css-truncate.css-truncate-target.hide-sm.hide-md span.p-org div").text
    except:
        company = "None"

    print(user, name, company, contribution)



# driver.implicitly_wait(60)
# email = driver.find_element(By.CSS_SELECTOR, "input#login_field")
# password = driver.find_element(By.CSS_SELECTOR, "input#password")
#
# email.send_keys("muhamedyaseenyahyaoui@gmail.com")
# password.send_keys("mayway2805")
#
# driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary.btn-block.js-sign-in-button").click()
