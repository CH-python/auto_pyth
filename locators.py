class Locator(object):

    #welcome page locators
    sign_in="Sign_in"
    sign_up="Sign_up"

    #sign in page locators as user
    user_email="email"
    user_password="password"
    login_button="Login_button"

    #main user page locators
    payments="//*[@id='sidebar-menu']/div/ul/li[3]/a"
    details="//*[@id='historyTable']/tbody/tr[2]/td[3]/button"
    titlePopup='//*[@id="myModalLabel"]/span'

    #payments page locators
    first_utility_details="#historyTable > tbody > tr:nth-child(1) > td:nth-child(3) > button"
    second_utility_details="#historyTable > tbody > tr:nth-child(2) > td:nth-child(3) > button"