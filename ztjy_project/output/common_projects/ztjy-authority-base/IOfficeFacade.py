# -\*- coding:utf8 -\*-
# * Created by IntelliJ IDEA.
# * User: RPCCreater


from base.api.ztjy.api_ztjy_client import API_ZTJY_Client
from common.dateTimeTool import DateTimeTool


class IOfficeFacade(object):
    def __init__(self):
        self.ztjy_client = API_ZTJY_Client()
        self._interface = 'com.ztjy.authority.facade.IOfficeFacade'
        self._method_addOffice = 'addOffice'
        self._method_batchFunctionalAuthOffice = 'batchFunctionalAuthOffice'
        self._method_batchGetOfficeInfo = 'batchGetOfficeInfo'
        self._method_changeParentOffice = 'changeParentOffice'
        self._method_deleteOffice = 'deleteOffice'
        self._method_deleteOfficeAndChildOffice = 'deleteOfficeAndChildOffice'
        self._method_getChildOffices = 'getChildOffices'
        self._method_getOfficeInfo = 'getOfficeInfo'
        self._method_getParentOffice = 'getParentOffice'
        self._method_getUserOffices = 'getUserOffices'
        self._method_insertOffice = 'insertOffice'
        self._method_isChildOffice = 'isChildOffice'
        self._method_syncOfficeInfo = 'syncOfficeInfo'
        self._method_updateOffice = 'updateOffice'

    def generator_params(self, **kwargs):
        params = []
        for key, value in kwargs.items():
            if value != 'ignore':
                if key in ['parentOfficeId', 'officeId']:
                    params.append({"type": "java.lang.Long", "data": value})
                elif key in ['officeTypeCodeEnum']:
                    params.append({"type": "com.ztjy.authority.constants.OfficeTypeCodeEnum", "data": value})
                elif key in ['userCenterEnum']:
                    params.append({"type": "com.ztjy.authority.constants.UserCenterEnum", "data": value})
                elif key in ['officeDTO']:
                    params.append({"type": "com.ztjy.authority.model.OfficeDTO", "data": value})
                elif key in ['childOfficeIds', 'officeIds']:
                    params.append({"type": "java.util.List", "data": value})
                elif key in ['officeIds']:
                    params.append({"type": "java.util.Collection", "data": value})
                else:
                    params.append({"type": "java.lang.String", "data": value})
        return params

    def addOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long parentOfficeId
        :param: String outerId
        :param: String officeName
        :param: String userId
        :param: OfficeTypeCodeEnum officeTypeCodeEnum
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???addOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_addOffice,
                                                      params=params)
        print('%s???addOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def batchFunctionalAuthOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Collection<Long> officeIds
        :param: String functionalCode
        """
        print('\n%s???batchFunctionalAuthOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_batchFunctionalAuthOffice,
                                                      params=params)
        print('%s???batchFunctionalAuthOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def batchGetOfficeInfo(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: List<Long> officeIds
        """
        print('\n%s???batchGetOfficeInfo?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_batchGetOfficeInfo,
                                                      params=params)
        print('%s???batchGetOfficeInfo?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def changeParentOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Long parentOfficeId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???changeParentOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_changeParentOffice,
                                                      params=params)
        print('%s???changeParentOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def deleteOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???deleteOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_deleteOffice,
                                                      params=params)
        print('%s???deleteOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def deleteOfficeAndChildOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???deleteOfficeAndChildOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_deleteOfficeAndChildOffice,
                                                      params=params)
        print('%s???deleteOfficeAndChildOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getChildOffices(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getChildOffices?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getChildOffices,
                                                      params=params)
        print('%s???getChildOffices?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getOfficeInfo(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getOfficeInfo?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getOfficeInfo,
                                                      params=params)
        print('%s???getOfficeInfo?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getParentOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        """
        print('\n%s???getParentOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getParentOffice,
                                                      params=params)
        print('%s???getParentOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def getUserOffices(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: String userId
        """
        print('\n%s???getUserOffices?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_getUserOffices,
                                                      params=params)
        print('%s???getUserOffices?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def insertOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long parentOfficeId
        :param: String outerId
        :param: String officeName
        :param: String userId
        :param: List<Long> childOfficeIds
        :param: OfficeTypeCodeEnum officeTypeCodeEnum
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???insertOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_insertOffice,
                                                      params=params)
        print('%s???insertOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def isChildOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: Long parentOfficeId
        """
        print('\n%s???isChildOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_isChildOffice,
                                                      params=params)
        print('%s???isChildOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def syncOfficeInfo(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: OfficeDTO officeDTO
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???syncOfficeInfo?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_syncOfficeInfo,
                                                      params=params)
        print('%s???syncOfficeInfo?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

    def updateOffice(self, params: str = None):
        """
        # TODO ??????????????????????????????
        :param: Long officeId
        :param: String officeName
        :param: String userId
        :param: UserCenterEnum userCenterEnum
        """
        print('\n%s???updateOffice?????????????????????%s' % (DateTimeTool.getNowTime(), params))
        result = self.ztjy_client.dubboClient.request(requestInterfaceClassName=self._interface,
                                                      requestMethod=self._method_updateOffice,
                                                      params=params)
        print('%s???updateOffice?????????????????????%s' % (DateTimeTool.getNowTime(), result))
        return result

