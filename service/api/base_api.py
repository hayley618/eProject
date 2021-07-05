import json
import requests
from service.api.logger import Logger


class BaseApi:
    def __init__(self):
        self.log = Logger().get_log()

    def request(self, request: dict):
        if 'url' in request:
            return self.http_request(request)

    def http_request(self, request):
        # request = {
        #     'url': '',
        #     'method': 'get',
        #     'json': {},
        #     'params': {}
        # }
        r = requests.request(**request)
        self.log.info(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self):
        pass

    def tcp_request(self):
        pass
