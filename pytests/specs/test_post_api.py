import json
from pytests.support.hooks import *
from pytests.mocks.api_mock import *
from pytests.clients.post_api_client import LivrariaClient
from pytests.support.api_utils import ApiUtils


@pytest.mark.crud_livros
def test_post_livros():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.post_livros(payload)
    resp_parse = LivrariaClient.validate_response(response, 201)