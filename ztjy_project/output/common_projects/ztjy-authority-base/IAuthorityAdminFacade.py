# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IAuthorityAdminFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IAuthorityAdminFacade'
        self._method_getAllFunctional = 'getAllFunctional'
        self._method_initNewRoleTemplete = 'initNewRoleTemplete'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['officeType']:
                    params.append({"type": "java.lang.Byte", "data": value})
                elif key in ['userCenterEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserCenterEnum", "data": value})
                elif key in ['functionalCodes']:
                    params.append({"type": "java.util.Set", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def getAllFunctional(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        """
        print('\n%s【getAllFunctional】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getAllFunctional,
                                                      params=params)
        print('%s【getAllFunctional】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def initNewRoleTemplete(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Byte officeType
        :param: String roleCode
        :param: String roleName
        :param: String operateUserId
        :param: Set<String> functionalCodes
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【initNewRoleTemplete】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_initNewRoleTemplete,
                                                      params=params)
        print('%s【initNewRoleTemplete】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

