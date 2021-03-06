# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IUserFuncPkgExpireAuthFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IUserFuncPkgExpireAuthFacade'
        self._method_batchUpdateUserFuncPkgExpiryTime = 'batchUpdateUserFuncPkgExpiryTime'
        self._method_batchUserFuncPkgAuth = 'batchUserFuncPkgAuth'
        self._method_batchUserFuncPkgExpiryTime = 'batchUserFuncPkgExpiryTime'
        self._method_clearOfficeFuncPkgExpireAuthUsers = 'clearOfficeFuncPkgExpireAuthUsers'
        self._method_delayUserFuncPkgExpiryTime = 'delayUserFuncPkgExpiryTime'
        self._method_getUserFuncPkgExpiryTime = 'getUserFuncPkgExpiryTime'
        self._method_updateUserFuncPkgExpiryTime = 'updateUserFuncPkgExpiryTime'
        self._method_userFuncPkgAuth = 'userFuncPkgAuth'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['userFunctionalPackageOprerateDTO']:
                    params.append({"type": "com.ztjy.authority.model.UserFunctionalPackageOprerateDTO", "data": value})
                elif key in ['autoAuth']:
                    params.append({"type": "boolean", "data": value})
                elif key in ['officeId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['userTypeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserTypeEnum", "data": value})
                elif key in ['systemType']:
                    params.append({"type": "com.ztjy.authority.constants.UserCenterEnum", "data": value})
                elif key in ['userFunctionalPackageOprerateDTOs']:
                    params.append({"type": "java.util.Set", "data": value})
                elif key in ['userIds']:
                    params.append({"type": "java.util.Collection", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def batchUpdateUserFuncPkgExpiryTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Set<UserFunctionalPackageOprerateDTO> userFunctionalPackageOprerateDTOs
        :param: boolean autoAuth
        """
        print('\n%s???batchUpdateUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_batchUpdateUserFuncPkgExpiryTime,
                                                      params=params)
        print('%s???batchUpdateUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def batchUserFuncPkgAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Set<UserFunctionalPackageOprerateDTO> userFunctionalPackageOprerateDTOs
        """
        print('\n%s???batchUserFuncPkgAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_batchUserFuncPkgAuth,
                                                      params=params)
        print('%s???batchUserFuncPkgAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def batchUserFuncPkgExpiryTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalPackageCode
        :param: Long officeId
        :param: Collection<String> userIds
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???batchUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_batchUserFuncPkgExpiryTime,
                                                      params=params)
        print('%s???batchUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def clearOfficeFuncPkgExpireAuthUsers(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalPackageCode
        :param: String operateUserId
        :param: Long officeId
        :param: UserCenterEnum systemType
        """
        print('\n%s???clearOfficeFuncPkgExpireAuthUsers?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_clearOfficeFuncPkgExpireAuthUsers,
                                                      params=params)
        print('%s???clearOfficeFuncPkgExpireAuthUsers?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delayUserFuncPkgExpiryTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: UserFunctionalPackageOprerateDTO userFunctionalPackageOprerateDTO
        """
        print('\n%s???delayUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delayUserFuncPkgExpiryTime,
                                                      params=params)
        print('%s???delayUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserFuncPkgExpiryTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalPackageCode
        :param: String userId
        :param: Long officeId
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???getUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserFuncPkgExpiryTime,
                                                      params=params)
        print('%s???getUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateUserFuncPkgExpiryTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: UserFunctionalPackageOprerateDTO userFunctionalPackageOprerateDTO
        :param: boolean autoAuth
        """
        print('\n%s???updateUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateUserFuncPkgExpiryTime,
                                                      params=params)
        print('%s???updateUserFuncPkgExpiryTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def userFuncPkgAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: UserFunctionalPackageOprerateDTO userFunctionalPackageOprerateDTO
        """
        print('\n%s???userFuncPkgAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_userFuncPkgAuth,
                                                      params=params)
        print('%s???userFuncPkgAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

