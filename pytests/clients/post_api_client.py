from playwright.sync_api import sync_playwright
from pytests.support.hooks import *
from pytests.support.api_utils import ApiUtils

class LivrariaClient:

    def post_livros(payload):
        with sync_playwright() as p:
            uri_api = "http://132.145.174.237:3000/livros"

            context = p.request.new_context()
            response = context.post(uri_api, data=payload)
            LOG.log_info("POST")
            LOG.log_info(f"URL: {uri_api}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    def validate_response(response, code):
        resp = ApiUtils.request_parse_log(response)
        ApiUtils.validate_status_code(response, code)
        return resp
    