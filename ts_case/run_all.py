import unittest
from BeautifulReport import BeautifulReport
import os


# 获取路径到当前项目路径下的case目录
curpath = os.path.dirname(os.path.realpath(__file__))       # 获取当前项目路径到ts_case
casepath = os.path.join(curpath, "case")                    # 定义ts_case\case目录为casepath
reportpath = os.path.join(curpath, "report")                # 定义ts_case\report目录为reportpath

# 测试用例需放在case目录，判断是否存在case目录，若不存在则自动创建
if not os.path.exists(casepath):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(casepath)

# 测试报告生成放在report目录下，判断是否存在该目录，若不存在则自动创建
if not os.path.exists(reportpath): os.mkdir(reportpath)


# 遍历ts_case\case目录下的所有test开头的用例，并组合到一起return出去
def add_case(case_path=casepath, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover


# 调用BeautifulReport生成测试报告
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html',
                  description='测试登录报告',
                  log_path='report')


# 执行入口
if __name__ == "__main__":
    # 调用add_case()组成用例集合
    cases = add_case()
    # 调用unittest框架
    suite = unittest.TestSuite()
    # 遍历增加case到suite中
    for i in cases:
        suite.addTest(i)

    # 输出并调用run方法，将测试集传进去
    print(suite)
    run(suite)
