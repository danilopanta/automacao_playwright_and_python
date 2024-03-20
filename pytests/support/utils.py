import os


class Utils:

    # Função para ajustar a path da screenshot quando rodar com o player do pycharm
    def path_screenshot():
        if "/specs" in os.getcwd():
            os.environ['PATH_SCREENSHOT'] = os.getcwd().replace("/specs", "")
        else:
            os.environ['PATH_SCREENSHOT'] = f"{os.getcwd()}/pytests"
