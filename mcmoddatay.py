# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LINK = input('请输入爬取地址（一般为 https://www.mcmod.cn/modpack/edit/ ）: ')
MAIL = input('请输入 MCMOD 网站账户邮箱: ')
PASS = input('请输入 MCMOD 网站密码: ')
S = int(input('请输入起始页码（如 2 ）: '))
L = int(input('请输入结束页码（如 10000 ）: '))
J = int(input('请输入爬取间隔（秒，推荐输入 2 ，不建议输入 1 ，否则出现将无法正常保存）: '))

options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.mcmod.cn/login')
driver.find_element(By.ID, 'login-username').send_keys(MAIL)
driver.find_element(By.ID, 'login-password').send_keys(PASS)
driver.find_element(By.ID, 'login-action-btn').click()

for i in range(S, L+1):
    print(f'当前正在获取第 {i} 号数据')
    url = LINK + str(i)
    driver.get(url)
    for j in range(5):
        try:
            html = driver.page_source
            with open(f'mcmodwebdatay/{i}.html', 'w', encoding='utf-8') as f:
                f.write(html)
            break
        except:
            if j == 4:
                print(f'错误地址：{url}')
    time.sleep(J)

print('完成！！！')