class Locator(object):

    #welcome page locators
    signIn = "Sign_in2"
    signUp = "Sign_up"

    #sign in page locators as user
    userEmail = "email"
    userPassword = "password"
    loginButton = "Login_button"

    #main user page locators
    payments = "#sidebar-menu>div>ul>li:nth-child(3)>a"

    #popup payments
    pay = "pay"
    details = "#historyTable > tbody > tr:nth-child(1) > td:nth-child(3) > button"
    titlePopupPayments = "#myModalLabel > span"
    balance = "#historyTable > tbody > tr:nth-child(1) > td.balance"

    #popup_payments: Select payment Sum
    paymentSum = "payment-sum-input"
    downloadCheck = "download-check-label"
    sendCheck = "send-check-label"
    proceed = "payment-proceed"

    #popup payments: EasyPay
    titlePopupEasyPay = "#container > section > span:nth-child(3) > div > div > main > div > header > h1"
    mailInput = "div.StaggerGroup-child.is-head-0.is-tail-NaN > div > div > div > fieldset > span > div > div.Textbox-inputRow > input"
    cardNumberInput = "div.StaggerGroup-child.is-head-1.is-tail-NaN > span > span:nth-child(1) > div > div.Textbox-inputRow > input"
    dateCardInput = "div.Fieldset-childLeft.u-size1of2 > div.Textbox-inputRow > input"
    cvNumberInput = "div.Fieldset-childRight.u-size1of2 > div.Textbox-inputRow > input"
    zipCodeInput =  "div.StaggerGroup-child > div > div > div > div > div.Textbox-inputRow > input"
    btnRememberMe = "span.Fieldset-child--subdued.Fieldset-child--checkboxActive"
    phoneInput = "fieldset > fieldset > span > div > div.Textbox-inputRow > input"
    btnPopupPay = "Button-animationWrapper-child--primary"
    btnBack = "Header-navBack"