import unittest


def createsuite():
    # 将测试用例加入到测试(容器)套件中进行
    # discover

    discover = unittest.defaultTestLoader.discover("./",pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover


if __name__ == '__main__':
    # 创建了一个测试套件
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



