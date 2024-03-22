# acessar o site Orbia Brasil
# Selecionar a opção de login
# Inserir e-mail
# Inserir senha
# Clicar no botão Login
# Verificar se foi realizado login corretamente

import allure
import pytest
from pytests.pages.login_page import Login
from playwright.sync_api import Page

@pytest.mark.login_orbia_br
def test_login_site_orbia(page: Page):
    with allure.step("Acessar Site Orbia"):
        Login.access_orbia_site_br(page)
    with allure.step("Aceitar os cookies"):
        Login.accept_cookies(page)
    with allure.step("Selecionar a opçao de login"):
        Login.access_login_page_br(page)
    with allure.step("Realizar login orbia"):
        Login.fill_login_orbia(page)
    with allure.step("Verificar se foi realizado o Login"):
        Login.validate_login_orbia(page)
