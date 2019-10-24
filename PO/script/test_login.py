import sys
import os

import allure

sys.path.append(os.getcwd())


from page.page_login import PageLogin
import pytest

#数据



def get_data():
    return  [("1564543445",123456),
            ("1564543445",123456),
            ("1564543445",123456)]
    # with open(Base_URL+os.sep+"data"+os.sep+filename,"r",encoding="utf-8")as f:
    #     print(yaml.load(f))

class Test_login:
    #初始化
    @allure.step(title="执行登陆")
    def setup_class(self):
    #获取pagelogin对象
        self.login=PageLogin()
    #关闭弹窗
        self.login.page_close_alert()
    #点击我
        self.login.page_click_me()
    #点击已有用户登录
        self.login.page_click_username_exite()

#结束
    @allure.step(title="执行退出")
    def teardown_class(self):
        # 关闭driver
        self.login.driver.quit()
# 测试方法
    @pytest.mark.parametrize('username,pwd',get_data())
    def test_login(self,username,pwd):
        allure.attach("描述","验证登陆")
        self.login.page_login(username,pwd)

    # def test_other(self):
    #     with open('./image')


