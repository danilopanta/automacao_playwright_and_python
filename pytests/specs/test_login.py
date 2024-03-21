# acessar o site Orbia Brasil
# Selecionar a opção de login
# Inserir e-mail
# Inserir senha
# Clicar no botão Login
# Verificar se foi realizado login corretamente

import pytest
from pytests.pages.login_page import Login
from playwright.sync_api import Page

@pytest.mark.acess_cookies
def test_aceitar_cookies(page:Page):
    Login.access_orbia_site_br(page)
    Login.accept_cookies(page)

@pytest.mark.login_orbia
def login_site_orbia(page: Page):
    Login.access_login_page_br(page)
    Login.fill_login_orbia(page)