from base.httpRequest import HttpRequest
from util.commonTemplate import CommonTemplate
import yaml
from util.handle_log import error_logger,normal_logger



class Testcase_base():
    def setup(self):
        print('开始测试')


    def get_token(self):
        """
        使用固定账号登录获取token供其他接口使用
        :return:
        """
        userInfo = yaml.safe_load(open("data/tokenUser.yaml"))
        data = CommonTemplate().template("api/login.yaml",userInfo)
        self.response= self.getResponse(data)
        try:
            token=self.response.json()["data"]["token"]
            return token
        except Exception as e:
            error_logger.error("获取token失败")


    def getResponse(self,data):
        self.data = data
        self.httpRequest = HttpRequest(self.data)
        try:
            self.response = self.httpRequest.send_new()
            return self.response
        except Exception as e:
            error_logger.info("请求发送失败".format(e))


    def teardown(self):
        print('测试结束')


