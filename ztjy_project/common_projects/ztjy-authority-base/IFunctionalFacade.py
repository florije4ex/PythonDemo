# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IFunctionalFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IFunctionalFacade'
        self._method_addFunctional = 'addFunctional'
        self._method_addFunctionalPackage = 'addFunctionalPackage'
        self._method_addFunctionalPackageItem = 'addFunctionalPackageItem'
        self._method_addFunctionalPackageItemByCode = 'addFunctionalPackageItemByCode'
        self._method_addOfficeFunctionalPackageAuth = 'addOfficeFunctionalPackageAuth'
        self._method_addOfficeFunctionalTryAuth = 'addOfficeFunctionalTryAuth'
        self._method_closeRoleFunctionals = 'closeRoleFunctionals'
        self._method_delFunctional = 'delFunctional'
        self._method_delFunctionalPackage = 'delFunctionalPackage'
        self._method_delFunctionalPackageByCode = 'delFunctionalPackageByCode'
        self._method_delFunctionalPackageItem = 'delFunctionalPackageItem'
        self._method_delFunctionalPackageItemByCode = 'delFunctionalPackageItemByCode'
        self._method_delOfficeFunctionalPackageAuth = 'delOfficeFunctionalPackageAuth'
        self._method_deleteOfficeFunctionalTryAuth = 'deleteOfficeFunctionalTryAuth'
        self._method_findFunctionalByCode = 'findFunctionalByCode'
        self._method_findFunctionalByCodes = 'findFunctionalByCodes'
        self._method_findModuleFunctional = 'findModuleFunctional'
        self._method_findOfficeTryFunctionals = 'findOfficeTryFunctionals'
        self._method_getFunctionalPackage = 'getFunctionalPackage'
        self._method_getFunctionalPackageItems = 'getFunctionalPackageItems'
        self._method_getFunctionalPackageItemsByCode = 'getFunctionalPackageItemsByCode'
        self._method_getFunctionalPackagePage = 'getFunctionalPackagePage'
        self._method_getOfficeAuthFunctionalPackages = 'getOfficeAuthFunctionalPackages'
        self._method_getOfficeAuthFunctionals = 'getOfficeAuthFunctionals'
        self._method_getOfficeCloseFunctionals = 'getOfficeCloseFunctionals'
        self._method_getOfficeFunctionalPackages = 'getOfficeFunctionalPackages'
        self._method_getRoleAuthFunctionals = 'getRoleAuthFunctionals'
        self._method_getRoleAuthFunctionalsByCode = 'getRoleAuthFunctionalsByCode'
        self._method_updateFunctional = 'updateFunctional'
        self._method_updateFunctionalPackageDetailAuth = 'updateFunctionalPackageDetailAuth'
        self._method_updateFunctionalPackageName = 'updateFunctionalPackageName'
        self._method_updateOfficeCloseFunctionalAuth = 'updateOfficeCloseFunctionalAuth'
        self._method_updateOfficeFunctionalAuthByCode = 'updateOfficeFunctionalAuthByCode'
        self._method_updateOfficeFunctionalPackageAuth = 'updateOfficeFunctionalPackageAuth'
        self._method_updateOfficeFunctionalPackageAuthByCode = 'updateOfficeFunctionalPackageAuthByCode'
        self._method_updateRoleFunctionals = 'updateRoleFunctionals'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['functionalPackageDetailDTO']:
                    params.append({"type": "com.ztjy.authority.model.FunctionalPackageDetailDTO", "data": value})
                elif key in ['userCenterEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserCenterEnum", "data": value})
                elif key in ['functionalPackageId', 'officeId', 'roleId', 'functionalId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['pageNo', 'pageSize']:
                    params.append({"type": "java.lang.Integer", "data": value})
                elif key in ['newVersion', 'enable', 'force']:
                    params.append({"type": "boolean", "data": value})
                elif key in ['functionalIds']:
                    params.append({"type": "java.util.Collection", "data": value})
                elif key in ['functional']:
                    params.append({"type": "com.ztjy.authority.model.FunctionalDTO", "data": value})
                elif key in ['systemTypeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.SystemTypeEnum", "data": value})
                elif key in ['functionalIds']:
                    params.append({"type": "java.util.List", "data": value})
                elif key in ['functionalCodes']:
                    params.append({"type": "java.util.Set", "data": value})
                elif key in ['functionalCodes']:
                    params.append({"type": "java.util.Collection", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def addFunctional(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: FunctionalDTO functional
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addFunctional,
                                                      params=params)
        print('%s???addFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addFunctionalPackage(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: FunctionalPackageDetailDTO functionalPackageDetailDTO
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addFunctionalPackage?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addFunctionalPackage,
                                                      params=params)
        print('%s???addFunctionalPackage?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addFunctionalPackageItem(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalPackageId
        :param: List<Long> functionalIds
        :param: boolean newVersion
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addFunctionalPackageItem?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addFunctionalPackageItem,
                                                      params=params)
        print('%s???addFunctionalPackageItem?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addFunctionalPackageItemByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalPackageCode
        :param: String operateUserId
        :param: List<Long> functionalIds
        :param: boolean newVersion
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addFunctionalPackageItemByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addFunctionalPackageItemByCode,
                                                      params=params)
        print('%s???addFunctionalPackageItemByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addOfficeFunctionalPackageAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String functionalPackageCode
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addOfficeFunctionalPackageAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addOfficeFunctionalPackageAuth,
                                                      params=params)
        print('%s???addOfficeFunctionalPackageAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def addOfficeFunctionalTryAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Set<String> functionalCodes
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addOfficeFunctionalTryAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addOfficeFunctionalTryAuth,
                                                      params=params)
        print('%s???addOfficeFunctionalTryAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def closeRoleFunctionals(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long roleId
        :param: Collection<Long> functionalIds
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???closeRoleFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_closeRoleFunctionals,
                                                      params=params)
        print('%s???closeRoleFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delFunctional(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalId
        :param: boolean force
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delFunctional,
                                                      params=params)
        print('%s???delFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delFunctionalPackage(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalPackageId
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delFunctionalPackage?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delFunctionalPackage,
                                                      params=params)
        print('%s???delFunctionalPackage?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delFunctionalPackageByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalPackageCode
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delFunctionalPackageByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delFunctionalPackageByCode,
                                                      params=params)
        print('%s???delFunctionalPackageByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delFunctionalPackageItem(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalPackageId
        :param: List<Long> functionalIds
        :param: boolean newVersion
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delFunctionalPackageItem?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delFunctionalPackageItem,
                                                      params=params)
        print('%s???delFunctionalPackageItem?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delFunctionalPackageItemByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalPackageCode
        :param: String operateUserId
        :param: List<Long> functionalIds
        :param: boolean newVersion
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delFunctionalPackageItemByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delFunctionalPackageItemByCode,
                                                      params=params)
        print('%s???delFunctionalPackageItemByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def delOfficeFunctionalPackageAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String functionalPackageCode
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???delOfficeFunctionalPackageAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_delOfficeFunctionalPackageAuth,
                                                      params=params)
        print('%s???delOfficeFunctionalPackageAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def deleteOfficeFunctionalTryAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Set<String> functionalCodes
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???deleteOfficeFunctionalTryAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_deleteOfficeFunctionalTryAuth,
                                                      params=params)
        print('%s???deleteOfficeFunctionalTryAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def findFunctionalByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalCode
        """
        print('\n%s???findFunctionalByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findFunctionalByCode,
                                                      params=params)
        print('%s???findFunctionalByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def findFunctionalByCodes(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Collection<String> functionalCodes
        """
        print('\n%s???findFunctionalByCodes?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findFunctionalByCodes,
                                                      params=params)
        print('%s???findFunctionalByCodes?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def findModuleFunctional(self, params: str = None):
        """
        # TODO ??????????????????????????????
        """
        print('\n%s???findModuleFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findModuleFunctional,
                                                      params=params)
        print('%s???findModuleFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def findOfficeTryFunctionals(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: SystemTypeEnum systemTypeEnum
        """
        print('\n%s???findOfficeTryFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_findOfficeTryFunctionals,
                                                      params=params)
        print('%s???findOfficeTryFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getFunctionalPackage(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalPackageId
        """
        print('\n%s???getFunctionalPackage?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getFunctionalPackage,
                                                      params=params)
        print('%s???getFunctionalPackage?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getFunctionalPackageItems(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalPackageId
        """
        print('\n%s???getFunctionalPackageItems?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getFunctionalPackageItems,
                                                      params=params)
        print('%s???getFunctionalPackageItems?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getFunctionalPackageItemsByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String functionalPackageCode
        """
        print('\n%s???getFunctionalPackageItemsByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getFunctionalPackageItemsByCode,
                                                      params=params)
        print('%s???getFunctionalPackageItemsByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getFunctionalPackagePage(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Integer pageNo
        :param: Integer pageSize
        """
        print('\n%s???getFunctionalPackagePage?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getFunctionalPackagePage,
                                                      params=params)
        print('%s???getFunctionalPackagePage?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeAuthFunctionalPackages(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getOfficeAuthFunctionalPackages?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeAuthFunctionalPackages,
                                                      params=params)
        print('%s???getOfficeAuthFunctionalPackages?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeAuthFunctionals(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getOfficeAuthFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeAuthFunctionals,
                                                      params=params)
        print('%s???getOfficeAuthFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeCloseFunctionals(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getOfficeCloseFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeCloseFunctionals,
                                                      params=params)
        print('%s???getOfficeCloseFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeFunctionalPackages(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getOfficeFunctionalPackages?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeFunctionalPackages,
                                                      params=params)
        print('%s???getOfficeFunctionalPackages?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getRoleAuthFunctionals(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long roleId
        """
        print('\n%s???getRoleAuthFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getRoleAuthFunctionals,
                                                      params=params)
        print('%s???getRoleAuthFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getRoleAuthFunctionalsByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String roleCode
        """
        print('\n%s???getRoleAuthFunctionalsByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getRoleAuthFunctionalsByCode,
                                                      params=params)
        print('%s???getRoleAuthFunctionalsByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateFunctional(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: FunctionalDTO functional
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateFunctional,
                                                      params=params)
        print('%s???updateFunctional?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateFunctionalPackageDetailAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalPackageId
        :param: Collection<Long> functionalIds
        :param: boolean enable
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateFunctionalPackageDetailAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateFunctionalPackageDetailAuth,
                                                      params=params)
        print('%s???updateFunctionalPackageDetailAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateFunctionalPackageName(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long functionalPackageId
        :param: String functionalPackageName
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateFunctionalPackageName?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateFunctionalPackageName,
                                                      params=params)
        print('%s???updateFunctionalPackageName?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeCloseFunctionalAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Set<String> functionalCodes
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateOfficeCloseFunctionalAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeCloseFunctionalAuth,
                                                      params=params)
        print('%s???updateOfficeCloseFunctionalAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeFunctionalAuthByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Set<String> functionalCodes
        :param: boolean enable
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateOfficeFunctionalAuthByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeFunctionalAuthByCode,
                                                      params=params)
        print('%s???updateOfficeFunctionalAuthByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeFunctionalPackageAuth(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Long functionalPackageId
        :param: boolean enable
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateOfficeFunctionalPackageAuth?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeFunctionalPackageAuth,
                                                      params=params)
        print('%s???updateOfficeFunctionalPackageAuth?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOfficeFunctionalPackageAuthByCode(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String functionalPackageCode
        :param: String operateUserId
        :param: boolean enable
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateOfficeFunctionalPackageAuthByCode?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOfficeFunctionalPackageAuthByCode,
                                                      params=params)
        print('%s???updateOfficeFunctionalPackageAuthByCode?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateRoleFunctionals(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long roleId
        :param: Collection<Long> functionalIds
        :param: String operateUserId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateRoleFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateRoleFunctionals,
                                                      params=params)
        print('%s???updateRoleFunctionals?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

