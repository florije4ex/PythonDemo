# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IRoleFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IRoleFacade'
        self._method_addOfficeRole = 'addOfficeRole'
        self._method_addRoleTemplete = 'addRoleTemplete'
        self._method_clearOfficeRoles = 'clearOfficeRoles'
        self._method_delOfficeRole = 'delOfficeRole'
        self._method_delRoleTemplete = 'delRoleTemplete'
        self._method_getOfficeRoleList = 'getOfficeRoleList'
        self._method_getRoleTempletes = 'getRoleTempletes'
        self._method_getRoleUserFlags = 'getRoleUserFlags'
        self._method_getRoleUserIds = 'getRoleUserIds'
        self._method_getSysTempletesRole = 'getSysTempletesRole'
        self._method_getUserAllRoleList = 'getUserAllRoleList'
        self._method_getUserOfficeRoleList = 'getUserOfficeRoleList'
        self._method_joinOfficeRole = 'joinOfficeRole'
        self._method_leaveOfficeRole = 'leaveOfficeRole'
        self._method_updateOfficeRole = 'updateOfficeRole'
        self._method_updateOfficeRoleUsers = 'updateOfficeRoleUsers'
        self._method_updateOfficeRoleUsersAndInit = 'updateOfficeRoleUsersAndInit'
        self._method_updateUserOfficeRoles = 'updateUserOfficeRoles'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['roleDTO']:
                    params.append({"type": "com.ztjy.authority.model.RoleDTO", "data": value})
                elif key in ['userCenterEnum', 'systemType']:
                    params.append({"type": "com.ztjy.authority.constants.UserCenterEnum", "data": value})
                elif key in ['roleId', 'officeId', 'officeFunctionTempleteId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['force']:
                    params.append({"type": "boolean", "data": value})
                elif key in ['userType']:
                    params.append({"type": "java.lang.Byte", "data": value})
                elif key in ['userIds']:
                    params.append({"type": "java.util.Set", "data": value})
                elif key in ['userType']:
                    params.append({"type": "com.ztjy.authority.constants.UserTypeEnum", "data": value})
                elif key in ['roleTempleteDTO']:
                    params.append({"type": "com.ztjy.authority.model.RoleTempleteDTO", "data": value})
                elif key in ['pageNo', 'pageSize']:
                    params.append({"type": "java.lang.Integer", "data": value})
                elif key in ['officeTypeCodeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.OfficeTypeCodeEnum", "data": value})
                elif key in ['roleIds']:
                    params.append({"type": "java.util.Set", "data": value})
                elif key in ['initRoles']:
                    params.append({"type": "java.util.Map", "data": value})
                elif key in ['userIds']:
                    params.append({"type": "java.util.Collection", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def addOfficeRole(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: RoleDTO roleDTO
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【addOfficeRole】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addOfficeRole,
                                                      params=params)
        print('%s【addOfficeRole】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addRoleTemplete(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: RoleTempleteDTO roleTempleteDTO
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【addRoleTemplete】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addRoleTemplete,
                                                      params=params)
        print('%s【addRoleTemplete】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def clearOfficeRoles(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String userId
        :param: String operateUserId
        :param: Byte userType
        :param: Long officeId
        :param: UserCenterEnum systemType
        """
        print('\n%s【clearOfficeRoles】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_clearOfficeRoles,
                                                      params=params)
        print('%s【clearOfficeRoles】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delOfficeRole(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long roleId
        :param: Boolean force
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【delOfficeRole】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delOfficeRole,
                                                      params=params)
        print('%s【delOfficeRole】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delRoleTemplete(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeFunctionTempleteId
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【delRoleTemplete】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delRoleTemplete,
                                                      params=params)
        print('%s【delRoleTemplete】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeRoleList(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        """
        print('\n%s【getOfficeRoleList】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeRoleList,
                                                      params=params)
        print('%s【getOfficeRoleList】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getRoleTempletes(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Integer pageNo
        :param: Integer pageSize
        """
        print('\n%s【getRoleTempletes】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getRoleTempletes,
                                                      params=params)
        print('%s【getRoleTempletes】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getRoleUserFlags(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Collection<String> userIds
        :param: Byte userType
        :param: Long roleId
        :param: Long officeId
        """
        print('\n%s【getRoleUserFlags】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getRoleUserFlags,
                                                      params=params)
        print('%s【getRoleUserFlags】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getRoleUserIds(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long roleId
        :param: Long officeId
        :param: Byte userType
        """
        print('\n%s【getRoleUserIds】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getRoleUserIds,
                                                      params=params)
        print('%s【getRoleUserIds】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getSysTempletesRole(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: OfficeTypeCodeEnum officeTypeCodeEnum
        """
        print('\n%s【getSysTempletesRole】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getSysTempletesRole,
                                                      params=params)
        print('%s【getSysTempletesRole】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserAllRoleList(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String userId
        """
        print('\n%s【getUserAllRoleList】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserAllRoleList,
                                                      params=params)
        print('%s【getUserAllRoleList】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserOfficeRoleList(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String userId
        :param: UserTypeEnum userType
        :param: Long officeId
        """
        print('\n%s【getUserOfficeRoleList】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserOfficeRoleList,
                                                      params=params)
        print('%s【getUserOfficeRoleList】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def joinOfficeRole(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String userId
        :param: String operateUserId
        :param: Byte userType
        :param: Long officeId
        :param: Long roleId
        :param: UserCenterEnum systemType
        """
        print('\n%s【joinOfficeRole】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_joinOfficeRole,
                                                      params=params)
        print('%s【joinOfficeRole】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def leaveOfficeRole(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String userId
        :param: String operateUserId
        :param: Byte userType
        :param: Long officeId
        :param: Long roleId
        :param: UserCenterEnum systemType
        """
        print('\n%s【leaveOfficeRole】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_leaveOfficeRole,
                                                      params=params)
        print('%s【leaveOfficeRole】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeRole(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: RoleDTO roleDTO
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【updateOfficeRole】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeRole,
                                                      params=params)
        print('%s【updateOfficeRole】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeRoleUsers(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Set<String> userIds
        :param: Byte userType
        :param: Long officeId
        :param: Long roleId
        :param: String operateUserId
        :param: UserCenterEnum systemType
        """
        print('\n%s【updateOfficeRoleUsers】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeRoleUsers,
                                                      params=params)
        print('%s【updateOfficeRoleUsers】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeRoleUsersAndInit(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Set<String> userIds
        :param: Byte userType
        :param: Long officeId
        :param: Long roleId
        :param: Map<String_List<Long>> initRoles
        :param: String operateUserId
        :param: UserCenterEnum systemType
        """
        print('\n%s【updateOfficeRoleUsersAndInit】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeRoleUsersAndInit,
                                                      params=params)
        print('%s【updateOfficeRoleUsersAndInit】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateUserOfficeRoles(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String userId
        :param: String operateUserId
        :param: Byte userType
        :param: Long officeId
        :param: Set<Long> roleIds
        :param: UserCenterEnum systemType
        """
        print('\n%s【updateUserOfficeRoles】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateUserOfficeRoles,
                                                      params=params)
        print('%s【updateUserOfficeRoles】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

