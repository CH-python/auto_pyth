import unittest
import os
import HtmlTestRunner
import xmlrunner
import TestforUS1.Tests.testGetToPaymentWindow
import TestforUS1.Tests.testButtonsDownloadAndSend
import TestforUS1.Tests.testSelectBill
import TestforUS1.Tests.testAll
# import TestforUS1.Tests.testCheckBalanceAfterPay
# import TestforUS1.Tests.testTC10



def main():

    basicSuite = unittest.TestSuite()
    basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testAll.Test))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testSelectBill.TestTC1))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testButtonsDownloadAndSend.TestTC3))
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testGetToPaymentWindow.TestTC4))
    # print(basicSuite)
    # basicSuite.addTest(unittest.makeSuite(TestforUS1.Tests.testCheckBalanceAfterPay.TestTC15))

    html_report_dir = './html_report/'
    # xml_report_dir = './reports/xml_report'
    runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir, verbosity=2)\
    # runner = xmlrunner.XMLTestRunner(output=xml_report_dir)
    runner.run(basicSuite)


if __name__ == "__main__":
    main()