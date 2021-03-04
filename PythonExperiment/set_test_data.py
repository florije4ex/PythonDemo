# @File    : set_test_data
# @Description:
# @Author  : yangbh
# @Department:研发-测试
# @Time    : 2021/3/3 17:14

areaCode, roleCode = '350200', 'MOM1'
# schoolId = 'TestDataSI%s' % StrTool.getRandomText(10, 0, 90, 10, 0, 0)
# parentId = 'TestDataPI%s' % StrTool.getRandomText(10, 0, 90, 10, 0, 0)

param_data = [
    ['ignore', None, '', '350200', 'A' * 20 + 'C'],  # areaCode
    ['ignore', None, '', 'S' * 22 + 'I'],  # schoolId
    ['ignore', None, '', 'P' * 20 + 'I'],  # parentId
    ['ignore', None, '', 'R' * 22 + 'C'],  # roleCode
]

# defalutDataList = [areaCode, schoolId, parentId, roleCode]

    # @pytest.mark.parametrize('areaCode, schoolId, parentId,roleCode', [test_datas for test_datas in
    #                                                                    ParamListTool.generator_input_params(
    #                                                                        defalutDataList, param_data)])
    # def test_get_module_land_page_check_field(self, areaCode, schoolId, parentId, roleCode):