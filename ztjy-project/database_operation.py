# @File    : database_operation
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/1 15:08








class Database_Operation:
    def __init__(self):
        self._db_client = ZTJY_Mysql_Clients().db_authority_client
        self.table = 't_office'

    def insert_sql(self, **kwargs):
        """
        :param kwargs: 插入字段=值
        :return:
        """
        dbfields = str(tuple(kwargs.keys())).replace("'", '')
        dbvalues = tuple(kwargs.values())
        sql = 'INSERT INTO {table} {dbfields} VALUES {dbvalues}'.format(table=self.table, dbfields=dbfields,
                                                                        dbvalues=dbvalues)
        sql = sql.replace("None", 'NULL')
        try:
            self._db_client.executeSQL(sql)
        except:
            print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))

    def del_sql(self, **kwargs):
        """
        :param kwargs: 查询条件
        :return:
        """
        sql = 'DELETE FROM {table}'.format(table=self.table)
        sql = sql + ' WHERE ' + ' AND '.join(['%s = %r' % (k, v) for (k, v) in kwargs.items()])
        try:
            self._db_client.executeSQL(sql)
        except:
            print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))

    def update_sql(self, conditions: str = None, **kwargs):
        """
        :param conditions: 查询条件
        :param kwargs: 需要更新的字段
        :return:
        """
        sql = 'UPDATE {table} SET '.format(table=self.table) + ','.join(
            ['%s = %r' % (k, v) for (k, v) in kwargs.items()])  # 拼接需要更新的字段
        if conditions is not None:
            sql = sql + ' WHERE %s' % conditions  # 拼接查询字段
            sql = sql.replace("None", 'NULL')
        try:
            self._db_client.executeSQL(sql)
        except:
            print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))

    def select_sql(self, returnField: str = None, multiValueField: str = None, groupByField: str = None, orderByField: str = None, limit: int = None, **kwargs):
        """
        :param returnField 返回字段
        :param multiValueField: 查询字段传入多个值，=替换为in，传入的值必须为str
        :param groupByField: 聚合
        :param orderByField: 排序字段, 加上  'filed DESC '：按照filed倒序，‘filed’：按照file顺序
        :param limit: 查询数量，'2,3'：从第二条查询结果，查询3条记录，‘3’：查询3条记录
        :param kwargs: 查询字段，按key=value 格式
        :return:
        """
        sql = 'SELECT * from %s' % self.table
        if kwargs:
            sql = sql + ' WHERE ' + ' AND '.join(['%s = %r ' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
        if multiValueField is not None:
            # 包含多个值的字段，multiValueField为kwargs某一个key，value包含多个值
            for k, v in kwargs.items():
                if k == multiValueField:
                    sql = StrTool.replaceContentWithLBRB(sql, ' IN(', k, v, 0)
                    sql = StrTool.replaceContentWithLBRB(sql, ')', v, " ", 0)
        if returnField is not None:
            # 返回的字段
            sql = sql.replace('*', returnField)
        if groupByField is not None:
            # 根据字段聚合
            sql = sql + ' GROUP BY %s ' % groupByField
        if orderByField is not None:
            # 排序
            sql = sql + ' ORDER BY %s' % orderByField
        if limit is not None:
            sql = sql + ' LIMIT %s ' % limit
        try:
            result = self._db_client.executeSQL(sql)
            return result
        except:
            print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))
            print('SQL Update Fail %s' % (traceback.print_exc()))


