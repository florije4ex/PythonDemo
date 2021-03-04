# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater
# TODO 用例模板生成后，需要人工调试，直到用例达到足够的覆盖率，并能全部测试通过

import allure
import pytest
from allpairspy import AllPairs
from assertpy import assert_that

from common_projects.api.ztjy.dubbo.ztjy_authority_base.ITryFunctionalFacade import ITryFunctionalFacade


def pairs_datas():
    """
    采取 pairwise ( 结对测试 ) 的测试策略进行用例设计，减少测试组合的同时最大化用例性价比
    :return: 符合正交分析结果的测试数据集
    """
    param_data = [
        ['ignore', None, '', 'OFFICEID', 'OF' * 11],  # OFFICEID
        ['ignore', None, '', 'FUNCTIONALCODES', 'FU' * 11],  # FUNCTIONALCODES
        ['ignore', None, '', 'OPERATEUSERID', 'OP' * 11],  # OPERATEUSERID
        ['ignore', None, '', 'USERCENTERENUM', 'US' * 11],  # USERCENTERENUM
    ]
    return AllPairs(param_data)


@allure.description('负责人：XXXXXXX')
class Test_ITryFunctionalFacade_deleteOfficeFunctionalTryAuth(object):
    def setup_class(self):
        self._itryfunctionalfacade = ITryFunctionalFacade()

    @pytest.mark.parametrize('officeId, functionalCodes, operateUserId, userCenterEnum', pairs_datas())
    def test_ITryFunctionalFacade_deleteOfficeFunctionalTryAuth(self, officeId, functionalCodes, operateUserId, userCenterEnum):
        params = self._itryfunctionalfacade.generator_params(officeId=officeId, functionalCodes=functionalCodes, operateUserId=operateUserId, userCenterEnum=userCenterEnum)
        try:
            result = self._itryfunctionalfacade.deleteOfficeFunctionalTryAuth(params=params)
        except Exception as e:
            print("*" * 80)
            print(e.__str__())
            print("*" * 80)
            # TODO 断言逻辑待完善
            assert_that(e.__str__()).contains("NullPointerException", "NoSuchMethodException")
        else:
            # TODO 断言逻辑待完善
            assert_that(result).is_not_none()

