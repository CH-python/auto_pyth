import unittest
import TestforUS1.Tests.testTC1
import TestforUS1.Tests.testTC3
import TestforUS1.Tests.testTC4
import TestforUS1.Tests.testTC15
import TestforUS1.Tests.testTC10

basicSuite = unittest.TestSuite()

basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC1.TestTC1))
# basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC15.TestTC15))
# basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC3.TestTC3))
# basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC4.TestTC4))
# basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testTC10.TestTC10))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(basicSuite)