from testCase.testcase_base import Testcase_base
from util.commonTemplate import CommonTemplate
import allure
import yaml
import pytest

from util.handle_log import normal_logger, error_logger
from util.handle_yaml import Handle_yaml

@allure.feature("策略管理模块接口用例脚本")
class Test_ceLueGuanLi(Testcase_base):
    token = {"token": Testcase_base().get_token()}
    @allure.story("策略列表查询")
    @pytest.mark.parametrize('casedata', yaml.safe_load(open("data/fengKongJueCeYinqing/ceLueGuanLi/strategy-listQuery_data.yaml")))
    def test_remindMatterList(self, casedata):
        self.casedata = casedata
        casedata.update(self.token)
        self.data = CommonTemplate().template("api/fengKongJueCeYinqing/ceLueGuanLi/strategy-listQuery.yaml", self.casedata)
        self.r = self.getResponse(self.data)
        # 获取用例标题和测试用例描述
        description = casedata.get("description")
        uri = Handle_yaml("api/fengKongJueCeYinqing/ceLueGuanLi/strategy-listQuery.yaml").get_uri()
        try:
            expected_errMsg = self.casedata.get("veryfi").get("errMsg")
            assert (self.r.json()["errMsg"] == expected_errMsg)
            normal_logger.info(uri + "的" + description + "用例执行成功")
        except AssertionError as e:
            error_logger.error(uri + "的" + description + "用例执行失败:{}".format(e))
            raise e