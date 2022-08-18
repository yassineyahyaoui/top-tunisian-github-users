import os
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

    readme_file = open(os.path.join("readme", "README.md"), "w")
    readme_file.write(readme_head)
    readme_file.close()

    readme_file = open(os.path.join("readme", "README.md"), "a")
    readme_file.write(date)
    readme_file.close()

    readme_file = open(os.path.join("readme", "README.md"), "a")
    readme_file.write(readme_before_table)
    readme_file.close()

    os.system('cmd /c "cd readme"')
    os.system('cmd /c "git add ."')
    os.system('cmd /c "git commit -m \"update\""')
    os.system('cmd /c "git push"')


def write_user(index, username, name, avatar_url, company, total_contribution):
    readme_file = open(os.path.join("readme", "README.md"), "a", encoding="utf-8")
    readme_file.write('<tr>\n' +
                      '    <td align="center">' + str(index) + '</td>\n' +
                      '    <td>\n' +
                      '        <a href="https://github.com/' + username + '">\n' +
                      '            <img src="' + avatar_url + '" width = "24" alt = "Avatar of ' + username + '" >' + username + '\n' +
                      '        </a><br/>\n' +
                      '    ' + name + '\n' +
                      '    </td>\n'
                      '    <td>' + company + '</td>\n'
                      '    <td align="center">' + str(total_contribution) + '</td>\n'
                      '</tr>\n')
    readme_file.close()


if __name__ == "__main__":
    main()
