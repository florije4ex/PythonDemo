# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IUserAuthFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IUserAuthFacade'
        self._method_findNotAuthFunctionalInOffice = 'findNotAuthFunctionalInOffice'
        self._method_findNotAuthFunctionalInOfficeWithDefault = 'findNotAuthFunctionalInOfficeWithDefault'
        self._method_getFunctionalUserExpireTime = 'getFunctionalUserExpireTime'
        self._method_getFunctionalUsersExpireTime = 'getFunctionalUsersExpireTime'
        self._method_getOfficeFunctionalAuthUsers = 'getOfficeFunctionalAuthUsers'
        self._method_getUserDataAuthLimit = 'getUserDataAuthLimit'
        self._method_getUserFunctionalList = 'getUserFunctionalList'
        self._method_getUserFunctionalListWithDefault = 'getUserFunctionalListWithDefault'
        self._method_getUserOfficeFunctionalList = 'getUserOfficeFunctionalList'
        self._method_getUserOfficeFunctionalListWithDefault = 'getUserOfficeFunctionalListWithDefault'
        self._method_isUserDataRoleAuth = 'isUserDataRoleAuth'
        self._method_isUserFunctionalAuth = 'isUserFunctionalAuth'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['officeId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['userTypeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserTypeEnum", "data": value})
                elif key in ['systemTypeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.SystemTypeEnum", "data": value})
                elif key in ['defaultRoles']:
                    params.append({"type": "java.util.Collection", "data": value})
                elif key in ['users', 'userIds']:
                    params.append({"type": "java.util.Set", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def findNotAuthFunctionalInOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String userId
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???findNotAuthFunctionalInOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findNotAuthFunctionalInOffice,
                                                      params=params)
        print('%s???findNotAuthFunctionalInOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def findNotAuthFunctionalInOfficeWithDefault(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String userId
        :param: Collection<Long> defaultRoles
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???findNotAuthFunctionalInOfficeWithDefault?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findNotAuthFunctionalInOfficeWithDefault,
                                                      params=params)
        print('%s???findNotAuthFunctionalInOfficeWithDefault?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getFunctionalUserExpireTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalCode
        :param: String userId
        :param: Long officeId
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???getFunctionalUserExpireTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getFunctionalUserExpireTime,
                                                      params=params)
        print('%s???getFunctionalUserExpireTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getFunctionalUsersExpireTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalCode
        :param: Long officeId
        :param: Set<String> userIds
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???getFunctionalUsersExpireTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getFunctionalUsersExpireTime,
                                                      params=params)
        print('%s???getFunctionalUsersExpireTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeFunctionalAuthUsers(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalCode
        :param: Long officeId
        """
        print('\n%s???getOfficeFunctionalAuthUsers?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeFunctionalAuthUsers,
                                                      params=params)
        print('%s???getOfficeFunctionalAuthUsers?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserDataAuthLimit(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String userId
        :param: String dataCode
        :param: UserTypeEnum userTypeEnum
        :param: Long officeId
        """
        print('\n%s???getUserDataAuthLimit?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserDataAuthLimit,
                                                      params=params)
        print('%s???getUserDataAuthLimit?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserFunctionalList(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String userId
        :param: Long officeId
        :param: UserTypeEnum userTypeEnum
        :param: SystemTypeEnum systemTypeEnum
        :param: Set<UserInfoDTO> users
        """
        print('\n%s???getUserFunctionalList?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserFunctionalList,
                                                      params=params)
        print('%s???getUserFunctionalList?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserFunctionalListWithDefault(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String userId
        :param: Long officeId
        :param: Collection<Long> defaultRoles
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???getUserFunctionalListWithDefault?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserFunctionalListWithDefault,
                                                      params=params)
        print('%s???getUserFunctionalListWithDefault?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserOfficeFunctionalList(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String userId
        :param: Long officeId
        :param: UserTypeEnum userTypeEnum
        :param: SystemTypeEnum systemTypeEnum
        """
        print('\n%s???getUserOfficeFunctionalList?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserOfficeFunctionalList,
                                                      params=params)
        print('%s???getUserOfficeFunctionalList?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserOfficeFunctionalListWithDefault(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String userId
        :param: Long officeId
        :param: Collection<Long> defaultRoles
        :param: UserTypeEnum userTypeEnum
        """
        print('\n%s???getUserOfficeFunctionalListWithDefault?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserOfficeFunctionalListWithDefault,
                                                      params=params)
        print('%s???getUserOfficeFunctionalListWithDefault?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def isUserDataRoleAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String userId
        :param: String dataCode
        :param: UserTypeEnum userTypeEnum
        :param: Long officeId
        """
        print('\n%s???isUserDataRoleAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_isUserDataRoleAuth,
                                                      params=params)
        print('%s???isUserDataRoleAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def isUserFunctionalAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        ??????1???????????????????????????
        ??????2?????????????????????ID????????????????????????????????????????????????????????????????????????????????????????????????????????????
        :param params1:java.lang.String userId,java.lang.Long officeId,UserTypeEnum userTypeEnum,java.lang.String functionalCode
        :param params2:java.util.Set<UserInfoDTO> users,java.lang.Long officeId,java.lang.String functionalCode
        :param: String userId
        :param: String functionalCode
        :param: Long officeId
        :param: UserTypeEnum userTypeEnum
        :param: Set<UserInfoDTO> users
        """
        print('\n%s???isUserFunctionalAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_isUserFunctionalAuth,
                                                      params=params)
        print('%s???isUserFunctionalAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

