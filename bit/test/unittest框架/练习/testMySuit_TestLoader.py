import unittest
import testMybaidu1
import testMybaidu2


def createsuite():
    # 将测试用例加入到测试(容器)套件中进行

    # TestLoader
    suite1 = unittest.TestLoader().loadTestsFromTestCase(testMybaidu1.MyBaidu)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(testMybaidu2.MyBaidu)
    suite3 = unittest.TestSuite([suite1, suite2])
    return suite3


if __name__ == '__main__':
    # 创建了一个测试套件
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



