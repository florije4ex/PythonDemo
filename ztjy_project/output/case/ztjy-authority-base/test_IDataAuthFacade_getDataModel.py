# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater
# TODO 用例模板生成后，需要人工调试，直到用例达到足够的覆盖率，并能全部测试通过

import allure
import pytest
from allpairspy import AllPairs
from assertpy import assert_that

from common_projects.api.ztjy.dubbo.ztjy_authority_base.IDataAuthFacade import IDataAuthFacade


@allure.description('负责人：XXXXXXX')
class Test_IDataAuthFacade_getDataModel(object):
    def setup_class(self):
        self._idataauthfacade = IDataAuthFacade()

    @pytest.mark.parametrize('['dataModelIds']', '')
    def test_IDataAuthFacade_getDataModel(self, dataModelIds):
        params = self._idataauthfacade.generator_params(dataModelIds=dataModelIds)
        try:
            result = self._idataauthfacade.getDataModel(params=params)
        except Exception as e:
            print("*" * 80)
            print(e.__str__())
            print("*" * 80)
            # TODO 断言逻辑待完善
            assert_that(e.__str__()).contains("NullPointerException", "NoSuchMethodException")
        else:
            # TODO 断言逻辑待完善
            assert_that(result).is_not_none()
