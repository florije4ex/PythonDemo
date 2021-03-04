# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater
# TODO 用例模板生成后，需要人工调试，直到用例达到足够的覆盖率，并能全部测试通过

import allure
import pytest
from allpairspy import AllPairs
from assertpy import assert_that

from common_projects.api.ztjy.dubbo.ztjy_authority_base.IDataAuthFacade import IDataAuthFacade


def pairs_datas():
    """
    采取 pairwise ( 结对测试 ) 的测试策略进行用例设计，减少测试组合的同时最大化用例性价比
    :return: 符合正交分析结果的测试数据集
    """
    param_data = [
        ['ignore', None, '', 'OFFICEID', 'OF' * 11],  # OFFICEID
        ['ignore', None, '', 'DATAAUTHGROUPID', 'DA' * 11],  # DATAAUTHGROUPID
        ['ignore', None, '', 'EXPIRYTIME', 'EX' * 11],  # EXPIRYTIME
        ['ignore', None, '', 'USERID', 'US' * 11],  # USERID
        ['ignore', None, '', 'USERCENTERENUM', 'US' * 11],  # USERCENTERENUM
    ]
    return AllPairs(param_data)


@allure.description('负责人：XXXXXXX')
class Test_IDataAuthFacade_updateOfficeDataAuthGroupExpireTime(object):
    def setup_class(self):
        self._idataauthfacade = IDataAuthFacade()

    @pytest.mark.parametrize('officeId, dataAuthGroupId, expiryTime, userId, userCenterEnum', pairs_datas())
    def test_IDataAuthFacade_updateOfficeDataAuthGroupExpireTime(self, officeId, dataAuthGroupId, expiryTime, userId, userCenterEnum):
        params = self._idataauthfacade.generator_params(officeId=officeId, dataAuthGroupId=dataAuthGroupId, expiryTime=expiryTime, userId=userId, userCenterEnum=userCenterEnum)
        try:
            result = self._idataauthfacade.updateOfficeDataAuthGroupExpireTime(params=params)
        except Exception as e:
            print("*" * 80)
            print(e.__str__())
            print("*" * 80)
            # TODO 断言逻辑待完善
            assert_that(e.__str__()).contains("NullPointerException", "NoSuchMethodException")
        else:
            # TODO 断言逻辑待完善
            assert_that(result).is_not_none()

