from src.open_bw import OpenBrowser as browser
from src.general.browser_operation import Browser_Opt as browser_opt
from time import sleep
import re


class User_Package_Detalis(browser):
    def __init__(self):
        element = "//*[span='用户套餐详情']"
        if browser.driver.find_element_by_xpath(element).is_displayed():
            browser.driver.find_element_by_xpath(element).click()
        else:
            headline = browser.driver.find_elements_by_class_name('layout-text')
            headline[1].click()
            if browser.driver.find_element_by_xpath(element).is_displayed():
                browser.driver.find_element_by_xpath(element).click()
        sleep(2)


    def query(self, userid='', phone='', product_id='', package_name='', owned='', casename='', **kwargs):
        # 默认id、phone、owned均为空，当调用时有传值时，才进行输入，owned为所属企业
        if userid != '':
            browser.driver.find_element_by_xpath(" //*[@placeholder='用户ID']").send_keys(userid)
        if phone != '':
            browser.driver.find_element_by_xpath(" //*[@placeholder='手机号码']").send_keys(phone)
        if product_id != '':
            browser.driver.find_element_by_xpath(" //*[@placeholder='产品ID']").send_keys(product_id)
        if package_name != '':
            browser.driver.find_element_by_xpath(" //*[@placeholder='套餐名称']").send_keys(package_name)
        if owned != '':
            browser.driver.find_element_by_xpath(" //*[@placeholder='请选择']").click()
            browser.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/form/div/div[5]/div/div/div/div[2]/ul[2]/li').click()
            owned = browser.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/form/div/div[5]/div/div/div/div[2]/ul[2]/li').text
        browser.driver.find_element_by_xpath("//*[span='查询']").click()
        browser.driver.implicitly_wait(10)

    def query_data(self, kwarg):
        sleep(2)
        pattern = re.compile(r'\d+')
        count = browser.driver.find_element_by_xpath("//span[@class='ivu-page-total']").text
        count = int(pattern.search(count).group(0))
        datas = {}
        if count > 0:
            for i in range(1, count + 1):
                dic = {}
                for j in range(1, 5):
                    key = browser.driver.find_element_by_xpath(
                        "//div[@class='ivu-table-header']/table/thead/tr/th[" + str(j) + "]/div/span").text
                    value = browser.driver.find_element_by_xpath(
                        "//tbody[@class='ivu-table-tbody']/tr[" + str(i) + "]/td[" + str(j) + "]/div/span").text
                    dic[key] = value
                datas[i] = dic
            kwarg_valus = []
            for i in datas:
                kwarg_valus.append(datas[i][kwarg])
            print(datas)
            return kwarg_valus
        else:
            msg = browser.driver.find_element_by_xpath('//div[@class="ivu-table-tip"]/table/tbody/tr/td/span').text
            return msg



