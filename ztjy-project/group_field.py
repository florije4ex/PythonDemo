# @File    : group_field
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/10/13 14:03

def fixture_get_all_dict_class_code(self):
    dictClassCodes = DICT_DATA_DB().select_sql(groupBy='DICT_CLASS_CODE')
    dictClassCodeList = []
    for i in range(len(dictClassCodes)):
        code = dictClassCodes[i]['DICT_CLASS_CODE']
        dictClassCodeList.append(code)
    return dictClassCodeList



def fixture_get_all_data_by_one_dict_class_code(self, dictClassCode, enabled):
    dictDatas = DICT_DATA_DB().select_sql(DICT_CLASS_CODE=dictClassCode, ENABLE=enabled)
    dictDataList = []
    for i in range(len(dictDatas)):
        dictDataList.append({dictDatas[i]['DATA_NAME'], dictDatas[i]['DATA_CODE'], dictDatas[i]['ENABLE']})
    return dictDataList

time.sleep(0.1)


@pytest.mark.parametrize("fieldName", (
            'schoolId', 'userName', 'userId', 'optype', 'moduleId', 'moduleName', 'opTime', 'ip', 'remark', 'opDay'))
def test_add_OperSys_log_check_field_empty(self, fixture_data_init, fieldName):
    """
    字段传空字符串
    :return:
    """
    params = self.ILogManageFacad.generator_params_oprLog(schoolId=self.schoolId, userName=self.userName,
                                                          userId=self.userId, optype=self.optype,
                                                          moduleId=self.moduleId, moduleName=self.moduleName,
                                                          opTime=self.opTime, ip=self.ip, remark=self.remark,
                                                          opDay=DateTimeTool.getNowTime('%Y-%m-%d'))
    new = "''"
    lbStr = "'%s':" % fieldName
    rbStr = ","
    params2 = StrTool.replaceContentWithLBRB(str(params), new, lbStr, rbStr, 0)
    result = self.ILogManageFacad.sendOperSysLog(params=params2)

    assert_that(result).is_none()
    time.sleep(self.sleepTime)  # 防止执行过快导致无法查询到插入的数据，此处做等待时间
    # 查询插入的数据是否入库
    sql_query_value = OPER_SYS_LOG_DB().select_sql(user_id=self.userId, school_id=self.schoolId)
    if fieldName == 'schoolId' or fieldName == 'userId' or fieldName == 'moduleId' or fieldName == 'opTime':
        assert_that(len(sql_query_value)).is_equal_to(0)
    else:
        assert_that(len(sql_query_value)).is_equal_to(1)

@pytest.mark.parametrize("fieldName", (
        'schoolId', 'userName', 'userId', 'optype', 'moduleId', 'moduleName', 'opTime', 'ip', 'remark', 'opDay'))
def test_add_OperSys_log_check_field_is_null(self, fixture_data_init, fieldName):
    """
    字段传null值
    :return:
    """
    params = self.ILogManageFacad.generator_params_oprLog(schoolId=self.schoolId, userName=self.userName,
                                                          userId=self.userId, optype=self.optype,
                                                          moduleId=self.moduleId, moduleName=self.moduleName,
                                                          opTime=self.opTime, ip=self.ip, remark=self.remark,
                                                          opDay=DateTimeTool.getNowTime('%Y-%m-%d'))
    new = "null"
    lbStr = "'%s':" % fieldName
    rbStr = ","
    params2 = StrTool.replaceContentWithLBRB(str(params), new, lbStr, rbStr, 0)
    result = self.ILogManageFacad.sendOperSysLog(params=params2)

    assert_that(result).is_none()
    time.sleep(self.sleepTime)  # 防止执行过快导致无法查询到插入的数据，此处做等待时间
    # 查询插入的数据是否入库
    sql_query_value = OPER_SYS_LOG_DB().select_sql(user_id=self.userId, school_id=self.schoolId)
    if fieldName == 'moduleName' or fieldName == 'remark' or fieldName == 'opDay':
        assert_that(len(sql_query_value)).is_equal_to(1)
    else:
        assert_that(len(sql_query_value)).is_equal_to(0)