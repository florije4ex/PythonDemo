# @File    : dubbo_params
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/9 9:59

def generator_params1(self, *args):
    params = []
    for arg in args:
        if isinstance(arg, int):
            params.append({"type": "java.lang.Long", "data": arg})
        if isinstance(arg, str):
            params.append({"type": "java.lang.String", "data": arg})
    return params

def generator_params_oprLog(self, **kwargs):
    data = {}
    data.update(**kwargs)
    params = [{'type': 'com.ztjy.hms.server.model.dto.OperLogDto', 'data': data}]
    return params


def test_ignore_schoolId_growth_share_to_notice_machine(self):
    msgId = self.randomValue
    contentType = 100

    params = self.iNoticeFacade.generator_params1(growthId=msgId, contentType=contentType)
    try:
        result = self.iNoticeFacade.growthShareToNoticeMachine(params=params)
    except Exception as e:
        print('*' * 80)
        print(e.__str__())
        print('*' * 80)
        assert_that(e.__str__()).contains('NoSuchMethodException')
    else:
        assert_that(result).is_not_none()