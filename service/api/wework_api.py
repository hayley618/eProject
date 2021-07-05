from service.api.base_api import BaseApi


class Wework(BaseApi):
    token: str = None

    def get_token(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'method': 'get',
            'params': {'corpid': 'wwb441a4fb9644fda6',
                       'corpsecret': 'jaKbJNz4n00L0pfdFLtHnowmohOaJ8OSOc2g8KAIFw0'
                       }
        }
        r = self.request(data)
        self.token = r.json()['access_token']
