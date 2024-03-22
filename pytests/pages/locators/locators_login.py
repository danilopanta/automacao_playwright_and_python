    # **
    # * Mapeamento de elementos
    # **

class LocatorsLogin:

        def accept_cookies(page):
            return page.locator("xpath=//button[@id='btnAcceptCookies']")

        def open_user_menu(page):
            return page.locator("xpath=//li[@id='userMenuItem']")
        
        def field_cpf_email(page):
            return page.locator("xpath=//input[@id='loginEmail']")
        
        def field_password(page):
            return page.locator("xpath=//input[@id='password']")
        
        def btn_access_orbia(page):
            return page.locator("xpath=//button[@id='login']")
        
        def user_logged(page):
            return page.locator("xpath=//input[@id='isUserLogged']")