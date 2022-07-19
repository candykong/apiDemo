import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import allure
from testCase.testcase_base import Testcase_base
from util.commonTemplate import CommonTemplate
import pytest
import yaml
from util.handle_log import error_logger,normal_logger
from util.handle_yaml import Handle_yaml


@allure.feature("测试登录退出模块")
class Test_login(Testcase_base):

    @allure.story("登录接口")
    @pytest.mark.parametrize('casedata', yaml.safe_load(open("data/login_data.yaml")))
    def test_login(self,casedata):
        self.casedata=casedata
        self.data = CommonTemplate().template("api/login.yaml", self.casedata)
        self.r=self.getResponse(self.data)
        # 获取用例标题和测试用例描述
        description = casedata.get("description")
        uri = Handle_yaml("api/login.yaml").get_uri()
        try:
            expected_errMsg=self.casedata.get("veryfi").get("errMsg")
            assert (self.r.json()["errMsg"] == expected_errMsg)
            normal_logger.info(uri+"的"+description+"用例执行成功")
        except AssertionError as e:
            error_logger.error(uri+"的"+description+"用例执行失败:{}".format(e))
            raise e

