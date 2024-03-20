from pytests.pages.locators.locators_login import LocatorsLogin
locators = LocatorsLogin
from playwright.sync_api import Keyboard

class Login:


    def access_orbia_site_br(page):
        page.goto("https://orbia-uat.bravium.com.br/orbia")
        assert page.title() == "Orbia - Você e o agronegócio acontecem aqui."

    def accept_cookies(page):
        locators.accept_cookies(page).click()

    def access_login_page_br(page):
        locators.open_user_menu(page).click()
        assert page.title() == "Identificação - Orbia"
    
    def fill_login_orbia(page):
        locators.field_cpf_email(page).fill("05857743079")
        locators.field_password(page).fill("Mudar@123")
        # Pressiona a tecla "Enter" após preencher o campo de senha
        page.keyboard.press("Enter")

        locators.btn_access_orbia(page).click()

        # Aguarda 10 segundos antes de verificar o título da página
        page.wait_for_timeout(10000)

        assert page.title() == "Orbia - Você e o agronegócio acontecem aqui."