import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    now = datetime.now()
    date = now.strftime("%d %b %Y %H:%M")


    readme_head_file = open("readme-head.txt", "r")
    readme_head = readme_head_file.read()
    readme_head_file.close()

    readme_before_table_file = open("readme-before-table.txt", "r")
    readme_before_table = readme_before_table_file.read()
    readme_before_table_file.close()

    readme_after_table_file = open("readme-after-table.txt", "r")
    readme_after_table = readme_after_table_file.read()
    readme_after_table_file.close()

    readme_file = open("README.md", "w")
    readme_file.write(readme_head)
    readme_file.close()

    readme_file = open("README.md", "a")
    readme_file.write(date)
    readme_file.close()

    readme_file = open("README.md", "a")
    readme_file.write(readme_before_table)
    readme_file.close()


    driver = webdriver.Chrome()
    driver.get("https://github.com/gayanvoice/top-github-users/blob/main/markdown/total_contributions/tunisia.md")

    avatars_list = driver.find_elements(By.CSS_SELECTOR, "table td a img[width='24']")

    users = []
    users_list = []
    for avatar in avatars_list:
        users_list.append(avatar.get_attribute("alt")[10:])

    i = 1
    for user in users_list:
        if requests.get("https://github.com/" + user).status_code == 200:
            driver.get("https://github.com/" + user)
            if driver.find_element(By.CSS_SELECTOR, "span.p-name.vcard-fullname.d-block.overflow-hidden").text != "":
                name = driver.find_element(By.CSS_SELECTOR, "span.p-name.vcard-fullname.d-block.overflow-hidden").text
            else:
                name = "No name"
            avatar = driver.find_element(By.CSS_SELECTOR, "img.avatar.avatar-user.width-full.border.color-bg-default").get_attribute("src")
            try:
                company = driver.find_element(By.CSS_SELECTOR, "li.vcard-detail.pt-1.css-truncate.css-truncate-target.hide-sm.hide-md span.p-org div").text
            except:
                company = "No company"
            total_contribution = int(driver.find_element(By.CSS_SELECTOR, ".js-yearly-contributions .position-relative h2.f4.text-normal.mb-2").text[:-31].replace(",", ""))

            print(i, user, name, avatar, company, total_contribution)
            users.append((i, user, name, avatar, company, total_contribution))
            i = i + 1

    users.sort(key=lambda j: j[5], reverse=True)

    for user in users:
        write_user(user[0], user[1], user[2], user[3], user[4], user[5])

    readme_file = open("README.md", "a")
    readme_file.write(readme_after_table)
    readme_file.close()


def write_user(index, username, name, avatar_url, company, total_contribution):
    readme_file = open("README.md", "a", encoding="utf-8")
    readme_file.write('<tr>\n' +
                      '    <td align="center">' + str(index) + '</td>\n' +
                      '    <td>\n' +
                      '        <a href="https://github.com/' + username + '">\n' +
                      '            <img src="' + avatar_url + '" width = "24" alt = "Avatar of ' + username + '" >' + username + '\n' +
                      '        </a><br/>\n' +
                      '    ' + name + '\n' +
                      '    </td>\n'
                      '    <td>' + company + '</td>\n'
                      '    <td align="center">' + total_contribution + '</td>\n'
                      '</tr>\n')
    readme_file.close()


if __name__ == "__main__":
    main()


# driver.implicitly_wait(60)
# email = driver.find_element(By.CSS_SELECTOR, "input#login_field")
# password = driver.find_element(By.CSS_SELECTOR, "input#password")
#
# email.send_keys("muhamedyaseenyahyaoui@gmail.com")
# password.send_keys("mayway2805")
#
# driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary.btn-block.js-sign-in-button").click()
