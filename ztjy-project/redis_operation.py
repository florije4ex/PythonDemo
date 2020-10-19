# @File    : redis_operation
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/10/16 14:10
class Hms_Redis:
    def __init__(self):
        self._hms_redis = ZTJY_Redis_Clients().hms_redis_db0

    def operation_redis(self, operation: str = 'get', **kwargs):
        redis_key = ':'.join(['%s' % v for v in kwargs.values()])
        if operation == 'exists':
            isExistedis = self._hms_redis.exists(redis_key)
            return isExistedis
        elif operation == 'get':
            redis_value = self._hms_redis.get(redis_key)
            return redis_value
        elif operation == 'ttl':
            redis_ttl_time = self._hms_redis.ttl(redis_key)
            return redis_ttl_time
        elif operation == 'keys':
            redis_keys = self._hms_redis.keys(redis_key)
            return redis_keys
        elif operation == 'delete':
            redis_keys_delete = self._hms_redis.delete(redis_key)
            return redis_keys_delete
        else:
            print("Redis Operation【%s】 Not Supported!!!"%operation)



@pytest.mark.parametrize("userType", (1, 2, 3))
    @pytest.mark.parametrize("schoolStatus", (0, 1))
    @pytest.mark.parametrize("isFlag", (0, 1))
    def test_update_password_and_clear_cache_check_field(self, fixture_init_data, userType, schoolStatus, isFlag):
        """
        :param fixture_init_data:
        :param userType: 1-'SUPER':超级账号, 2-'MAIN'：主账号, 3-'SUB'：子账号
        :param schoolStatus: 学校状态，1启用 0禁用
        :param isFlag: 删除标识1存在0不存在
        :return:
        """
        # 测试数据准备
        SCHOOL_USER_DB().update_sql(self.userName, is_flag=isFlag, status=schoolStatus, user_type=userType,
                                    user_pwd=self.md5OldPwd)
        Hms_Redis().operation_redis(self.redis_key, 'set', value=10)

        dto_params = self.iWSchoolUserFacade.generator_dto_params(userName=self.userName, md5Pwd=self.md5Pwd,
                                                                  userType=userType)
        params = self.iWSchoolUserFacade.generator_params(SchoolPasswordDTO=dto_params)
        result = self.iWSchoolUserFacade.updatePasswordAndClearCache(params=params)

        # 查数据库、缓存数据
        resultSql = SCHOOL_USER_DB().select_sql(user_name=self.userName)
        resultRedis = Hms_Redis().operation_redis(self.redis_key, 'exists')

        assert_that(result).is_none()
        assert_that(resultSql[0]['user_type']).is_equal_to(userType)
        assert_that(resultSql[0]['status']).is_equal_to(schoolStatus)
        assert_that(resultSql[0]['is_flag']).is_equal_to(isFlag)
        assert_that(resultSql[0]['user_pwd']).is_equal_to(self.md5Pwd)
        assert_that(resultRedis).is_false()