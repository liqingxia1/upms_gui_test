from src.login import LOGIN
from src.open_bw import OpenBrowser as browser
from src.general.browser_operation import Browser_Opt as browser_opt
import unittest
from time import sleep
import warnings
'''
定义登录测试集合的class名称为：LoginTestCase，并继承unittest（必须要继承）
setUp：测试执行前的初始化操作,打开浏览器，且最大化


以test开头的均为用例
—— msg = LOGIN().user_login("111", "ctf", 0, "错误的用户名")
—— msg = LOGIN().user_login(参数1, 参数2, 参数3, 参数4)
—— 调用LOGIN()类中的user_login方法，参数4个参数，并保存返回的msg

—— self.assertEqual(msg, "该用户未被授权登录此系统，请联系管理员")
—— self.assertEqual(得到的提示, 预期返回的提示)
—— 调用assertEqual方法，判断得到的弹框提示是否与预期的一致


TearDown：test执行后的操作,关闭浏览器
'''

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        browser().open_firefox()


    def test_error_username(self):
        msg = LOGIN().user_login("111", "ctf", "错误的用户名")
        self.assertEqual(msg, "该用户未被授权登录此系统，请联系管理员")

    def test_error_username2(self):
        msg = LOGIN().user_login("CTF", "ctf", "大小写错误的用户名")
        self.assertEqual(msg, "用户名或密码错误，请重新输入")

    def test_error_pwd(self):
        msg = LOGIN().user_login("ctf", "000", "错误的密码")
        self.assertEqual(msg, "用户名或密码错误，请重新输入")

    def test_error_pwd2(self):
        msg = LOGIN().user_login("ctf", "CTF","大小写错误的密码")
        print(msg)
        print(type(msg))
        self.assertEqual(msg, "用户名或密码错误，请重新输入")

    def test_error_nullusername(self):
        msg = LOGIN().user_login("", "123456", "为空的用户名")
        self.assertEqual(msg, "请输入账号密码")

    def test_error_nullpwd(self):
        msg = LOGIN().user_login("ctf", "", "为空的密码")
        self.assertEqual(msg, "请输入账号密码")

    def test_pass(self):
        msg = LOGIN().default_user_login()
        self.assertEqual(msg, "ctf")


    def tearDown(self):
        pass

