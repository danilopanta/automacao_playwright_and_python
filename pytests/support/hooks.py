import pytest
import os
from dotenv import load_dotenv
from pytests.support.log_service import LogService
from pytests.support.utils import Utils
LOG = LogService
Utils.path_screenshot()

# Função do pytest para executar uma única vez antes de todos os testes
@pytest.fixture(scope="session", autouse=True)
def before_all():
    load_dotenv()

# Função do pytest para executar antes e depois de cada teste
# antes de "yield" = before, depois de "yield" = after
@pytest.fixture(autouse=True)
def before_after():
    LOG.log_info("-----Before-----")
    yield
    LOG.log_info("-----After-----")