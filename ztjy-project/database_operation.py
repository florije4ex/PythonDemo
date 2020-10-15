# @File    : database_operation
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/1 15:08

for i in range(len(result)):
    assert_that(data[i]['DICT_CLASS_CODE']).is_equal_to(result[i]['dictClassCode'])

def insert_sql(self, **alterations):
    dbfields = str(tuple(alterations.keys())).replace("'", '')
    dbvalues = tuple(alterations.values())
    sql = 'INSERT INTO {table} {dbfields} VALUES {dbvalues}'.format(table=self.table, dbfields=dbfields,
                                                                    dbvalues=dbvalues)
    try:
        if self._db_hms_client.executeSQL(sql):
            print('SQL Insert Successful')
    except:
        print('SQL Insert Fail')

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

#第二个版本
def update_sales_order_sql(self, **alteration, **conditions):
    sql = 'UPDATE {table} SET '.format(table=self.table)
    update = ','.join(['%s = %r' % (k, v) for (k, v) in alteration.items()])  # 拼接需要更新的字段
    sql = sql + update + 'WHERE ' + ' AND '.join(['%s = %r' % (k, v) for (k, v) in conditions.items()])  # 拼接查询字段
    try:
        if self._db_sales_client.executeSQL(sql):
            print('SQL  Update Successful')
    except:
        print('SQL Update Fail')


def del_sql(self, **kwargs):
    sql = 'DELETE FROM {table}'.format(table=self.table)
    sql = sql + ' WHERE ' + ' AND '.join(['%s = %r' % (k, v) for (k, v) in kwargs.items()])
    try:
        if self._db_hms_client.executeSQL(sql):
            print('SQL Del Successful')
    except:
        print('SQL Del Fail')


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
#第一个版本
def select_sql(self, **kwargs):
    sqlSelct = 'SELECT * from {table}'.format(table=self.table)
    sql = sqlSelct + ' WHERE ' + ' AND '.join(
        ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])

    try:
        result = self._db_hms_client.executeSQL(sql)
        print("SQL Select Successful")
        return result
    except:
        print("SQL Select FAIL")

#第二个版本
def select_sql(self, groupBy: str = '', orderBy: str = '', sort: str = 'DESC', limitStart: int = '1',
               limitNum: int = '1', **kwargs):
    sqlSelct = 'SELECT * from {table}'.format(table=self.table)
    if orderBy != '':
        sqlWhere = sqlSelct + ' WHERE ' + ' AND '.join(
            ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
        sql = sqlWhere + ' ORDER BY {orderBy} {sort}'.format(orderBy=orderBy,
                                                             sort=sort) + ' LIMIT {limit},{num}'.format(
            limit=limitStart, num=limitNum)
    elif groupBy != '':
        sqlSelct = sqlSelct.replace('*', groupBy)
        sql = sqlSelct + ' GROUP BY {groupBy} '.format(groupBy=groupBy)
    else:
        sql = sqlSelct + ' WHERE ' + ' AND '.join(
            ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
    try:
        result = self._db_hms_client.executeSQL(sql)
        print("SQL Select Successful")
        return result
    except:
        print("SQL Select FAIL")

    def update_sql(self, classId: str = '', **alteration):
        updateSql = 'UPDATE {table} SET '.format(table=self.table)
        sql = updateSql + ','.join([' %s = % r ' % (k, v) for (k, v) in alteration.items()])
        if classId != '':
            sql = sql + ' WHERE ' + ' AND '.join([' ID = %r ' % classId])  # 拼接查询字段
        try:
            if self._db_school_client.executeSQL(sql):
                time.sleep(self.sleepTime)
        except:
            print('t_class SQL Update Fail')

def select_sql(self, isDistinct: str = '', deduplField: str = '', groupBy: str = '', orderBy: str = '',
               sort: str = 'DESC', limitStart: int = '1', limitNum: int = '1', **kwargs):
    sqlSelct = 'SELECT * from {table}'.format(table=self.table)
    if orderBy != '':
        # 排序
        sql = sqlSelct + ' WHERE ' + ' AND '.join(['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in
                                                   kwargs.items()]) + ' ORDER BY {orderBy} {sort}'.format(
            orderBy=orderBy, sort=sort) + ' LIMIT {limit},{num}'.format(limit=limitStart, num=limitNum)
    elif groupBy != '':
        # 根据字段聚合
        sql = sqlSelct.replace('*', groupBy) + ' WHERE ' + ' AND '.join(
            ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in
             kwargs.items()]) + ' GROUP BY {groupBy} '.format(groupBy=groupBy)
        if isDistinct != '':
            # 去重
            sql = sql.replace(deduplField, 'DISTINCT(%s)' % deduplField, 1)
    elif deduplField != '':
        sql = sqlSelct.replace('*', deduplField) + ' WHERE ' + ' AND '.join(
            ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
    else:
        sql = sqlSelct + ' WHERE ' + ' AND '.join(
            ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
    try:
        result = self._db_school_client.executeSQL(sql)
        print("t_class SQL Select Successful")
        return result
    except:
        print("t_class SQL Select FAIL")