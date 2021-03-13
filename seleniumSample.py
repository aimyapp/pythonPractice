from selenium import webdriver
import os

# chrome用のwebdriver
DRIVER_PATH = os.path.join(os.path.dirname("C:/webdriver/chromedriver.exe"), "chromedriver")
# ハンゲームのサイト取得
browser = webdriver.Chrome(DRIVER_PATH)
browser.get("https://www.hange.jp/")
# ID, PWの入力
user_name = browser.find_element_by_id('strmemberid')
user_name.send_keys('xxxxx')
password = browser.find_element_by_id('strpassword')
password.send_keys('xxxxx')
# ログイン実行
login_btn = browser.find_element_by_id('loginBtn')
login_btn.click()