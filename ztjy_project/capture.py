# @File    : capture
# @Description:
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2020/12/17 17:53

def capture_OfficeNotExistedFuncPkgAuthException(self, params):
    try:
        result = self.iUserAuthFacade.getFunctionalUsersExpireTime(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains("code=3021, msg='组织并不存在该功能组权限'")
    else:
        assert_that(result).is_none()


def capture_NullPointerException(self, params):
    try:
        result = self.iUserAuthFacade.getFunctionalUsersExpireTime(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains("NullPointerException")
    else:
        assert_that(result).is_none()


def capture_PrarmsIsException(self, params):
    try:
        result = self.iUserAuthFacade.getFunctionalUsersExpireTime(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains("code=3001, msg='参数异常'")
    else:
        assert_that(result).is_none()


def capture_PrarmsIsNull(self, params):
    try:
        result = self.iUserAuthFacade.getFunctionalUsersExpireTime(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains("code=3002, msg='参数为空'")
    else:
        assert_that(result).is_none()


def capture_NoSuchMethodException(self, params):
    try:
        result = self.iUserAuthFacade.getFunctionalUsersExpireTime(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains("NoSuchMethodException")
    else:
        assert_that(result).is_none()
