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