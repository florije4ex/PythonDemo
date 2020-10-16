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
