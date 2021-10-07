import HTMLTestRunner
import os
import sys
import time
import unittest

def createsuite():
    discovers = unittest.defaultTestLoader.discover("./", pattern="testbaidu*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__=="__main__":
    #1，创建一个文件夹
    curpath = sys.path[0]
    print(sys.path)
    print(sys.path[0])
    # 当当前路径下resultreport文件夹不存在的时候，就创建一个
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')

    # 2，解决重复命名的问题
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    print(time.time())
    print(time.localtime(time.time()))
    # 文件名是路径加上文件的名称
    filename = curpath + '/resultreport/'+ now + 'resultreport.html'
    # 打开 HTML 文件, wb 以写的方式
    with open(filename, 'wb') as fp:
        # 括号里的参数是 HTML 报告里面的参数
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告",
                                               description=u"用例执行情况", verbosity=2)
        suite = createsuite()
        runner.run(suite)
