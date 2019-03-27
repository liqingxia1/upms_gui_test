import os
import datetime
from src.open_bw import OpenBrowser as browser

class Browser_Opt(browser):
    '''
    执行浏览器操作
    def max:最大化
    def set_size: 设置浏览器大小
    def back_up: 后退
    def for_ward: 前进
    def user_details: 截屏
    def get_time: 获取当前时间
    '''

    def max(self):
        browser.driver.maximize_window()

    def set_size(self, wide, high):
        browser.driver.set_window_size(wide, high)

    def back_up(self):
        browser.driver.back()

    def for_ward(self):
        browser.driver.forward()


    def screenshot(self, png_name,die):
        path = os.path.dirname(os.getcwd())
        png_path = os.path.join(path, 'screenshot\\'+die +'\\' + png_name + '.png')
        browser.driver.get_screenshot_as_file(png_path)

    # 获取当前时间
    def get_time(self):
        time = datetime.datetime.now().strftime('%m%d%H%M%S')  # 现在
        return time

