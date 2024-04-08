from pytests.pages.locators.locators_login import LocatorsLogin
from playwright.sync_api import expect
from pytests.support.db.sql_server_utils import SqlServerUtils

locators = LocatorsLogin

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
        #Criando uma instância para receber o retorno do 'document' que a função entrega
        pardocument = Login.connection_return_query()

        #Utilizando a coluna ParDocumentID, para selecionar um participante e preencher o campo login
        locators.field_cpf_email(page).fill(pardocument[0]['parDocumentID'])

        locators.field_password(page).fill("Unica@123")
        page.keyboard.press("Enter") # Pressiona a tecla "Enter" após preencher o campo de senha
        locators.btn_access_orbia(page).click()

    def validate_login_orbia(page):
        expect(locators.user_logged(page)).to_have_value('TRUE', timeout=10000)

    #Função para conectar ao banco tbParticipant e retornar os dados do participante.
    def connection_return_query():
        
        params = {
        "host": "sqluat01.satelital.com.br",
        "port": "1433",
        "database": "dbPRW",
        "user": "iusr_orbia_prw",
        "password": "orbia@2020"
    }
        connection = SqlServerUtils.connection_sql_server(params)
        
        query = "select top 1 * from tbparticipant where idcampaign = 'BRBAY' and parPassword = '00610485987E98E82C2D831F6C2FF155' and parStatus = 'A'"
        
        document = SqlServerUtils.query_sql_server(connection,query)

        return document