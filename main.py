from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


driver = webdriver.Chrome()
driver.get("https://github.com/gayanvoice/top-github-users/blob/main/markdown/total_contributions/tunisia.md")

driver.implicitly_wait(60)
avatars_list = driver.find_elements(By.CSS_SELECTOR, "table td a img[width='24']")

users = []
users_list = []
for avatar in avatars_list:
    users_list.append(avatar.get_attribute("alt")[10:])

i = 1
for user in users_list:
    driver.get("https://github.com/" + user)
    driver.implicitly_wait(60)
    if driver.find_element(By.CSS_SELECTOR, "span.p-name.vcard-fullname.d-block.overflow-hidden").text != "":
        name = driver.find_element(By.CSS_SELECTOR, "span.p-name.vcard-fullname.d-block.overflow-hidden").text
    else:
        name = "No name"
    avatar = driver.find_element(By.CSS_SELECTOR, "img.avatar.avatar-user.width-full.border.color-bg-default").get_attribute("src")
    contribution = driver.find_element(By.CSS_SELECTOR, ".js-yearly-contributions .position-relative h2.f4.text-normal.mb-2").text[:-31]
    try:
        company = driver.find_element(By.CSS_SELECTOR, "li.vcard-detail.pt-1.css-truncate.css-truncate-target.hide-sm.hide-md span.p-org div").text
    except:
        company = "No company"

    print(i, user, name, avatar, company, contribution)
    users.append((i, user, name, avatar, company, contribution))
    print(users[i - 1])
    i = i + 1


now = datetime.now()
date = now.strftime("%Y %b %d %H:%M")





# driver.implicitly_wait(60)
# email = driver.find_element(By.CSS_SELECTOR, "input#login_field")
# password = driver.find_element(By.CSS_SELECTOR, "input#password")
#
# email.send_keys("muhamedyaseenyahyaoui@gmail.com")
# password.send_keys("mayway2805")
#
# driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary.btn-block.js-sign-in-button").click()
