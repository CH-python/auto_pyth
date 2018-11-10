import unittest
import TestforUS1.Tests.testTC1
import TestforUS1.Tests.testTC15
import TestforUS1.Tests.testTC3

basicSuite = unittest.TestSuite()
# basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC1.TestTC1))
# basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC15.TestTC15))
basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC3.TestTC3))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(basicSuite)