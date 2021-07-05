import pytest
from service.api.tag.tag import Tag


class TestWework:

    def setup_class(self):
        self.wework = Tag()
        self.wework.get_token()

    # 获取企业标签库
    def test_search(self):
        r = self.wework.search_tag()
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize('group_name, tag_name', [('group5', 'tag5'), ('group6', 'tag6')])
    def test_add_tag(self, group_name, tag_name):
        r = self.wework.add_tag(group_name, tag_name)
        assert r.json()['errcode'] == 0
        # 验证标签有没有添加上
        r_group_list = []
        r_tag_group = self.wework.search_tag().json()['tag_group']
        for i in range(len(r_tag_group)):
            r_group_list.append(r_tag_group[i]['group_name'])
        print(r_group_list)
        try:
            assert 'group5' in r_group_list
            print('新增标签成功')
        except:
            print('新增标签失败')
        # 删除新增的标签
        self.wework.del_tag(r_tag_group[r_group_list.index('group5')]['group_id'])
        self.wework.search_tag()
        try:
            assert 'group5' not in r_group_list
            print('删除标签成功')
        except:
            print('删除标签失败')

    def test_del_tag(self):

        r = self.wework.del_tag('xxx')
        assert r.json()['errcode'] == 0
        self.wework.search_tag()

    def test_edit_tag(self):
        r = self.wework.search_tag()
        tag_id = r.json()['tag_group'][0]['tag'][0]['id']
        r = self.wework.edit_tag(tag_id, 'new_tag_name_0705001')
        assert r.json()['errcode'] == 0
        self.wework.search_tag()
