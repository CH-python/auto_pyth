import unittest
import TestforUS1.Tests.TestTC1

basicSuite = unittest.TestSuite()
basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.TestTC1.TestTC1))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(basicSuite)
