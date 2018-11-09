import unittest
import TestforUS1.Tests.TestTC1
import TestforUS1.Tests.TestTC2

basicSuite = unittest.TestSuite()
basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.TestTC1.TestTC1))
basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.TestTC2.TestTC2))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(basicSuite)