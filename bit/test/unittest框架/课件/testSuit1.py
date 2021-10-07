import unittest
import testbaidu1
import testbaidu2


def createsuite():
    # addTest
    # suite=unittest.TestSuite()
    # suite.addTest(testbaidu1.Baidu1("test_hao"))
    # suite.addTest(testbaidu1.Baidu1("test_baidusearch"))
    #
    # suite.addTest(testbaidu2.Baidu2("test_hao"))
    # suite.addTest(testbaidu2.Baidu2("test_baidusearch"))
    # return suite

    # makesuit
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(testbaidu1.Baidu1))
    # suite.addTest(unittest.makeSuite(testbaidu2.Baidu2))
    # return suite

    # TestLoader
    suite1=unittest.TestLoader().loadTestsFromTestCase(testbaidu1.Baidu1)
    suite2=unittest.TestLoader().loadTestsFromTestCase(testbaidu2.Baidu2)
    suite = unittest.TestSuite([suite1, suite2])
    return suite

    # discover
    # discover = unittest.defaultTestLoader.discover("./", pattern="testbaidu*.py", top_level_dir=None)
    # print(discover)
    # return discover


if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
