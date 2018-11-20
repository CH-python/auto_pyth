import unittest
import os
import HtmlTestRunner
import xmlrunner
import TestforUS1.Tests.testGetToPaymentWindow
import TestforUS1.Tests.testButtonsDownloadAndSend
import TestforUS1.Tests.testSelectBill
import TestforUS1.Tests.testCheckBalanceAfterPay
import TestforUS1.Tests.testCheckNoSaveCardDataAfterRefresh
import TestforUS1.Tests.testCheckNoSaveCvcAfterRefresh
import TestforUS1.Tests.testAllKate
import TestforUS1.Tests.testAllSviat

class TestStringMethods(unittest.TestCase):
    basicSuite = unittest.TestSuite()
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testAllKate.Test))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testAllSviat.Test))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testSelectBill.TestTC1))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testButtonsDownloadAndSend.TestTC3))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testGetToPaymentWindow.TestTC4))
    basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testCheckBalanceAfterPay.TestTC15))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testCheckNoSaveCardDataAfterRefresh.TestTC11))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testCheckNoSaveCvcAfterRefresh.TestTC10))

    html_report_dir = './html_report'
    runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    runner.run(basicSuite)