class History_Version:

    def abc(self):
        for i in range(len(result)):
            assert_that(data[i]['DICT_CLASS_CODE']).is_equal_to(result[i]['dictClassCode'])

    def insert_sql(self, **alterations):
        dbfields = str(tuple(alterations.keys())).replace("'", '')
        dbvalues = tuple(alterations.values())
        sql = 'INSERT INTO {table} {dbfields} VALUES {dbvalues}'.format(table=self.table, dbfields=dbfields,
                                                                        dbvalues=dbvalues)
        sql = sql.replace("'null'", 'NULL')
        try:
            if self._db_client.executeSQL(sql):
                print('SQL Insert Successful')
        except:
            print('SQL Insert Fail')


    def update_sql(self, userId, **alteration):
        sql = 'UPDATE {table} SET '.format(table=self.table) + ','.join(
            ['%s = %r' % (k, v) for (k, v) in alteration.items()])
        sql = sql + ' WHERE ' + ' AND '.join(['user_id = "%s"' % userId])  # 拼接查询字段
        try:
            if self._db_client.executeSQL(sql):
                print('%s SQL  Update Successful' % self.table)
        except:
            print('%s SQL Update Fail' % self.table)

    #第二个版本
    def update_sales_order_sql(self, **alteration, **conditions):
        sql = 'UPDATE {table} SET '.format(table=self.table)
        update = ','.join(['%s = %r' % (k, v) for (k, v) in alteration.items()])  # 拼接需要更新的字段
        sql = sql + update + 'WHERE ' + ' AND '.join(['%s = %r' % (k, v) for (k, v) in conditions.items()])  # 拼接查询字段
        try:
            if self._db_client.executeSQL(sql):
                print('SQL  Update Successful')
        except:
            print('SQL Update Fail')


    def del_sql(self, **kwargs):
        sql = 'DELETE FROM {table}'.format(table=self.table)
        sql = sql + ' WHERE ' + ' AND '.join(['%s = %r' % (k, v) for (k, v) in kwargs.items()])
        try:
            if self._db_client.executeSQL(sql):
                print('SQL Del Successful')
        except:
            print('SQL Del Fail')


    def select_sales_order_info_sql(self, SelectField):
        table = 't_sales_order'
        sql = 'SELECT * from {table}  WHERE '.format(table=table)
        where = ' AND '.join(['%s = %r' % (key, SelectField[key]) for key in SelectField])  # 拼接查询字段
        sql += where  # 完成sql拼装
        try:
            result = self._db_client.executeSQL(sql)
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
            result = self._db_client.executeSQL(sql)
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
            result = self._db_client.executeSQL(sql)
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
                if self._db_client.executeSQL(sql):
                    time.sleep(self.sleepTime)
            except:
                print('t_class SQL Update Fail')

    class Role_User_Ridx_DB:
        def __init__(self):
            self._db_client = ZTJY_Mysql_Clients().db_authority_client
            self.table = 't_role_user_ridx'

        def select_sql(self, isDistinct: str = None, deduplField: str = None, groupBy: str = None, orderBy: str = None,
                       sort: str = 'DESC', limitStart: int = None, limitNum: int = None, **kwargs):
            sqlSelct = 'SELECT * from {table}'.format(table=self.table)
            if orderBy != None:
                # 排序
                sql = sqlSelct + ' WHERE ' + ' AND '.join(['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in
                                                           kwargs.items()]) + ' ORDER BY {orderBy} {sort}'.format(
                    orderBy=orderBy, sort=sort) + ' LIMIT {limit},{num}'.format(limit=limitStart, num=limitNum)
            elif groupBy != None:
                # 根据字段聚合
                sql = sqlSelct.replace('*', groupBy) + ' WHERE ' + ' AND '.join(
                    ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in
                     kwargs.items()]) + ' GROUP BY {groupBy} '.format(groupBy=groupBy)
                if isDistinct != None:
                    # 去重
                    sql = sql.replace(deduplField, 'DISTINCT(%s)' % deduplField, 1)
            elif deduplField != None:
                sql = sqlSelct.replace('*', deduplField) + ' WHERE ' + ' AND '.join(
                    ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
            else:
                sql = sqlSelct + ' WHERE ' + ' AND '.join(
                    ['%s = %r' % (str(k).replace("'", ''), v) for (k, v) in kwargs.items()])
            try:
                result = self._db_client.executeSQL(sql)
                return result
            except:
                print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))

        def update_sql(self, userId, **alteration):
            sql = 'UPDATE {table} SET '.format(table=self.table) + ','.join(
                ['%s = %r' % (k, v) for (k, v) in alteration.items()])
            sql = sql + ' WHERE ' + ' AND '.join(['user_id = "%s"' % userId])  # 拼接查询字段
            try:
                self._db_client.executeSQL(sql)
            except:
                print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))

        def del_sql(self, **kwargs):
            sql = 'DELETE FROM {table}'.format(table=self.table)
            sql = sql + ' WHERE ' + ' AND '.join(['%s = %r' % (k, v) for (k, v) in kwargs.items()])
            try:
                self._db_client.executeSQL(sql)
            except:
                print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))

        def insert_sql(self, **alterations):
            dbfields = str(tuple(alterations.keys())).replace("'", '')
            dbvalues = tuple(alterations.values())
            sql = 'INSERT INTO {table} {dbfields} VALUES {dbvalues}'.format(table=self.table, dbfields=dbfields,
                                                                            dbvalues=dbvalues)
            sql = sql.replace("None", 'NULL')
            try:
                self._db_client.executeSQL(sql)
            except:
                print('%s SQL Update Fail %s' % (self.table, traceback.print_exc()))