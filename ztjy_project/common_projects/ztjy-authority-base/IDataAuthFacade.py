# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IDataAuthFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IDataAuthFacade'
        self._method_addDataAuthGroup = 'addDataAuthGroup'
        self._method_addDataAuthGroupInOffice = 'addDataAuthGroupInOffice'
        self._method_addDataAuthorityLimit = 'addDataAuthorityLimit'
        self._method_addDataModel = 'addDataModel'
        self._method_addDataRoleAuthority = 'addDataRoleAuthority'
        self._method_delDataAuthGroup = 'delDataAuthGroup'
        self._method_delDataAuthorityLimit = 'delDataAuthorityLimit'
        self._method_delDataModel = 'delDataModel'
        self._method_delDataRoleAuthority = 'delDataRoleAuthority'
        self._method_delOfficeDataAuthGroup = 'delOfficeDataAuthGroup'
        self._method_getAllDataModel = 'getAllDataModel'
        self._method_getDataAuthGroupByCode = 'getDataAuthGroupByCode'
        self._method_getDataAuthGroupByCreateOffice = 'getDataAuthGroupByCreateOffice'
        self._method_getDataAuthorityLimit = 'getDataAuthorityLimit'
        self._method_getDataModel = 'getDataModel'
        self._method_getDataRoleAuthority = 'getDataRoleAuthority'
        self._method_getGroupDataRoleAuthorityList = 'getGroupDataRoleAuthorityList'
        self._method_getOfficeDataAuthGroupByRelateOffice = 'getOfficeDataAuthGroupByRelateOffice'
        self._method_switchOfficeDataAuthGroup = 'switchOfficeDataAuthGroup'
        self._method_updateAuthorityName = 'updateAuthorityName'
        self._method_updateAuthorityType = 'updateAuthorityType'
        self._method_updateDataAuthGroupName = 'updateDataAuthGroupName'
        self._method_updateDataModel = 'updateDataModel'
        self._method_updateOfficeDataAuthGroupExpireTime = 'updateOfficeDataAuthGroupExpireTime'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['userCenterEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserCenterEnum", "data": value})
                elif key in ['dataModelId', 'dataAuthorityId', 'createOfficeId', 'dataLimitId', 'officeId', 'dataAuthGroupId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['dtoList']:
                    params.append({"type": "java.util.List", "data": value})
                elif key in ['newVersion', 'enable']:
                    params.append({"type": "boolean", "data": value})
                elif key in ['dto']:
                    params.append({"type": "com.ztjy.authority.model.DataAuthDTO", "data": value})
                elif key in ['typeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.DataAuthorityTypeEnum", "data": value})
                elif key in ['templateFlag']:
                    params.append({"type": "java.lang.Byte", "data": value})
                elif key in ['expiryTime']:
                    params.append({"type": "java.util.Date", "data": value})
                elif key in ['dataModelIds']:
                    params.append({"type": "java.util.Set", "data": value})
                elif key in ['dataAuthGroupIdList']:
                    params.append({"type": "java.util.Collection", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def addDataAuthGroup(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String dataAuthGroupName
        :param: String dataAuthGroupCode
        :param: String userId
        :param: Long createOfficeId
        :param: Byte templateFlag
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【addDataAuthGroup】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataAuthGroup,
                                                      params=params)
        print('%s【addDataAuthGroup】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataAuthGroupInOffice(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: Long dataAuthGroupId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【addDataAuthGroupInOffice】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataAuthGroupInOffice,
                                                      params=params)
        print('%s【addDataAuthGroupInOffice】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataAuthorityLimit(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthorityId
        :param: Long createOfficeId
        :param: List<DataAuthDetailDTO> dtoList
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s【addDataAuthorityLimit】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataAuthorityLimit,
                                                      params=params)
        print('%s【addDataAuthorityLimit】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataModel(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String dataName
        :param: String dataCode
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【addDataModel】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataModel,
                                                      params=params)
        print('%s【addDataModel】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataRoleAuthority(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: DataAuthDTO dto
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Long officeId
        :param: Boolean newVersion
        """
        print('\n%s【addDataRoleAuthority】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataRoleAuthority,
                                                      params=params)
        print('%s【addDataRoleAuthority】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataAuthGroup(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthGroupId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【delDataAuthGroup】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataAuthGroup,
                                                      params=params)
        print('%s【delDataAuthGroup】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataAuthorityLimit(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataLimitId
        :param: Long officeId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s【delDataAuthorityLimit】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataAuthorityLimit,
                                                      params=params)
        print('%s【delDataAuthorityLimit】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataModel(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataModelId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【delDataModel】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataModel,
                                                      params=params)
        print('%s【delDataModel】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataRoleAuthority(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthorityId
        :param: Long officeId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s【delDataRoleAuthority】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataRoleAuthority,
                                                      params=params)
        print('%s【delDataRoleAuthority】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delOfficeDataAuthGroup(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: Collection<Long> dataAuthGroupIdList
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【delOfficeDataAuthGroup】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delOfficeDataAuthGroup,
                                                      params=params)
        print('%s【delOfficeDataAuthGroup】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getAllDataModel(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        """
        print('\n%s【getAllDataModel】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getAllDataModel,
                                                      params=params)
        print('%s【getAllDataModel】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataAuthGroupByCode(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: String dataAuthGroupCode
        """
        print('\n%s【getDataAuthGroupByCode】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataAuthGroupByCode,
                                                      params=params)
        print('%s【getDataAuthGroupByCode】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataAuthGroupByCreateOffice(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        """
        print('\n%s【getDataAuthGroupByCreateOffice】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataAuthGroupByCreateOffice,
                                                      params=params)
        print('%s【getDataAuthGroupByCreateOffice】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataAuthorityLimit(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthorityId
        """
        print('\n%s【getDataAuthorityLimit】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataAuthorityLimit,
                                                      params=params)
        print('%s【getDataAuthorityLimit】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataModel(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Set<Long> dataModelIds
        """
        print('\n%s【getDataModel】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataModel,
                                                      params=params)
        print('%s【getDataModel】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataRoleAuthority(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthorityId
        """
        print('\n%s【getDataRoleAuthority】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataRoleAuthority,
                                                      params=params)
        print('%s【getDataRoleAuthority】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getGroupDataRoleAuthorityList(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthGroupId
        """
        print('\n%s【getGroupDataRoleAuthorityList】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getGroupDataRoleAuthorityList,
                                                      params=params)
        print('%s【getGroupDataRoleAuthorityList】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeDataAuthGroupByRelateOffice(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        """
        print('\n%s【getOfficeDataAuthGroupByRelateOffice】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeDataAuthGroupByRelateOffice,
                                                      params=params)
        print('%s【getOfficeDataAuthGroupByRelateOffice】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def switchOfficeDataAuthGroup(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: Collection<Long> dataAuthGroupIdList
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean enable
        """
        print('\n%s【switchOfficeDataAuthGroup】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_switchOfficeDataAuthGroup,
                                                      params=params)
        print('%s【switchOfficeDataAuthGroup】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateAuthorityName(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthorityId
        :param: Long officeId
        :param: String dataAuthorityName
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s【updateAuthorityName】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateAuthorityName,
                                                      params=params)
        print('%s【updateAuthorityName】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateAuthorityType(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthorityId
        :param: Long officeId
        :param: DataAuthorityTypeEnum typeEnum
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s【updateAuthorityType】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateAuthorityType,
                                                      params=params)
        print('%s【updateAuthorityType】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateDataAuthGroupName(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataAuthGroupId
        :param: String dataAuthGroupName
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【updateDataAuthGroupName】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateDataAuthGroupName,
                                                      params=params)
        print('%s【updateDataAuthGroupName】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateDataModel(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long dataModelId
        :param: String dataName
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【updateDataModel】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateDataModel,
                                                      params=params)
        print('%s【updateDataModel】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeDataAuthGroupExpireTime(self, params: str = None):
        """
        # TODO 相应的测试用例待调试
        :param: Long officeId
        :param: Long dataAuthGroupId
        :param: Date expiryTime
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s【updateOfficeDataAuthGroupExpireTime】【请求参数】%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeDataAuthGroupExpireTime,
                                                      params=params)
        print('%s【updateOfficeDataAuthGroupExpireTime】【响应信息】%s' % (DateTimeTool.getNowTime(), result))
        return result

