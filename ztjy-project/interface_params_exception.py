# @File    : interface_params_exception
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/10/14 9:46


@pytest.mark.parametrize("dictClassCode,desc", [(None, 'None值'), ('', '空字符串'), (StrTool.getRandomText(10), '不存在的code')])
def test_get_dict_class_code_check_field_exception_input(self, dictClassCode, desc):
    """
    异常场景测试
    :param dictClassCode:
    :param desc:
    :return:
    """
    params = self.dictDataFacade.generator_params(dictClassCode)
    if dictClassCode is None:
        try:
            result = self.dictDataFacade.getByDictClassCode(params=params)
        except Exception as e:
            print('*' * 80)
            print(e.__str__())
            print('*' * 80)
            assert_that(e.__str__()).contains('NullPointerException')
        else:
            assert_that(result).is_equal_to([])
            assert_that(result).is_length(0)
    else:
        result = self.dictDataFacade.getByDictClassCode(params=params)
        assert_that(result).is_equal_to([])
        assert_that(result).is_length(0)

def test_get_dict_class_code_ignore_field(self):
    """
    缺少字段
    :return:
    """
    params = self.dictDataFacade.generator_params()
    try:
        result = self.dictDataFacade.getByDictClassCode(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains('NoSuchMethodException')
    else:
        assert_that(result).is_equal_to([])
        assert_that(result).is_length(0)

def test_get_dict_class_code_extra_field(self):
    """
    多字段
    :return:
    """
    params = self.dictDataFacade.generator_params('APP_GUIDE', '12312')
    try:
        result = self.dictDataFacade.getByDictClassCode(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains('NoSuchMethodException')
    else:
        assert_that(result).is_equal_to([])
        assert_that(result).is_length(0)
