from src import config
from src.open_bw import OpenBrowser as browser
from src.general.browser_operation import Browser_Opt as browser_opt
from time import sleep

'''
定义登录界面的操作
class名为LOGIN，继承了browser，获取到了打开的浏览器（应导入时采用了别名from src.open_bw import OpenBrowser as browser）
__init__中配置了默认的url、用户名、密码

-user_login(self, username=0, password=0, isassert=1, msg="登录"):
——用户登录方法的封装，传入的参数有username、password、isassert、msg
————username：用户名
————password：密码
————isassert：是否断言
————msg：用例的名称（截图时会用到）

login_assert(self, username, errmsg):
——用户登录后，判断是否登录成功的方法，传入的参数有username,errmsg
————username：用户名
————errmsg：错误信息（截图时会用到）

'''


class LOGIN(browser):
    def __init__(self):
        # 默认取配置文件中的qa环境下的url、用户名、密码等信息
        self.username = config.get_config('upms_qa', 'username')
        self.password = config.get_config('upms_qa', 'password')
        self.url = config.get_config('upms_qa', 'url')

    def user_login(self, username, password, msg="正常登录"):
        # 打开浏览器
        browser.driver.get(self.url)
        browser.driver.implicitly_wait(10)

        browser.driver.find_element_by_id("userNo").clear()
        browser.driver.find_element_by_id("userNo").send_keys(username)
        browser.driver.find_element_by_id("pwd").clear()
        browser.driver.find_element_by_id("pwd").send_keys(password)
        browser.driver.find_element_by_id("subSave").click()
        browser.driver.implicitly_wait(10)
        return self.login_assert(username=username, errmsg=msg)

    def default_user_login(self):
        if browser.driver.find_elements_by_class_name("main-user-name"):
            browser.driver.refresh()
            sleep(3)
        else:
            return self.user_login(self.username, self.password)

    def login_assert(self, username, errmsg):
        # 根据元素判断是否登录成功
        if browser.driver.find_elements_by_class_name("main-user-name"):

            # 获取登录成功后的用户名显示保存为actual，并判断actual与username一致，若一致则登录成功，不一致则调用screenshot进行截图，并提示登录账户与显示账号不一致
            actual = browser.driver.find_element_by_class_name("main-user-name").text
            if username != actual:
                browser_opt().screenshot(png_name=username + "登录成功账号名显示错误", die="login")
                print("登录成功账号名显示错误,登录账号为:" + username + "显示账号为：", actual)
            else:
                browser_opt().screenshot(username + "登录成功", die="login")
                print("登录成功")
        # 登录失败时，将弹出的提示保存至actual，调用screenshot进行截图，并提示登录错误
        else:
            if browser.driver.find_element_by_id("showMsg"):
                actual = browser.driver.find_element_by_id("showMsg").text
            browser_opt().screenshot(errmsg, die="login")
            print("系统提示：" + actual + "\n截图信息：" + errmsg)

        # 返回actual（可能为用户名或系统提示消息）
        return actual





