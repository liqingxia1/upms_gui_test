from src.login import LOGIN
from src.open_bw import OpenBrowser as browser
from src.general.browser_operation import Browser_Opt as browser_opt
from src.user_manage.user_details import User_Detalis
import unittest
from time import sleep
import warnings

'''
定义用户详情界面测试集合的class名称为：UserDetailsTestCase，并继承unittest（必须要继承）
setUp：测试执行前的初始化操作,打开浏览器，且最大化、用户登录


以test开头的均为用例
—— user_d = User_Detalis()
—— 定义user_d等于User_Detalis类

—— msg = user_d.query(id="YX046020180629193930435261689", casename="用户详情-id查询")
—— 调用User_Detalis类下的query方法，传入参数id、casename
—— 得到返回的msg

—— self.assertEqual(得到的提示, 预期返回的提示)
—— 调用assertEqual方法，判断得到的弹框提示是否与预期的一致

TearDown：test执行后的操作,关闭浏览器
'''


class UserDetailsTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        browser().open_firefox()
        LOGIN().default_user_login()
        self.user_d = User_Detalis()

    def test_id_query(self):
        msg = self.user_d.query(id="YX046020190218142513964256716", casename="用户详情-id查询")
        self.assertEqual(msg, 0)

    def test_phone_query(self):
        msg = self.user_d.query(phone="13570818004", casename="用户详情-手机号码查询")
        self.assertEqual(msg, 0)

    def test_query(self):
        msg = self.user_d.query(casename="直接点击查询")
        self.assertEqual(msg, 0)

    def test_id_phone_query(self):
        msg = self.user_d.query(id="YX046020190218142513964256716", phone="13570818004", casename="使用id与手机")
        self.assertEqual(msg, 0)

    def test_errorphone_query(self):
        msg = self.user_d.query(phone="135a", casename="使用错误手机号")
        self.assertEqual(msg, "暂无数据")

    def tearDown(self):
        pass


