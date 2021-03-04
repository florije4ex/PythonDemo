# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IOfficeFuncExpireAuthFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IOfficeFuncExpireAuthFacade'
        self._method_addOfficeFunctionalPackageExpiryAuth = 'addOfficeFunctionalPackageExpiryAuth'
        self._method_delayOfficeFuncPkgExpiryTime = 'delayOfficeFuncPkgExpiryTime'
        self._method_getFunctionalOfficeExpireTime = 'getFunctionalOfficeExpireTime'
        self._method_getOfficeAuthWithBaseAndTryFunctionals = 'getOfficeAuthWithBaseAndTryFunctionals'
        self._method_hasOfficeFunctionalWithBaseAndTry = 'hasOfficeFunctionalWithBaseAndTry'
        self._method_updateOfficeFunctionalPackageExpiryTime = 'updateOfficeFunctionalPackageExpiryTime'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['officeFunctionalPackageOprerateDTO']:
                    params.append({"type": "com.ztjy.authority.model.OfficeFunctionalPackageOprerateDTO", "data": value})
                elif key in ['officeId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['systemTypeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.SystemTypeEnum", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def addOfficeFunctionalPackageExpiryAuth(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: OfficeFunctionalPackageOprerateDTO officeFunctionalPackageOprerateDTO
        """
        print('\n%s【addOfficeFunctionalPackageExpiryAuth】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addOfficeFunctionalPackageExpiryAuth,
                                                      params=params)
        print('%s【addOfficeFunctionalPackageExpiryAuth】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delayOfficeFuncPkgExpiryTime(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: OfficeFunctionalPackageOprerateDTO officeFunctionalPackageOprerateDTO
        """
        print('\n%s【delayOfficeFuncPkgExpiryTime】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delayOfficeFuncPkgExpiryTime,
                                                      params=params)
        print('%s【delayOfficeFuncPkgExpiryTime】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getFunctionalOfficeExpireTime(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String functionalCode
        :param: Long officeId
        """
        print('\n%s【getFunctionalOfficeExpireTime】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getFunctionalOfficeExpireTime,
                                                      params=params)
        print('%s【getFunctionalOfficeExpireTime】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeAuthWithBaseAndTryFunctionals(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: SystemTypeEnum systemTypeEnum
        """
        print('\n%s【getOfficeAuthWithBaseAndTryFunctionals】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeAuthWithBaseAndTryFunctionals,
                                                      params=params)
        print('%s【getOfficeAuthWithBaseAndTryFunctionals】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def hasOfficeFunctionalWithBaseAndTry(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: String functionalCode
        """
        print('\n%s【hasOfficeFunctionalWithBaseAndTry】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_hasOfficeFunctionalWithBaseAndTry,
                                                      params=params)
        print('%s【hasOfficeFunctionalWithBaseAndTry】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeFunctionalPackageExpiryTime(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: OfficeFunctionalPackageOprerateDTO officeFunctionalPackageOprerateDTO
        """
        print('\n%s【updateOfficeFunctionalPackageExpiryTime】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeFunctionalPackageExpiryTime,
                                                      params=params)
        print('%s【updateOfficeFunctionalPackageExpiryTime】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

