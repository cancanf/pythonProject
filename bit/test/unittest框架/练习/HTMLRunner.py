import HTMLTestRunner
import os
import sys
import time
import unittest


def createstuite():
    discovers = unittest.defaultTestLoader.discover("./", pattern="test*.py", top_level_dir=None)
    print(discovers)
    return discovers


if __name__ == '__main__':
    curpath = sys.path[0]
    print(sys.path)
    print(sys.path[0])
    # 路径不存在就创建一个
    if not os.path.exists(curpath + '/resultreport'):
        os.makedirs(curpath + '/resultreport')

    # 2.测试要执行很多次，命名很可能会重复
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    print(time.time())
    print(time.localtime(time.time()))
    # 构造文件名
    filename = curpath + '/resultreport/' + now + 'resultreport.html'
    # 打开 HTML 文件 ,wb的方式写入
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告",
                                               description="用例测试情况", verbosity=2)
        suite = createstuite()
        runner.run(suite)
