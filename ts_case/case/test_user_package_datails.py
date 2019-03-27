from src.login import LOGIN
from src.open_bw import OpenBrowser as browser
from src.general.browser_operation import Browser_Opt as browser_opt
from src.user_manage.user_package_details import User_Package_Detalis
import unittest
from time import sleep
import warnings

class Test_User_Package_Datails(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        browser().open_firefox()
        LOGIN().default_user_login()
        self.user_d = User_Package_Detalis()

    def test_id_query(self):
        self.user_d.query(userid="YX046020190218142513964256716", casename="用户套餐详情-id查询")
        msg = self.user_d.query_data("用户ID")
        for i in msg:
            self.assertEqual(i, "YX046020190218142513964256716")

    def test_phone_query(self):
        self.user_d.query(phone="13570818004", casename="用户套餐详情-手机号码查询")
        msg = self.user_d.query_data("手机号码")
        for i in msg:
            self.assertEqual(i, "13570818004")

    def test_query(self):
        self.user_d.query(casename="直接点击查询")
        msg = self.user_d.query_data("手机号码")
        self.assertIsNotNone (msg)

    def test_id_phone_query(self):
        self.user_d.query(userid="YX046020190218142513964256716", phone="13570818004", casename="使用id与手机")
        msg = self.user_d.query_data("用户ID")
        for i in msg:
            self.assertEqual(i, "YX046020190218142513964256716")
        msg = self.user_d.query_data("手机号码")
        for i in msg:
            self.assertEqual(i, "13570818004")

    def test_errorphone_query(self):
        self.user_d.query(phone="13532ssa", casename="使用错误手机号")
        msg = self.user_d.query_data("手机号码")
        self.assertEqual(msg, "暂无数据")

    def tearDown(self):
        pass


