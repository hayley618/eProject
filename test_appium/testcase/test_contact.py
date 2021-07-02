from faker import Faker
from test_appium.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.fake = Faker('zh-CN')

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_contact(self):
        name = self.fake.name()
        phonenumber = self.fake.phone_number()
        self.main.goto_contactlist().goto_add_member().addmember_send().add_member_send(name, phonenumber).find_toast()

    def test_contact2(self):
        name = self.fake.name()
        phonenumber = self.fake.phone_number()
        self.main.goto_contactlist().goto_add_member().addmember_send().add_member_send(name, phonenumber).find_toast()