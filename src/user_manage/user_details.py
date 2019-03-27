from src.open_bw import OpenBrowser as browser
from src.general.browser_operation import Browser_Opt as browser_opt
from time import sleep

'''
定义用户详情界面的操作
class名为User_Detalis，继承了browser 
__init__中先进入用户管理、再点击用户详情

-query(self, id='', phone='', owned='', casename=''):
——用户详情界面查询的方法的封装，传入的参数有id、phone、owned、casename
————username：用户名
————password：密码
————owned：所属企业
————casename：用例名称（截图时会用到）
以上参数默认为空，为空时，则不会输入该条件，不为空时则会输入该条件的查询值 
'''


class User_Detalis(browser):
    def __init__(self):
        element = "//*[span='用户详情']"
        if browser.driver.find_element_by_xpath(element).is_displayed():
            browser.driver.find_element_by_xpath(element).click()
        else:
            headline = browser.driver.find_elements_by_class_name('layout-text')
            headline[1].click()
            if browser.driver.find_element_by_xpath(element).is_displayed():
                browser.driver.find_element_by_xpath(element).click()
        sleep(2)

        self.phone = ''
        self.id = ''

    def query(self, id='', phone='', owned='', casename=''):
        # 默认id、phone、owned均为空，当调用时有传值时，才进行输入，owned为所属企业
        if id != '':
            browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[1]/div/form/div/div[1]/div/div/div/input').send_keys(id)
        if phone != '':
            browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[1]/div/form/div/div[2]/div/div/div/input').send_keys(phone)
        if owned != '':
            browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[1]/div/form/div/div[3]/div/div/div/div[1]/input[2]').click()
            browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[1]/div/form/div/div[3]/div/div/div/div[2]/ul[2]/li').click()
            owned = browser.driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[3]/div/div/div/div[1]/div/form/div/div[3]/div/div/div/div[2]/ul[2]/li').text
        sleep(2)

        # 点击查询
        browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[1]/div/form/div/div[4]/div/button').click()

        sleep(2)
        # 获取是否提示暂无数据
        msg = browser.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[3]/div/div/div/div[2]/div/div[3]/table/tbody/tr/td/span').text

        # 判断页面提示是否为暂无数据
        if msg != '暂无数据':
            # 获取当前搜索展示的总条数
            number = browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/ul/span').text
            number = number.replace("共 ",'').replace(" 条",'')

            # 默认返回result为0
            result = 0
            # 判断搜索到的数据总量，默认仅展示10条数据，若总数超过10条，也只对比当前页面数据是否与查询条件一致
            if int(number)>10:
                count= 11
            else:
                count = int(number)+1

            # 根据数据进行遍历，获取数量栏的信息，进行对比，rsp_id为id; rsp_owned为所属企业; rsp_phone为手机号码
            for i in range(1, count):
                rsp_id = browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr['+str(i)+']/td[1]/div').text
                rsp_owned = browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/div/span').text
                rsp_phone = browser.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[8]/div/span').text
                # 只有查询有输入时才进行检查，且当查询的条件not in 获取的数据中时，result赋值为1
                if id != '':
                    self.id = id
                    if id not in rsp_id:
                        result = 1
                if phone != '':
                    self.phone = phone
                    if phone not in rsp_phone:
                        result = 1
                if owned != '':
                    if owned not in rsp_owned:
                        result = 1
                print(rsp_id,rsp_phone,rsp_owned)

            # 调用screenshot方法执行截图操作
            browser_opt().screenshot(casename, die="userDetails")
            return result
        else :
            browser_opt().screenshot(casename, die="userDetails")
            print(msg)
            return msg

    def view_details(self):
        browser.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr/td[1]/div/div/button[1]').click()
        sleep(3)
        id = browser.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/form/div/div[1]/div/div/div/input').text
        phone = browser.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/form/div/div[2]/div/div/div/input').text
        number = browser.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/ul/span').text
        number = number.replace("共 ", '').replace(" 条", '')
        print("111111",id, phone, number)

        # 判断搜索到的数据总量，默认仅展示10条数据，若总数超过10条，也只对比当前页面数据是否与查询条件一致
        if int(number) > 10:
            count = 11
        else:
            count = int(number) + 1

        # 根据数据进行遍历，获取数量栏的信息，进行对比，rsp_id为id; rsp_owned为所属企业; rsp_phone为手机号码
        for i in range(1, count):
            rsp_id = browser.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[1]').text
            rsp_phone = browser.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/div').text
            # 只有查询有输入时才进行检查，且当查询的条件not in 获取的数据中时，result赋值为1
            if self.id != rsp_id or self.phone != rsp_phone:
                browser_opt().screenshot("用户套餐详情错误", die="userDetails")
                print(rsp_id, rsp_phone)

    def freeze(self, pop="确定"):
        browser.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr/td[1]/div/div/button[2]').click()
        state = browser.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr/td[1]/div/div/button[2]').text
        print("当前状态为：",state)
        pop_up = browser.driver.find_element_by_xpath('/html/body/div[23]/div[2]/div/div/div[2]/div/p').text
        print("点击%s,弹出提示框：%s"%(state, pop_up))
        if pop == "确定":
            browser.driver.find_element_by_xpath('/html/body/div[23]/div[2]/div/div/div[3]/div/button[1]').click()
        elif pop == "取消":
            browser.driver.find_element_by_xpath('/html/body/div[23]/div[2]/div/div/div[3]/div/button[2]').click()
        sleep(5)
        state = browser.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr/td[1]/div/div/button[2]').text
        print("点击%s后，最新状态为：%s"%(pop, state))




