from selenium import webdriver
from  time import sleep


class OpenBrowser():
    driver = None

    def open_chrome(self):
        # 打开谷歌浏览器
        if OpenBrowser.driver is None:
            OpenBrowser.driver = webdriver.Chrome()
            OpenBrowser.driver.maximize_window()

    def open_firefox(self):
        # 打开火狐浏览器
        if OpenBrowser.driver is None:
            OpenBrowser.driver = webdriver.Firefox()
            OpenBrowser.driver.maximize_window()

    def close_browser(self):
        # 关闭浏览器
        OpenBrowser.driver.quit()

