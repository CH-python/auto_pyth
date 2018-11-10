class Locator(object):

    #welcome page locators
    signIn = "Sign_in"
    signUp = "Sign_up"

    #sign in page locators as user
    userEmail = "email"
    userPassword = "password"
    loginButton = "Login_button"

    #main user page locators
    payments = "//*[@id='sidebar-menu']/div/ul/li[3]/a"

    #popup payments
    pay = "pay"
    details = "//*[@id='historyTable']/tbody/tr[2]/td[3]/button"
    titlePopup = "//*[@id='myModalLabel']/span"

    #popup_payments: Select payment Sum
    paymentSum = "payment-sum-input"
    downloadCheck = "download-check-label"
    sendCheck = "send-check-label"
    proceed = "payment-proceed"


    #popup payments: EasyPay
    wayToFields = "/html/body/div/section/span/div/div/main/form/div/div/div/div/div/div/div"
    mailInput = wayToFields + "/div/div/div/fieldset/span/div/div/input"
    cardNumberInput = wayToFields + "/fieldset/div/div/span/span/div/div/input"
    dateCardInput = wayToFields + "/fieldset/div/div/div/div/input"
    cvNumberInput = wayToFields + "/fieldset/div/div/div[2]/div/input"
    zipCodeInput = wayToFields + "/fieldset/div/div/div/div/div/div/input"
    btnRememberMe = wayToFields + "/div/fieldset/span"
    phoneInput = wayToFields + "/div/div/div/fieldset/fieldset/span/div/div/input"
    btnPay = "Button-animationWrapper-child--primary"
    btnClose = "Header-navBack"


