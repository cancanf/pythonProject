import unittest
import testMybaidu1
import testMybaidu2


def createsuite():
    # 使用makesuit方法
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testMybaidu1.MyBaidu))
    suite.addTest(unittest.makeSuite(testMybaidu2.MyBaidu))
    return suite


if __name__ == '__main__':
    # 创建了一个测试套件
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


