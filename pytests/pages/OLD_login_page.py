from pytests.support.screenshot_service import ScreenshotService

class LoginPage:

    # **
    # * Mapeamento de elementos
    # **

    def field_email(page):
        return page.locator("xpath=//input[@id='email']")

    def field_password(page):
        return page.locator("xpath=//input[@id='senha']")

    def button_entrar(page):
        return page.locator("xpath=//button[contains(text(),'Entrar')]")

    def element_login_sucess(page):
        return page.locator("xpath=//div[contains(text(),'Bem vindo, testudemy!')]")

    # **
    # * Métodos e Funções
    # **

    def page_sr_barriga(page):
        page.goto("https://seubarriga.wcaquino.me/login")
        ScreenshotService.take_screenshot(page)
        assert page.title() == "Seu Barriga - Log in"

    def fill_login(page):
        LoginPage.field_email(page).fill("test@test")
        LoginPage.field_password(page).fill("123")
        ScreenshotService.take_screenshot(page)

    def perform_login(page):
        LoginPage.button_entrar(page).click()
        elemente = LoginPage.element_login_sucess(page)
        assert elemente.text_content() == "Bem vindo, test!"
        ScreenshotService.take_screenshot(page)