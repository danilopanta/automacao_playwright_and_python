from pytests.support.hooks import *
from pytests.pages.login_page import LoginPage
from playwright.sync_api import Page
import allure


# Descrição dos testes com pytest
@pytest.mark.test_login
def test_login(page: Page):
    with allure.step("acessar o site sr barriga"):
        LoginPage.page_sr_barriga(page)
    with allure.step("preencher o campos de login"):
        LoginPage.fill_login(page)
    with allure.step("realizar o login"):
        LoginPage.perform_login(page)