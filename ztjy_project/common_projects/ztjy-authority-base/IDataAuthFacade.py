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
        # TODO ??????????????????????????????
        :param: String dataAuthGroupName
        :param: String dataAuthGroupCode
        :param: String userId
        :param: Long createOfficeId
        :param: Byte templateFlag
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataAuthGroup,
                                                      params=params)
        print('%s???addDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataAuthGroupInOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Long dataAuthGroupId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addDataAuthGroupInOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataAuthGroupInOffice,
                                                      params=params)
        print('%s???addDataAuthGroupInOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataAuthorityLimit(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthorityId
        :param: Long createOfficeId
        :param: List<DataAuthDetailDTO> dtoList
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s???addDataAuthorityLimit?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataAuthorityLimit,
                                                      params=params)
        print('%s???addDataAuthorityLimit?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataModel(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String dataName
        :param: String dataCode
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataModel,
                                                      params=params)
        print('%s???addDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addDataRoleAuthority(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: DataAuthDTO dto
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Long officeId
        :param: Boolean newVersion
        """
        print('\n%s???addDataRoleAuthority?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addDataRoleAuthority,
                                                      params=params)
        print('%s???addDataRoleAuthority?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataAuthGroup(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthGroupId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataAuthGroup,
                                                      params=params)
        print('%s???delDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataAuthorityLimit(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataLimitId
        :param: Long officeId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s???delDataAuthorityLimit?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataAuthorityLimit,
                                                      params=params)
        print('%s???delDataAuthorityLimit?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataModel(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataModelId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataModel,
                                                      params=params)
        print('%s???delDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delDataRoleAuthority(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthorityId
        :param: Long officeId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s???delDataRoleAuthority?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delDataRoleAuthority,
                                                      params=params)
        print('%s???delDataRoleAuthority?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delOfficeDataAuthGroup(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Collection<Long> dataAuthGroupIdList
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delOfficeDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delOfficeDataAuthGroup,
                                                      params=params)
        print('%s???delOfficeDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getAllDataModel(self, params: str = None):
        """
        # TODO ??????????????????????????????
        """
        print('\n%s???getAllDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getAllDataModel,
                                                      params=params)
        print('%s???getAllDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataAuthGroupByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String dataAuthGroupCode
        """
        print('\n%s???getDataAuthGroupByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataAuthGroupByCode,
                                                      params=params)
        print('%s???getDataAuthGroupByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataAuthGroupByCreateOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getDataAuthGroupByCreateOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataAuthGroupByCreateOffice,
                                                      params=params)
        print('%s???getDataAuthGroupByCreateOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataAuthorityLimit(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthorityId
        """
        print('\n%s???getDataAuthorityLimit?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataAuthorityLimit,
                                                      params=params)
        print('%s???getDataAuthorityLimit?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataModel(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Set<Long> dataModelIds
        """
        print('\n%s???getDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataModel,
                                                      params=params)
        print('%s???getDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getDataRoleAuthority(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthorityId
        """
        print('\n%s???getDataRoleAuthority?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getDataRoleAuthority,
                                                      params=params)
        print('%s???getDataRoleAuthority?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getGroupDataRoleAuthorityList(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthGroupId
        """
        print('\n%s???getGroupDataRoleAuthorityList?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getGroupDataRoleAuthorityList,
                                                      params=params)
        print('%s???getGroupDataRoleAuthorityList?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeDataAuthGroupByRelateOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getOfficeDataAuthGroupByRelateOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeDataAuthGroupByRelateOffice,
                                                      params=params)
        print('%s???getOfficeDataAuthGroupByRelateOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def switchOfficeDataAuthGroup(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Collection<Long> dataAuthGroupIdList
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean enable
        """
        print('\n%s???switchOfficeDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_switchOfficeDataAuthGroup,
                                                      params=params)
        print('%s???switchOfficeDataAuthGroup?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateAuthorityName(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthorityId
        :param: Long officeId
        :param: String dataAuthorityName
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s???updateAuthorityName?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateAuthorityName,
                                                      params=params)
        print('%s???updateAuthorityName?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateAuthorityType(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthorityId
        :param: Long officeId
        :param: DataAuthorityTypeEnum typeEnum
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        :param: Boolean newVersion
        """
        print('\n%s???updateAuthorityType?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateAuthorityType,
                                                      params=params)
        print('%s???updateAuthorityType?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateDataAuthGroupName(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataAuthGroupId
        :param: String dataAuthGroupName
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateDataAuthGroupName?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateDataAuthGroupName,
                                                      params=params)
        print('%s???updateDataAuthGroupName?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateDataModel(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long dataModelId
        :param: String dataName
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateDataModel,
                                                      params=params)
        print('%s???updateDataModel?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeDataAuthGroupExpireTime(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Long dataAuthGroupId
        :param: Date expiryTime
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateOfficeDataAuthGroupExpireTime?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeDataAuthGroupExpireTime,
                                                      params=params)
        print('%s???updateOfficeDataAuthGroupExpireTime?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

