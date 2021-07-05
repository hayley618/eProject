from service.api.wework_api import Wework


class Tag(Wework):
    def search_tag(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?',
            'params': {'access_token': self.token},
            'method': 'post',
            'json': {}
        }
        return self.request(data)


    def add_tag(self, group_name, tag_name):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?',
            'params': {'access_token': self.token},
            'method': 'post',
            'json': {"group_name": group_name,
                     "order": 1,
                     "tag":
                         [
                             {
                                 "name": tag_name,
                                 "order": 1
                             }
                         ]
                     }
        }
        return self.request(data)


    def del_tag(self, group_id):
        data = {
            'url': 'ttps://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {'access_token': self.token},
            'method': 'post',
            'json': {'group_id': group_id}
        }
        return self.request(data)


    def edit_tag(self, tag_id, tag_name):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'params': {'access_token': self.token},
            'method': 'post',
            'json': {
                'id': tag_id,
                'name': tag_name
            }
        }
        return self.request(data)
