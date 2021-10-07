import unittest
import testMybaidu1
import testMybaidu2


def createsuite():
    # 将测试用例加入到测试(容器)套件中进行
    # addTest手动加入测试用例到测试套件的方法
    # suite = unittest.TestSuite()
    # suite.addTest(testMybaidu1.MyBaidu("test_new"))
    # suite.addTest(testMybaidu1.MyBaidu("test_baidusearch"))
    #
    # suite.addTest(testMybaidu2.MyBaidu("test_new"))
    # suite.addTest(testMybaidu2.MyBaidu("test_baidusearch"))
    # return suite

    # 使用makesuit方法
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(testMybaidu1.MyBaidu))
    # suite.addTest(unittest.makeSuite(testMybaidu2.MyBaidu))
    # return suite

    # TestLoader
    suite1 = unittest.TestLoader().loadTestsFromTestCase(testMybaidu1.MyBaidu)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(testMybaidu2.MyBaidu)
    suite3 = unittest.TestSuite([suite1, suite2])
    return suite3

    # discover
    # discover = unittest.defaultTestLoader.discover("./",pattern="test*.py",top_level_dir=None)
    # print(discover)
    # return discover


if __name__ == '__main__':
    # 创建了一个测试套件
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
