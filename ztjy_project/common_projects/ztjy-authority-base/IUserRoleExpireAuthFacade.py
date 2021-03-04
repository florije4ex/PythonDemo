# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IUserRoleExpireAuthFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IUserRoleExpireAuthFacade'
        self._method_delayOfficeRoleExpiryTime = 'delayOfficeRoleExpiryTime'
        self._method_getUserRoleByFunctionalCode = 'getUserRoleByFunctionalCode'
        self._method_joinOfficeRole = 'joinOfficeRole'
        self._method_updateOfficeRoleExpiryTime = 'updateOfficeRoleExpiryTime'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['userRoleOprerateDTO']:
                    params.append({"type": "com.ztjy.authority.model.UserRoleOprerateDTO", "data": value})
                elif key in ['autoAuth']:
                    params.append({"type": "boolean", "data": value})
                elif key in ['officeId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['userTypeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserTypeEnum", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def delayOfficeRoleExpiryTime(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: UserRoleOprerateDTO userRoleOprerateDTO
        """
        print('\n%s【delayOfficeRoleExpiryTime】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delayOfficeRoleExpiryTime,
                                                      params=params)
        print('%s【delayOfficeRoleExpiryTime】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserRoleByFunctionalCode(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String functionalCode
        :param: String userId
        :param: Long officeId
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s【getUserRoleByFunctionalCode】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserRoleByFunctionalCode,
                                                      params=params)
        print('%s【getUserRoleByFunctionalCode】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def joinOfficeRole(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: UserRoleOprerateDTO userRoleOprerateDTO
        """
        print('\n%s【joinOfficeRole】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_joinOfficeRole,
                                                      params=params)
        print('%s【joinOfficeRole】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeRoleExpiryTime(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: UserRoleOprerateDTO userRoleOprerateDTO
        :param: boolean autoAuth
        """
        print('\n%s【updateOfficeRoleExpiryTime】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeRoleExpiryTime,
                                                      params=params)
        print('%s【updateOfficeRoleExpiryTime】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

