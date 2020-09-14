# @File    : database_operation
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/1 15:08


def update_sales_order_sql(self, SelectField, updateField):
    table = 't_sales_order'  # 表
    sql = 'UPDATE {table} SET '.format(table=table)
    update = ','.join(['%s = %r' % (key, updateField[key]) for key in updateField])  # 拼接需要更新的字段
    where = ' AND '.join(['%s = %r' % (key, SelectField[key]) for key in SelectField])  # 拼接查询字段
    where = 'WHERE ' + where
    sql += update
    sql += where  # 完成sql拼装
    try:
        if self._db_sales_client.executeSQL(sql):
            print('SQL  Update Successful')
    except:
        print('SQL Update Fail')


def select_sales_order_info_sql(self, SelectField):
    table = 't_sales_order'
    sql = 'SELECT * from {table}  WHERE '.format(table=table)
    where = ' AND '.join(['%s = %r' % (key, SelectField[key]) for key in SelectField])  # 拼接查询字段
    sql += where  # 完成sql拼装
    try:
        result = self._db_sales_client.executeSQL(sql)
        return result
        print("SQL Select Successful")
    except:
        print("SQL Select FAIL")