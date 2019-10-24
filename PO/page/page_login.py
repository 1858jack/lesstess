

import page
from base.base import Base



class PageLogin(Base):
    #关闭弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)
    # 点击我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击已有账号
    def page_click_username_exite(self):
        self.base_click(page.login_username_exists)

    # 输入用户名
    def page_input_usertname(self,username):
        self.base_input(page.login_username,username)

    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)

    # 点击登陆
    def page_click_login(self):
        self.base_click(page.login_btn)

    #综合业务
    def page_login(self,username,pwd):

        self.page_input_usertname(username)
        # sleep(2)
        self.page_input_pwd(pwd)
        # sleep(2)
        self.page_click_login()

