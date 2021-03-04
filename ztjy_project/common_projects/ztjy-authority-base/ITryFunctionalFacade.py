# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class ITryFunctionalFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.ITryFunctionalFacade'
        self._method_addOfficeFunctionalTryAuth = 'addOfficeFunctionalTryAuth'
        self._method_deleteOfficeFunctionalTryAuth = 'deleteOfficeFunctionalTryAuth'
        self._method_findOfficeTryFunctionals = 'findOfficeTryFunctionals'
        self._method_findTryOfficeIdsByFunctionalCode = 'findTryOfficeIdsByFunctionalCode'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['officeId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['userCenterEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserCenterEnum", "data": value})
                elif key in ['systemTypeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.SystemTypeEnum", "data": value})
                elif key in ['page']:
                    params.append({"type": "com.ztjy.common.model.Page", "data": value})
                elif key in ['functionalCodes']:
                    params.append({"type": "java.util.Set", "data": value})
                elif key in ['page']:
                    params.append({"type": "com.ztjy.common.model.Page", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def addOfficeFunctionalTryAuth(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: Set<String> functionalCodes
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【addOfficeFunctionalTryAuth】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addOfficeFunctionalTryAuth,
                                                      params=params)
        print('%s【addOfficeFunctionalTryAuth】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def deleteOfficeFunctionalTryAuth(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: Set<String> functionalCodes
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【deleteOfficeFunctionalTryAuth】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_deleteOfficeFunctionalTryAuth,
                                                      params=params)
        print('%s【deleteOfficeFunctionalTryAuth】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def findOfficeTryFunctionals(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: String functionalCode
        :param: SystemTypeEnum systemTypeEnum
        :param: Page<FunctionalDTO> page
        """
        print('\n%s【findOfficeTryFunctionals】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findOfficeTryFunctionals,
                                                      params=params)
        print('%s【findOfficeTryFunctionals】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def findTryOfficeIdsByFunctionalCode(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String functionalCode
        :param: Page<Long> page
        """
        print('\n%s【findTryOfficeIdsByFunctionalCode】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findTryOfficeIdsByFunctionalCode,
                                                      params=params)
        print('%s【findTryOfficeIdsByFunctionalCode】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

