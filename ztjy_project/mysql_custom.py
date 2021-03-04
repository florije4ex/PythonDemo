# @File    : mysql_custom
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/17 20:00


class T_Teacher_Custom_Config_DB(object):

    def __init__(self):
        self._db_config_client = ZTJY_Mysql_Clients().db_config_client

    def select_datas(self, select_list=None, groupby_list=None, orderby_list=None, limit_tup=(0, 3), **where_kv_datas):
        sql = self._db_config_client.select(select_list=select_list) \
              + self._db_config_client.from_table(from_table='t_teacher_custom_config') \
              + self._db_config_client.where(**where_kv_datas) \
              + self._db_config_client.groupby(groupby_list=groupby_list) \
              + self._db_config_client.orderby(orderby_list=orderby_list) \
              + self._db_config_client.limit(limit_tup=limit_tup)
        print('DB_SQL >>> ', sql)
        result = self._db_config_client.executeSQL(sql)
        return result


def test_get_custom_config_normal_by_gardener(self):
    """
     * create by: zhangjf
     * create time: 2020/7/8 21:33
     * description: 正常合法有效的数据 园长角色
     * params:
     * return:
    """
    params = self.getCustomConfig.generator_get_custom_config_params(teacherid=self.gardenerid,
                                                                     schoolid=self.gardener_schoolid,
                                                                     configtype=1)
    result = self.getCustomConfig.get_custom_config(params=params)
    result_db = self.getCustomConfig_db.select_datas(select_list=['CONFIT_STR'],
                                                     TEACHER_ID=self.gardenerid,
                                                     SCHOOL_ID=self.gardener_schoolid,
                                                     CONFIG_TYPE=1)
    if result is None:
        assert_that(len(result_db)).is_equal_to(0)
    else:
        assert_that(result['configStr']).is_equal_to(result_db[0]['CONFIT_STR'])