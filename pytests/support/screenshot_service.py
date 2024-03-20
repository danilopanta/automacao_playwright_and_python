import os
import allure
from pytests.support.hooks import *

class ScreenshotService:

    # Função para tirar screenshot da tela e realizar o attachment no allure report    
    def take_screenshot(page):
        PATH_SCREENSHOT = f"{os.environ['PATH_SCREENSHOT']}/screenshot/screenshot.png"
        page.screenshot(path=PATH_SCREENSHOT)
        allure.attach.file(PATH_SCREENSHOT, attachment_type=allure.attachment_type.PNG)